from flask import Flask, request, jsonify, render_template
import jinja2

import json
import sys
import os

from subprocess import Popen, PIPE


app = Flask(__name__)
app.config['DEBUG'] = True


# Default message for no additional address
@app.route("/")
def welcome():
    return render_template("info.html")


# View log
@app.route("/log")
def show_log():
    convert_log()
    return render_template("log.html")


# Clear log
@app.route("/log/clear")
def clear_log():
    f = open("templates/log.txt", "w")
    f.close()
    return render_template("log_cleared.html")


# Our call to receive a document POST
@app.route("/document", methods=["POST"])
def get_document():
    if request.is_json:
        data = request.get_json()
        # For understanding of JSON format, check crawling_schema.json

        # Check for lack of fields
        for key in ["url", "html", "docs"]:
            if key not in data:
                return "Required JSON fields not present", 400

        # Get file information for body
        fname = url_to_fname(data["url"])
        fname = "../data/" + fname + ".txt"
        ftype = "html"
        url = data["url"]

        eprint("LOG:\t(server)\tStarting text_transformation for", fname)

        outfile = open(fname, "w")
        json.dump(data["html"], outfile)
        outfile.close();

        # Start text_transformation subprocess
        Popen(["python3", "../src/text_transformation.py",
              fname, ftype, url],
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
            url = attachment[0]

            eprint("LOG:\t(server)\tStarting text_transformation for", fname)

            outfile = open(fname, "w")
            json.dump(attachment[2], outfile)
            outfile.close();

            # Start subprocess
            Popen(["python3", "../src/text_transformation.py",
                  fname, ftype, url],
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
    data = json.load(open("stopwords.json", "r"))
    # eprint("LOG:\t(server)\tSending stopwords to text_transformation")
    return jsonify(data)


# Test version of Indexing's /setToken
@app.route("/setToken", methods=["POST"])
def test_indexing_set_token():
    # While this works for my setup, it looks like indexing might have
    # something weird re: json vs plain text. TODO check with them
    if request.is_json:
        request_json = request.get_json()

        # Print to file (to check correctness)
        outfile = open("check.json", "w")
        json.dump(request_json, outfile, sort_keys=True, indent=4,
                  separators=(',', ':'))

        # Everything ok!
        # eprint("LOG:\t(server)\tReceived json data from text_transformation")
        return "Received JSON"
    else:
        # eprint("LOG:\t(server)\tReceived other from text_transformation")
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
    for char in [".", "/", ":", "#"]:
        url = url.replace(char, "_")
    while "__" in url:
        url = url.replace("__", "_")
    url = url.strip("_")
    return url


def convert_log():
    os.remove("templates/log.html")
    outfile = open("templates/log.html", "a")
    outfile.write("<!DOCTYPE html>\n<html lang='en'>\n<body>\n<p>\n")

    for line in open("templates/log.txt", "r"):
        html_line = "* " + line.replace("\n", " <br />\n")
        outfile.write(html_line)
    outfile.write("</p>\n</body>\n</html>\n")
    outfile.close()
