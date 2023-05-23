#from translator import english_to_french
#from translator import french_to_english
from flask import Flask, render_template, request
import json

import json
#import requests
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os


def pi_key = ('iOPVcUJiht0UA4vvWs-b1RttqQ2aFLylFb3Dxzu0gsuA')
api_url = ('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/999bf2d6-20bf-4bff-b55a-3c47f0eae0a2')
languages    =  'error'
english_text =  'error'
french_text  =  'error'
english_txt  =  'error'
french_txt   =  'error'

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator)


app = Flask("Web Translator")

#@app.route("/english_to_french")
@app.route('/process', methods=['POST'])
def processs_data():
    data = request.get_json()
    english_text = data['input1']
    languages = data['input2']
    french_text = english_to_French(english_text,languages)

    return jsonify({'result':french_text})
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

@app.route('/')
def index():
   # if request.method == 'POST':
    #   english_text = request.form['input']
     # # french_text = english_to_french(english_text,languages)
       #return french_text
      #eturn render_template('index.html', output = french_test)
       return render_template('index.html')   

    # Write the code to render template


def english_to_french(english_text,languages):
         
    #language_translator.set_service_url(api_url)
    #translation = language_translator.translate(
    #text = english_text, model_id = languages).get_result()
        
    #json_string = json.dumps(translation)
    #parsed_response = json.loads(json_string)
    #french_text = json_string
    
    #french_text = (parsed_response['translations'][0]['translation'])

    french_text = 
        
    return french_text

    

if __name__ == "__main__":
    app.run()

