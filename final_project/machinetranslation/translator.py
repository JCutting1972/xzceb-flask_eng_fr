
import json
import requests
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api_key = ('iOPVcUJiht0UA4vvWs-b1RttqQ2aFLylFb3Dxzu0gsuA')
api_url = ('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/999bf2d6-20bf-4bff-b55a-3c47f0eae0a2')
model_id = 'en-fr'
english_text = 'error'
#french_text = 'erro'

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator )

def EnglishToFrench(english_text):
    
    #english_text = input('Please enter text to translate: ')    
    text1 = english_text
    language_translator.set_service_url(api_url)
    translation = language_translator.translate(
    text = text1,model_id = 'en-fr').get_result()


   #
   # 
   # print(json.dumps(translation, indent=2, ensure_ascii=False)) 
      
    json_string = json.dumps(translation)#indent=2, ensure_ascii=False)
    parsed_response = json.loads(json_string)
    #print(json_string)
# Get dummy data using an API
#res = requests.get("http://dummy.restapiexample.com/api/v1/employees")
 
  #Convert data to dict
    
    
   
    
    french_text = parsed_response['translations'][0]['translation']
    #return french_text
    
    return french_text
    #print(english_text)
    #return french_text
    #print (french_text)
 
# Convert dict to string
   # Dict = json.dumps(translation) 
   # print(french_text)
    #print(type(french_text))




    #return french_text
    
    

EnglishToFrench(english_text)








