from flask import Flask, render_template
import json
from translator import english_to_french

app = Flask("Translator")
books = []

@app.route("/english_to_text")
def english_to_french(english_text):
    books.append({"translate to french": french_text})
    return "%s by %s appended" %(french_text)





@app.route("/english_to_french")
def englih_to_french(english_text):
    print(french_text)

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000