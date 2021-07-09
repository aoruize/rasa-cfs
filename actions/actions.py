# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from re import X
from typing import Any, Text, Dict, List
from threading import Timer

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ActionExecuted

import os
import openai

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
        inputQuestion = tracker.latest_message.get("text")
        searchingMessage = "Here's the most relevant result for '" + inputQuestion + "':"

        dispatcher.utter_message(text=searchingMessage)

        
        # Send semantic search query to OpenAI API using Babbage engine.
        # Returns up to the max_rerank number of documents, along with their search scores.
        # Read more on the API documentation: https://beta.openai.com/docs/api-reference/searches
        apiResponse = openai.Engine("babbage").search(
            search_model="babbage", 
            query=inputQuestion, 
            max_rerank=50,
            file="file-THEa0jeIEul23nFUj1L8nlVu" # https://api.openai.com/v1/files
        )

        # Sort the responses by their search scores in descending order
        sortedResponse = sorted(apiResponse["data"], key=lambda x: x["score"], reverse=True)
        
        # Split the highest scoring response into messages, using new line as split parameter
        returnMessages = (sortedResponse[0]["text"]).split("\n")

        # Send return messages to the user
        for returnMessage in returnMessages:
            t = Timer(0.5, dispatcher.utter_message(text=returnMessage))
            t.start() # after 0.5 seconds, the returnMessage will be sent

        # Returns ActionExecuted event to list of Events
        return [ActionExecuted("action_search_library", policy=None)]
