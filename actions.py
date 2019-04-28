# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional
from rasa_core_sdk import Action
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

#ignore this class
class details_job_action(Action):
    def name(self):
        return "details_job_action"
    @staticmethod
    def required_slots(tracker):
        # type: () -> List[Text]
        return ["JobOptions"]
    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        job_title = tracker.get_slot("job_title")
        print(tracker.get_slot("JobOptions"))
        dispatcher.utter_message("slot_values")
        dispatcher.utter_message(job_title)
        return []

#and this class too
class action_job(Action):
    def name(self):
        return "action_job"
    def run(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot("job_title")
        possible_jobs = [{"job_title" : "web developer"}, {"job_title": "web integrator"}, {"job_title": "software developer"}]
        message = "those the available jobs offers we have"
        buttons = []
        for job in possible_jobs:
            title = (job["job_title"])
            payload = ('/slot{\"job_title\": '+ job["job_title"] + '}')
            buttons.append({ "title": title, "payload": payload })
        dispatcher.utter_button_message(message, buttons)
        return [SlotSet("job_title", job_title)]

#and this ( just testing stuff i may need later on)
class action_ask_details(Action):
    def name(self):
        return "action_ask_details"
    def run(self, dispatcher, tracker, domain):
        Job_Options = [{"JobOptions" : "mission"}, {"JobOptions": "description"}, {"JobOptions": "date"}]
        message = "click to learn more"
        buttons = []
        for detail in Job_Options:
            title = (detail["JobOptions"])
            payload = ('/slot{\"JobOptions\": '+ detail["JobOptions"] + '}')
            buttons.append({ "title": title, "payload": payload })
        dispatcher.utter_button_message(message, buttons)
        job_option = tracker.get_slot("JobOptions")
        return [SlotSet("JobOptions",job_option)]

#this where it works ( check stories )
class jobs_form(FormAction):
    """Example of a custom form action"""
    def name(self):
        """Unique identifier of the form"""
        return "jobs_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["job_title"]
    def submit(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot("job_title")
       	dispatcher.utter_template('utter_submit', tracker)
        return []

class Actioncontact(Action):
    def name(self):
        return "action_contact"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("hello")
        #ignore this 
        results = [
            {
                "rec_create_date": "12 Jun 2016",
                "rec_dietary_info": "nothing",
                "rec_dob": "01 Apr 1988",
                "rec_first_name": "New",
                "rec_last_name": "Guy",
            }]
        return results

class ActionInternship(Action):
    def name(self):
        return "action_internship"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("hello")
        return ["hello","hello"]

class actionShowDetails(Action):
    def name(self):
        return "action_show_details"
    def run(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot("job_title")
        job_option = tracker.get_slot("JobOptions")  
        ## put stuff from database here
        dispatcher.utter_message("get " + job_option+" of "+ job_title )
        return []
