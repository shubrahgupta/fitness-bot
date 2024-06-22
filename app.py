from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import os
from langchain_core.output_parsers import StrOutputParser
#TODO:generate requirements.txt file
prompts = {
    "/tip":"Generate a tip or motivational quote related to wellness/gym/diet. Don't include unnecessary information or text.",
    "/dietplan":"You are a certified nutritionist with 10 years experience. Generate a good health diet plan for a week according to the user's weight, height, bmi, purpose, and preference(veg/non-veg). If not stated, give a generic diet plan for good health. Also provide the approximate nutritional value per day. Don't include unnecessary information or text. Keep the answers summarized and concise.",
    "/workoutplan":"You are a certified personal fitness trainer with 10 years experience. Generate a good health workout plan for a day according to the user's weight, height, bmi, purpose, and exercise-mode. If not stated, give a generic exercise plan for good health. Also provide the approximate nutritional value per day. Don't include unnecessary information or text. Keep the answers summarized and concise.",
    "/query":"You are a certified personal fitness trainer and nutrition expert with 10 years experience. Answer the user's query with your best possible advice. Don't ask any follow-up question. Don't include unnecessary information or text. Keep the answers summarized and concise.",
           }

def openai_handler(user_response, category):
    parser = StrOutputParser()

    model = AzureChatOpenAI(
        model_name="gpt-35-turbo",
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        )

    messages = [
        SystemMessage(content=prompts[category]),
        HumanMessage(content=user_response),
    ]

    chain = model | parser
    response = chain.invoke(messages)
    print(response)
    return response



def msg_handler(incoming_msg):

    if '/start' in incoming_msg:
        response = """Hi, start your wellness journey now. please use '/tip' or '/dietplan' or '/workoutPlan' or '/reminder' or '/query' tag along with the information needed.
                    \nThese templates can be used:
                    \n'/dietplan weight: 50Kg, height: 5 feet, purpose: muscle-enhancement, non-veg food'
                    \n'/workoutplan weight: 50Kg, height: 5 feet, purpose: leg-muscles-enhancement, exercise mode: mid'
                    \n'/query I am unable to feel my back-muscle while doing lat-pull downs. What should I do to improve?'
                    \n'/tip'
                    """
    elif '/tip' in incoming_msg:
        response = openai_handler("",'/tip')
    elif '/dietplan' in incoming_msg:
        response = openai_handler(incoming_msg,'/dietplan')
    elif '/workoutplan' in incoming_msg:
        response = openai_handler(incoming_msg,'/workoutplan')
    elif '/query' in incoming_msg:
        response = openai_handler(incoming_msg,'/query')
    else:
        response = """Sorry! I only answer to the tags, please use '/tip' or '/dietplan' or '/workoutPlan' or '/reminder' or '/query' along with the information needed.
                    \nThese templates can be used:
                    \n'/dietplan weight: 50Kg, height: 5 feet, purpose: muscle-enhancement, non-veg food'
                    \n'/workoutplan weight: 50Kg, height: 5 feet, purpose: leg-muscles-enhancement, exercise mode: mid'
                    \n'/query I am unable to feel my back-muscle while doing lat-pull downs. What should I do to improve?'
                    \n'/tip'

                    """
    return response

    

app = Flask(__name__)
@app.route('/',methods=['GET'])
def hello():
    return 'Hello all!'

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    """Respond to incoming messages with a friendly SMS."""
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(msg_handler(incoming_msg))
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
