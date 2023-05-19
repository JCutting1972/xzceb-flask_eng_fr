from translator import english_to_french
from translator import french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

#@app.route("/english_to_french")
@app.route('/', methods=['GET', 'POST'])
#def eng
#def englishToFrench(english_text,languages):
 #   english_text = request.args.get('Text to Translate')
   #textToTranslate = request.args.get('textToTranslate')
    # Write your code here
  #  return "Translated Text To French"
   # return french_text

#@app.route("/french_txt")
#def french_to_english(french_txt,languages):
 #   french_txt = request.args.get('Text To Translate')
    # Write your code here
  #  return "Translated Text To English"
   # return english_txt

#@app.route("/")
def index():
    if request.method == 'POST':
       english_text = request.form['english text']
       languages = request.form['model id']
       french_text = english_to_french(english_text,languages)
       return render_template('index.html', result = french_test)
    return render_template('index.html')   

    # Write the code to render template

if __name__ == "__main__":
    app.run(debug=True)
