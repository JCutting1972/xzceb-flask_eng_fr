from flask import Flask, render_template, request
import json
import os
import tests
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests

app = Flask(__name__)


api_key = ('iOPVcUJiht0UA4vvWs-b1RttqQ2aFLylFb3Dxzu0gsuA')
api_url = ('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/999bf2d6-20bf-4bff-b55a-3c47f0eae0a2')
languages =    'error1'
english_text = 'error2'
french_text =  'error3'
english_txt =  'error4'
french_txt =   'error5'
translation =  'error6'

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
version = '2018-05-01',
authenticator = authenticator)
@app.route("/")
def page():
 return render_template('input.html')

@app.route("/english_to_french", methods = ['GET', 'POST']) 
def english_to_french():
 if request.method == 'POST':
  english_text = request.form['input_text']
  
  invale = english_text
  language_translator.set_service_url(api_url)
  translation = language_translator.translate(
  text = invale, model_id = 'en-fr').get_result()
  json_string = json.dumps(translation)
  parsed_response = json.loads(json_string)

  french_text = (parsed_response['translations'][0]['translation'])
  output=french_text
  return render_template("output.html",output=output)
 

@app.route("/french_to_english", methods = ['GET', 'POST']) 
def french_to_english():
 if request.method == 'POST':
  french_txt = request.form['input_text2']

  invale2 = french_txt
  language_translator.set_service_url(api_url)
  translation = language_translator.translate(
  text = invale2, model_id = 'fr-en').get_result()
  json_string = json.dumps(translation)
  parsed_response = json.loads(json_string)

  english_txt = (parsed_response['translations'][0]['translation'])
  output2 = english_txt
  return render_template("output2.html",output=output2)

if __name__=='__main__':
 app.run(debug=True)