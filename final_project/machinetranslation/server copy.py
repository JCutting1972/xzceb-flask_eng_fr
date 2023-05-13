from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")

def englishToFrench(english_text,languages):
    english_text = request.args.get('Text to Translate')
   #textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated Text To French"
    return french_text

@app.route("/french_txt")
def french_to_english(french_txt,languages):
    french_txt = request.args.get('Text To Translate')
    # Write your code here
    return "Translated Text To English"
    return english_txt


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
       english_text = request.form[english_text]
       english_text = request.form[languages]
       french_text = english_to_french(english_text,languages)
       #return render_template(index.html)
       return render_template('index.html')

    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
