import urllib2
import json
import re
from urllib2 import urlopen

API_BASE="http://bartjsonapi.elasticbeanstalk.com/api"

def lambda_handler(event, context):
    print (event)
    if (event["session"]["application"]["applicationId"] !=
            "amzn1.ask.skill.c7246ae0-c558-41fb-91f3-99285e81af20"):
        raise ValueError("Invalid Application ID")
    
    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])
    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

def on_session_started(session_started_request, session):
    print "Starting new session."

def on_launch(launch_request, session):
    return get_welcome_response()

def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]
    if intent_name == "knowhow":
        return KnowHow(intent)
    #elif intent_name == "simple_num":
    #    return Welcome()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...

def handle_session_end_request():
    card_title = "BART - Thanks"
    speech_output = "Thank you for using the BART skill.  See you next time!"
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))
    
def Welcome():
    session_attributes = {}
    card_title = "BART"
    speech_output = "Welcome to the add Caculator. " 
    reprompt_text = "Please ask me with two numbers, " \
                    "for example one plus two."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_welcome_response():
    session_attributes = {}
    card_title = "BART"
    speech_output = "Welcome to Alpha Calculator. " \
                    "I am the smartest Calculator in the world" \
                    "Just ask me whatever you want."
    reprompt_text = "" 
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def KnowHow(intent):
    print (intent)
    session_attributes = {}
    
    input_string = intent['slots']['word']['value']
    
    #input_string = "pi"
    html5_encoding={
        '\'':'%27',
        ' ':'%20',
    }
    
    for key, values in html5_encoding.items():
        input_string = input_string.replace(key, values)
    
    url_input = 'http://api.wolframalpha.com/v2/query?appid=W28765-8VEPU3RR3P&input={}&format=image,plaintext'.format(input_string)
    print ("url_input ready")
    response = urlopen(url_input)
    print ("start to read")
    html = response.read()
    print ("start to decode")
    html = html.decode('utf-8')
    html = html.replace("\n","")
    
    pod_re1 = [r'<pod[^>]*title=\'Result\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Decimal approximation\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Alternative representations\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Series representations\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Integral representations\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Solution\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Substitution\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Indefinite integral\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Derivative\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Values\'[^>]*>.*?</pod>|',
               r'<pod[^>]*title=\'Arc length of curve\'[^>]*>.*?</pod>|'
               
               ]
    pod_re = ''
    pod_re = pod_re.join(pod_re1)
    pod_re = r'(' + pod_re[:len(pod_re)-1] + r')'
    print (pod_re)
    pod_div = re.findall(pod_re, html)
   
    #pod_div = re.findall(r'<pod[^>]*Result[^>]*>.*?</pod>',html)
    print ("pod_div:{}".format(pod_div))
    result = re.findall(r'<plaintext>(.*)</plaintext>',pod_div[0])
    print ("result:{}".format(result))

    speech_output = result[0]
    card_title = "BART System Status"
    reprompt_text = ""
    should_end_session = True
    

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
