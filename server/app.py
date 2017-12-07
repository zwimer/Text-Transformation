from flask import Flask
from flask import request
from flask import jsonify

import json
import sys

from subprocess import Popen

app = Flask(__name__)

# easy print to error
# code from stackoverflow:
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Default message for no additional address
@app.route("/")
def welcome():
    return "LSPT Text Transformation (Z)\n"

# Test version of Indexing's /stopWords
@app.route("/stopWords", methods=["GET"])
def return_stopwords():
    data = json.load( open("stopwords.json", "r") )
    eprint("LOG:\t(server)\tSending stopwords to text_transformation")
    return jsonify(data)

# Test version of Indexing's /setToken
@app.route("/setToken", methods=["POST"])
def receive_token():
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
        return "POST OK"
    else:
        eprint("LOG:\t(server)\tReceived other from text_transformation")
        return "WRONG FORMAT"

# Used in /document calls to create a filename out of a URL
def url_to_fname(url):
    for char in [".", "/", ":", "#",]:
        url = url.replace(char, "_")
    while "__" in url:
        url = url.replace("__", "_")
    url = url.strip("_")
    return url

# Our call to receive a document POST
# Right now this just creates files and does not start text_transformation
# because the subprocess calls are wrong somehow
# TODO trigger text_transformation in this function
@app.route("/document", methods=["POST"])
def get_document():

    if request.is_json:
        data = request.get_json()
        # For understanding of JSON format, check crawling.json

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
            # Get file info
            fname = "../data/" + url_to_fname(attachment[0]) + ".txt"
            ftype = attachment[1]

            eprint("LOG:\t(server)\tStarting text_transformation for", fname)

            outfile = open(fname, "w")
            json.dump(attachment[2], outfile)

            # Start subprocess
            Popen(["python3", "../src/text_transformation.py", fname, ftype], \
                shell=False, stdin=None, stdout=None, stderr=2)

        return "POST OK"

    else:
        return "WRONG FORMAT"
