from flask import Flask, render_template, request
from .directory import search

app = Flask(__name__)

@app.get("/")
def index():
	return render_template("index.html")

@app.post("/")
def find_username():
	query = request.form.get("query", "").strip().casefold()
	if not query:
		return render_template("error.html", message="You didn't send a username to look up.")

	if len(query) > 8:
		return render_template("error.html", message=f"The username you supplied ({query}) is greater than 8 characters.")

	results = search(query)
	name_claimed = any(result.get("email_domain") == "mit.edu" and query == result.get("email_id") for result in results)

	if name_claimed:
		return render_template("no.html", query=query, results=results)
	else:
		return render_template("yes.html", query=query)
