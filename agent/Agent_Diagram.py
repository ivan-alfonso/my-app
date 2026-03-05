# You may need to add your working directory to the Python path. To do so, uncomment the following lines of code
# import sys
# sys.path.append("/Path/to/directory/besser-agentic-framework") # Replace with your directory path

import json
import logging
import operator

from besser.agent.core.agent import Agent
from besser.agent.nlp.llm.llm_huggingface import LLMHuggingFace
from besser.agent.nlp.llm.llm_huggingface_api import LLMHuggingFaceAPI
from besser.agent.nlp.llm.llm_openai_api import LLMOpenAI
from besser.agent.nlp.llm.llm_replicate_api import LLMReplicate
from besser.agent.core.session import Session
from besser.agent.nlp.intent_classifier.intent_classifier_configuration import LLMIntentClassifierConfiguration, SimpleIntentClassifierConfiguration
from besser.agent.nlp.speech2text.openai_speech2text import OpenAISpeech2Text
from besser.agent.nlp.text2speech.openai_text2speech import OpenAIText2Speech

# Configure the logging module
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')


# Create the bot
agent = Agent('Agent_Diagram')
# Load bot properties stored in a dedicated file
agent.load_properties('config.ini')

# Define the platform your chatbot will use





platform = agent.use_websocket_platform(use_ui=True)
# LLM instantiation based on config['llm']




ic_config = SimpleIntentClassifierConfiguration(
    framework='pytorch',
    num_epochs=50,
    embedding_dim=128,
    hidden_dim=128,
    input_max_num_tokens=15,
    discard_oov_sentences=True,
    check_exact_prediction_match=True,
    activation_last_layer='sigmoid',
    lr=0.001
)

agent.set_default_ic_config(ic_config)

# Default LLM when no config or model provides one
reply_llm = LLMOpenAI(
    agent=agent,
    name='gpt-5-nano',
    parameters={}
)

##############################
# INTENTS
##############################
OpeningHours = agent.new_intent('OpeningHours', [
    'what are the opening hours?',
    'library hours',
    'when do you open?',
    'hours of operation',
    ],
    description='Asking for the opening hours of the library.'
)
CheapestBook = agent.new_intent('CheapestBook', [
    'how to get the title of the cheapest book of an author?',
    'I want to know the cheapest book',
    'which is the cheapest book?',
    ])
Contact = agent.new_intent('Contact', [
    'I need to speak to someone',
    'contact support',
    'human assistance',
    ],
    description='Requesting to speak with a human assistant.'
)
Other = agent.new_intent('Other', [
    ],
    description='Any other question.'
)


##############################
# STATES
##############################


Greeting = agent.new_state('Greeting', initial=True)
Idle = agent.new_state('Idle')
OpeningHoursState = agent.new_state('OpeningHoursState')
CheapestBookState = agent.new_state('CheapestBookState')
ContactState = agent.new_state('ContactState')



# Greeting
def Greeting_body(session: Session):
    reply_text = 'Welcome to the library support system!'
    session.reply(reply_text)
Greeting.set_body(Greeting_body)
Greeting.go_to(Idle)
# Idle
def Idle_body(session: Session):
    reply_text = 'How can I assist you today?'
    session.reply(reply_text)
Idle.set_body(Idle_body)
Idle.when_intent_matched(OpeningHours).go_to(OpeningHoursState)
Idle.when_intent_matched(CheapestBook).go_to(CheapestBookState)
Idle.when_intent_matched(Contact).go_to(ContactState)
# OpeningHoursState
def OpeningHoursState_body(session: Session):
    reply_text = 'Our opening hours are MondayFriday 9 AM6 PM.'
    session.reply(reply_text)
    reply_text = 'Saturday 10 AM4 PM. Closed Sunday.'
    session.reply(reply_text)
OpeningHoursState.set_body(OpeningHoursState_body)
OpeningHoursState.go_to(Idle)
# CheapestBookState
def CheapestBookState_body(session: Session):
    reply_text = 'To get the cheapest book of an author, follow these steps:'
    session.reply(reply_text)
    reply_text = '1. Go to the Library tab.'
    session.reply(reply_text)
    reply_text = '2. In the table, select the library where you want to search.'
    session.reply(reply_text)
    reply_text = '3. Click on Cheapest Book.'
    session.reply(reply_text)
    reply_text = '4. Select an author and click Execute.'
    session.reply(reply_text)
CheapestBookState.set_body(CheapestBookState_body)
CheapestBookState.go_to(Idle)
# ContactState
def ContactState_body(session: Session):
    reply_text = 'You can contact a librarian at library@example.com or call +1 555-123-4567.'
    session.reply(reply_text)
    reply_text = 'They will get back to you shortly.'
    session.reply(reply_text)
ContactState.set_body(ContactState_body)
ContactState.go_to(Idle)




# RUN APPLICATION

if __name__ == '__main__':
    agent.run()