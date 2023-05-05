import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
api_url = '<your-url>'
model_id = 'en-it'
text_to_translate = 'Your content you want translate here'

# Prepare the Authenticator


authenticator = IAMAuthenticator('FgvhJhrvyxG09ko05FnhABEiTGfQXW2jlKS0bjTMcLry')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com/instances/cc131269-1e43-4679-b902-462cbac0c5e0')

# Translate
translation = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()

# Print results
print(json.dumps(translation, indent=2, ensure_ascii=False))