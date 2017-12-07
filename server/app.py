from flask import Flask
from flask import request
from flask import jsonify

import json
import subprocess

app = Flask(__name__)

# Default message for no additional address
@app.route("/")
def welcome():
    return "LSPT Text Transformation (Z)\n"

# Test version of Indexing's /stopWords
@app.route("/stopWords", methods=["GET"])
def return_stopwords():
    data = json.load( open("stopwords.json", "r") )
    print("LOG: Sending stopwords to text_transformation")
    return jsonify(data)

# Test version of Indexing's /setToken
@app.route("/setToken", methods=["POST"])
def receive_token():
    # While this works for my setup, it looks like indexing might have something
    # weird re: json vs plain text. TODO check with them
    if request.is_json:
        print("LOG: Received json from text_transformation")
        request_json = request.get_json()
        print( json.dumps(request_json, sort_keys=True, indent=4) )
        print("LOG: JSON ^^^^^^^^^")
        return "POST OK"
    else:
        print("LOG: Received other from text_transformation")
        return "WRONG FORMAT"

# Used in /document calls to create a filename out of a URL
def url_to_fname(url):
    for char in [".", "/", ":", "#", "__"]:
        url = url.replace(char, "_")
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

        # Start text_transformation for body
        fname = url_to_fname(data["url"])
        fname = "../data/" + fname + ".txt"
        ftype = "html"

        print("LOG: Starting text_transformation for", fname)

        outfile = open(fname, "w")
        json.dump(data["html"], outfile)
        #subprocess.run(["python3", "../src/text_transformation.py", \
        #    fname, "html"])

        for attach in data["docs"]:
            fname = "../data/" + url_to_fname(attach[0]) + ".txt"
            ftype = attach[1]

            print("LOG: Starting text_transformation for", fname)

            outfile = open(fname, "w")
            json.dump(attach[2], outfile)
            #subprocess.run(["python3", "../src/text_transformation.py", \
            #    fname, "html"])

        return "POST OK"

    else:
        return "WRONG FORMAT"
