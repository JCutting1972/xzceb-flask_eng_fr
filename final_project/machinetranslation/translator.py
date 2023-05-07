
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator




api_key = ('iOPVcUJiht0UA4vvWs-b1RttqQ2aFLylFb3Dxzu0gsuA')
api_url = ('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/999bf2d6-20bf-4bff-b55a-3c47f0eae0a2')
model_id = 'en-fr'
text_to_translate = 'snail'







authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)


language_translator.set_service_url(api_url)

translation = language_translator.translate(

text = text_to_translate,model_id = model_id).get_result()
#
# return french_text
print(json.dumps(translation, indent=2, ensure_ascii=False))