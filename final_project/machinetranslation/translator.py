
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os



api_key = ('kFgvhJhrvFgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLryyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLry')
url = ['https://api.au-syd.assistant.watson.cloud.ibm.com/instances/cc131269-1e43-4679-b902-462cbac0c5e0l']
model_id = 'en-it'
text_to_translate = 'blue'






authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version=('2018-05-01'),translation = language_translator.translate(
    text_to_translate = 'lobster'
    
    authenticator=authenticator

)

language_translator.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com/instances/cc131269-1e43-4679-b902-462cbac0c5e0')

translation = language_translator.translate(
    text=text_to_translate,
    'en-it').get_result()


#
# return french_text
print(json.dumps(translation, indent=2, ensure_ascii=False))

