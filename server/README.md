# app.py

The Flask server. To start the server (assuming you have Flask installed), run
```
export FLASK_APP=app.py
flask run --hostname=0.0.0.0 --port=8080
```
with the last option used if you want a public server. The server runs on port 8080

### Functionality

1. `http://<address>:8080/` will return a description message
2. `http://<address>:8080/stopWords` is a testing function to replicate the call to Indexing to get stopwords. It takes GET requests only and returns JSON
3. `http://<address>:8080/setToken` is a testing function to replicate the call to Indexing to give them our data. It takes POST requests only and returns "POST OK" or "WRONG FORMAT"
4. `http://<address>:8080/document` is a function to take in documents from crawling and save the document html and the body of each linked document in order to run text_transformation on each. It takes POST requests only and returns "POST OK" or "WRONG FORMAT" (**TODO**: make these more formal and actually have error responses...)

# crawling.py

A short program to send crawling data to the server. Run
```
python3 crawling.py
```
It should result in a response of `POST OK` and nothing else. The server will have created files in the top-level `data` folder

# text_transformation.py

**TODO**: Add actual url to json output instead of filename

Very similar to the version in the master branch, but GETs stopwords from this server, assumed to be running locally on port 8080, and POSTs its output to the server. The server should print the output. The command to run this is the same
