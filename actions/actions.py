from datetime import datetime
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests  # Ensure you import requests for the HTTP calls
import logging

# Initialize logger
logger = logging.getLogger(__name__)

class ActionCurrentTime(Action):

    def name(self) -> Text:
        return "action_current_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the current time
        current_time = datetime.now().strftime("%H:%M")

        # Send the current time as a message
        dispatcher.utter_message(text=f"The current time is {current_time}.")

        return []


class ActionFetchTaxAdvice(Action):

    def name(self) -> str:
        return "action_ask_tax"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_query = tracker.latest_message.get('text')

        url = "https://prod-tod-api.gateai.co/hmrc/graph/chat"
        payload = {
            "query": user_query,
            "history": []
        }
        logger.info("Payload for tax query: %s", payload)  # Log the payload

        try:
            response = requests.post(url, json=payload, timeout=10)  # Set a timeout of 10 seconds
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()
            status = data.get('status')

            if status == "success":
                response_text = data.get('response', 'No response available.')
                if response_text:  # Check if response_text is not empty
                    dispatcher.utter_message(text=response_text)
                else:
                    dispatcher.utter_message(text="The service returned an empty response. Please try again later.")
            else:
                dispatcher.utter_message(text="Sorry, I couldn't fetch the information at the moment. Please try again later.")

        except requests.exceptions.Timeout:
            dispatcher.utter_message(text="Sorry, the request to the tax service timed out. Please try again.")
            logger.error("Request timed out for query: %s", user_query)
        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(text="Sorry, I encountered an error while connecting to the tax service.")
            logger.error("Request error for query %s: %s", user_query, e)
        except Exception as e:
            dispatcher.utter_message(text="Sorry, I encountered an unexpected error.")
            logger.error("Unexpected error for query %s: %s", user_query, e)

        return []


class ActionFetchTaxAdviceFromFile(Action):

    def name(self) -> str:
        return "action_ask_tax_from_file"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_query = tracker.latest_message.get('text')

        url = "https://prod-tod-api.gateai.co/hmrc/graph/chat"
        path=""
        payload = {
            "query": user_query,
            "history": [],
            "file_path": path
        }
        logger.info("Payload for tax query: %s", payload)  # Log the payload

        try:
            response = requests.post(url, json=payload, timeout=10)  # Set a timeout of 10 seconds
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()
            status = data.get('status')

            if status == "success":
                response_text = data.get('response', 'No response available.')
                if response_text:  # Check if response_text is not empty
                    dispatcher.utter_message(text=response_text)
                else:
                    dispatcher.utter_message(text="The service returned an empty response. Please try again later.")
            else:
                dispatcher.utter_message(text="Sorry, I couldn't fetch the information at the moment. Please try again later.")

        except requests.exceptions.Timeout:
            dispatcher.utter_message(text="Sorry, the request to the tax service timed out. Please try again.")
            logger.error("Request timed out for query: %s", user_query)
        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(text="Sorry, I encountered an error while connecting to the tax service.")
            logger.error("Request error for query %s: %s", user_query, e)
        except Exception as e:
            dispatcher.utter_message(text="Sorry, I encountered an unexpected error.")
            logger.error("Unexpected error for query %s: %s", user_query, e)

        return []
