### When updating/changing URL

- server/crawling.py:10
- src/text_transformation.py:103
- src/text_transformation.py:212

# app.py

**TODO** add a page that writes the log, so we can check it easily

The Flask server. To make the server findable by Flask (assuming you have Flask installed), run `export FLASK_APP=app.py`. To run:

- locally: `flask run --port=8080`
- externally: `flask run --hostname=0.0.0.0 --port=8080`

### Functionality

1. `http://<address>:8080/` will return a description message
2. `http://<address>:8080/stopWords` is a testing function to replicate the call to Indexing to get stopwords. It takes GET requests only and returns JSON
3. `http://<address>:8080/setToken` is a testing function to replicate the call to Indexing to give them our data. It takes POST requests only and returns 200 or 415  w/ relevant messages if it handles the response (other responses are handled by Flask)
4. `http://<address>:8080/document` is a function to take in documents from crawling and save the document html and the body of each linked document in order to run text_transformation on each. It takes POST requests only and returns 200 or 415 w/ relevant messages if it handles the response (other responses are handled by Flask)

# crawling.py

A short program to send test crawling data to the server. Run `python3 crawling.py`. It should result in a response of `Received JSON` and nothing else. The server will have created files to send to text_transformation in the top-level `data` folder and a JSON output file `check.json` in the `server` folder.

# text_transformation.py

**TODO**: Add actual url to json output instead of filename

Very similar to the version in the master branch, but GETs stopwords from this server, assumed to be running locally on port 8080, and POSTs its output to the server. The server should print the output. The command to run this is the same, but you should never need to run it as the server will call it.
