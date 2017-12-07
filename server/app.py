from flask import Flask, request, jsonify

import json
import sys

from subprocess import Popen

app = Flask(__name__)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return "That page doesn't exist\n" + usage(), 404

# Default message for no additional address
@app.route("/")
def welcome():
    return "LSPT Text Transformation (Z)\n" + usage()

# Our call to receive a document POST
@app.route("/document", methods=["POST"])
def get_document():
    if request.is_json:
        data = request.get_json()
        # For understanding of JSON format, check crawling_schema.json

        # Check for lack of fields
        for key in ["url", "html", "docs"]:
            if not key in data:
                return "Required JSON fields not present", 400

        # Get file information for body
        fname = url_to_fname(data["url"])
        fname = "../data/" + fname + ".txt"
        ftype = "html"

        eprint("LOG:\t(server)\tStarting text_transformation for", fname)

        outfile = open(fname, "w")
        json.dump(data["html"], outfile)

        # Start text_transformation subprocess
        Popen(["python3", "../src/text_transformation.py", fname, "html"], \
            shell=False, stdin=None, stdout=None, stderr=2)

        # For each attached document
        for attachment in data["docs"]:

            # check for bad data - harder to do this one since there are no
            # fields... :(
            if len(attachment) != 3:
                return "Required JSON fields not present", 400

            # Get file info
            fname = "../data/" + url_to_fname(attachment[0]) + ".txt"
            ftype = attachment[1]

            eprint("LOG:\t(server)\tStarting text_transformation for", fname)

            outfile = open(fname, "w")
            json.dump(attachment[2], outfile)

            # Start subprocess
            Popen(["python3", "../src/text_transformation.py", fname, ftype], \
                shell=False, stdin=None, stdout=None, stderr=2)

        return "Received JSON"
    else:
        return "Unsupported media type - data is not JSON", 415

# =============================================================================
# TEST FUNCTIONS
# =============================================================================

# Test version of Indexing's /stopWords
@app.route("/stopWords", methods=["GET"])
def test_indexing_stopwords():
    data = json.load( open("stopwords.json", "r") )
    eprint("LOG:\t(server)\tSending stopwords to text_transformation")
    return jsonify(data)

# Test version of Indexing's /setToken
@app.route("/setToken", methods=["POST"])
def test_indexing_set_token():
    # While this works for my setup, it looks like indexing might have something
    # weird re: json vs plain text. TODO check with them
    if request.is_json:
        request_json = request.get_json()

        # Print to file (to check correctness)
        outfile = open("check.json", "w")
        json.dump(request_json, outfile, sort_keys=True, indent=4,
                  separators=(',', ':'))

        # Everything ok!
        eprint("LOG:\t(server)\tReceived json data from text_transformation")
        return "Received JSON"
    else:
        eprint("LOG:\t(server)\tReceived other from text_transformation")
        return "Unsupported media type - data is not JSON", 415

# =============================================================================
# UTILS
# =============================================================================

# print to error - code from stackoverflow:
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Used in /document calls to create a filename out of a URL
def url_to_fname(url):
    for char in [".", "/", ":", "#",]:
        url = url.replace(char, "_")
    while "__" in url:
        url = url.replace("__", "_")
    url = url.strip("_")
    return url

# returns info string for server users
def usage():
    info = ("Pages:\n"
            "\t/document :\n"
            "\t\taccepts POST\n"
            "\t\texpects type 'application/json'\n"
            "\t\texpects fields:\n"
            "\t\t{\n"
            "\t\t\t'html' : html body of page\n"
            "\t\t\t'docs' : [\n"
            "\t\t\t\t[\n"
            "\t\t\t\t\tlink to first attached document,\n"
            "\t\t\t\t\tdocument extension/type,\n"
            "\t\t\t\t\ttext body of document,\n"
            "\t\t\t\t],\n"
            "\t\t\t\tetc\n"
            "\t\t\t],\n"
            "\t\t\t'url' : site url\n" )
    return info
