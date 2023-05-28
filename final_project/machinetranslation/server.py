from translator import english_to_french
#from translator import french_to_english
from flask import Flask, render_template, request
import json
english_text = 'errror'
languages = 'en-fr'
#import jsonify
#import requests
#from ibm_watson import LanguageTranslatorV3
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#import os




app = Flask("Web Translator")

#
@app.route("/process", methods = ['GET', 'POST'])

def processs_data():
    data = request.get_json()
    
    
   # print(data)
   # json_string = json.dumps(data)
    parsed_data = json.loads(data)
    english_text = parsed_data['input1']
    
    languages= parsed_data['input2']
    print(languages)
    print(english_text)

   #global french_text



english_to_french(english_text, languages)



    
    
    
    
    
    
    
 # return french_text

    
    
    
    #english_text 
    
    #french_text = json_string
    
    #french_text = (parsed_response['translations'][0]['translation'])

    #french_text = 
        
    #return french_text


    #french_text = english_to_French(english_text,languages)
    
    


#@app.route('/retrieve', methods=['GET'])
#def retrieve_data():
  
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


#def english_to_french(english_text,languages):
         
    #language_translator.set_service_url(api_url)
    #translation = language_translator.translate(
    #text = english_text, model_id = languages).get_result()
        
    #json_string = json.dumps(translation)
    #parsed_response = json.loads(json_string)
    #french_text = json_string
    
    #french_text = (parsed_response['translations'][0]['translation'])

   # french_text = 
        
    #return french_text

    

if __name__ == "__main__":
    app.run()

