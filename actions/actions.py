# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ActionExecuted

import os
import openai
import jsonlines

# OpenAI authorization
openai.organization = "org-MVRMhL527YpFJrqDkAP9ivu5"
openai.api_key = os.getenv("OPENAI_API_KEY")

class ActionSearchLibrary(Action):

    def name(self) -> Text:
        return "action_search_library"

    async def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get user's message
        inputQuestion = tracker.latest_message.text
    
        dispatcher.utter_message(text="Searching through CFS Library...")

        try:
            # Send semantic search query to OpenAI API using Babbage engine
            response = openai.Engine("babbage").search(
                search_model="babbage", 
                query=inputQuestion, 
                max_rerank=5,
                file="file-THEa0jeIEul23nFUj1L8nlVu" # https://api.openai.com/v1/files
            )

            return_message = "This is what I found:\n" + response
            dispatcher.utter_message(text=return_message)

        except:
            dispatcher.utter_message("There was an error in requesting the OpenAI search, as the CFS file is being processed.")

        
        return [ActionExecuted("action_search_library", policy=None)]
