
import json
import requests
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

api_key = ('iOPVcUJiht0UA4vvWs-b1RttqQ2aFLylFb3Dxzu0gsuA')
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

def english_to_french(english_text,languages):
         
    language_translator.set_service_url(api_url)
    translation = language_translator.translate(
    text = english_text, model_id = languages).get_result()
        
    json_string = json.dumps(translation)
    parsed_response = json.loads(json_string)
    french_text = (parsed_response['translations'][0]['translation'])
        
    return french_text

def french_to_english(french_txt,languages):          
    
    language_translator.set_service_url(api_url)
    translation = language_translator.translate(
    text = french_txt, model_id = languages).get_result()
        
    json_string = json.dumps(translation)
   
    parsed_response = json.loads(json_string)
    english_txt = (parsed_response['translations'][0]['translation'])
        
    return english_txt





    
    
    










