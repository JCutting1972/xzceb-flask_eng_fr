
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os



api_key = ['apikFgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLryey']
url = ['https://api.au-syd.assistant.watson.cloud.ibm.com/instances/cc131269-1e43-4679-b902-462cbac0c5e0l']
model_id = 'en-it'
text_to_translate = 'blue'



api_key = ['apikFgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLryey']
api_key = ['apikFgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLryey']
api_key = ['apikFgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLryey']
authenticator = IAMAuthenticator(
language_translator = LanguageTranslatorV3(
    version=(2018-5-1),
    authenticator=authenticator

)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def EnglishToFrench(english_text):
    translation = language_translator.text_to_translate,model_id = model_id,get.result()
    return french_text
    print(json.dumps(translation, indent=2, ensure_ascii=False))