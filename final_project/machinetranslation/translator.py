
import json
import requests
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

api_key = ('iOPVcUJiht0UA4vvWs-b1RttqQ2aFLylFb3Dxzu0gsuA')
api_url = ('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/999bf2d6-20bf-4bff-b55a-3c47f0eae0a2')
languages    =  'error1'
english_text =  'error2'
french_text  =  'error3'
english_txt  =  'error4'
french_txt   =  'error5'
translation  =  'error6'

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator)

def english_to_french(english_text):
   #english_text = input('Enter English: ')
    language_translator.set_service_url(api_url)
    translation = language_translator.translate(
    text = english_text, model_id = 'en-fr').get_result()
        
    json_string = json.dumps(translation)
    parsed_response = json.loads(json_string)
    #parsed_data = json_string

    

    french_text = (parsed_response['translations'][0]['translation'])
    
    #output_dict = {'translation': output}

    #french_text = json.dumps(output_dict)
    
    
    #print(french_text)
    return french_text

    #print(output_json)
    
    
#print(translation)   
    #return fr

def french_to_english(french_txt):          
    #french_txt = input('Enter French: ')
    language_translator.set_service_url(api_url)
    translation = language_translator.translate(
    text = french_txt, model_id = 'fr-en').get_result()
        
    json_string = json.dumps(translation)
   
    parsed_response = json.loads(json_string)

    english_txt= (parsed_response['translations'][0]['translation'])
    

   
    #print(english_txt)    
    return english_txt
#english_text = 'Blue'
#languages = 'en-fr'

english_to_french(english_text)

french_to_english(french_txt)


    
    
    










