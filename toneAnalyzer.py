import json
import os
from pprint import pprint
from dotenv import load_dotenv, find_dotenv

from watson_developer_cloud import ConversationV1
from watson_developer_cloud import ToneAnalyzerV3

def invokeToneConversation(payload, maintainToneHistoryInContext=True):
    # load the .env file containing your environment variables for the required
    # services (conversation and tone)
    load_dotenv(find_dotenv())

    # replace with your own tone analyzer credentials
    tone_analyzer = ToneAnalyzerV3(
        username=os.environ.get('TONE_ANALYZER_USERNAME') or '0480936e-64df-4a8f-a420-0c59d557555c',
        password=os.environ.get('TONE_ANALYZER_PASSWORD') or 'SvzV7J6HjZDE',
        version='2016-04-01')

    # replace with your own workspace_id
    workspace_id = os.environ.get('WORKSPACE_ID') or 'YOUR WORKSPACE ID'

    """
     invokeToneConversation calls the the Tone Analyzer service to get the
     tone information for the user's input text (input['text'] in the payload
     json object), adds/updates the user's tone in the payload's context,
     and sends the payload to the
     conversation service to get a response which is printed to screen.
     :param payload: a json object containing the basic information needed to
     converse with the Conversation Service's message endpoint.
     :param maintainHistoryInContext:
     Note: as indicated below, the console.log statements can be replaced
     with application-specific code to process the err or data object
     returned by the Conversation Service.
    """
    tone = tone_analyzer.tone(text=payload)
    return tone


# synchronous call to conversation with tone included in the context
# pprint(invokeToneConversation(payload, maintainToneHistoryInContext))

path = r"F:\MyProjects\MLH_prime\data\reviews_vector\\"

for i in os.listdir(path):
    if i.endswith("_vector.csv"):
        try:
            print(i)
            payload = ""
            count = 0
            with open(path + i) as ih:
                for line in ih:
                    if count <= 50:
                        payload += " " + line.split(",")[0]
                        count += 1
                        
                    else:
                        break
            tone = invokeToneConversation(payload)

            for emotion in tone['document_tone']['tone_categories']:
                if emotion['category_id'] == 'emotion_tone':
                    print(emotion['tones'])
        except: pass