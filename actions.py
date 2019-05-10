# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional
from rasa_core_sdk import Action
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

# jobs action
class action_job(Action):
    def name(self):
        return "action_job"
    def run(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot("job_title")
        user_id = (tracker.current_state())["sender_id"]
        #in possible_jobs get the titles of the jobs from the database of user_id ( entreprise id )
        possible_jobs = [{"job_title" : "web developer"}, {"job_title": "web integrator"}, {"job_title": "software developer"}]
        message = "those the available jobs offers we have"
        buttons = []
        for job in possible_jobs:
            title = (job["job_title"])
            payload = ('/slot{\"job_title\": '+ job["job_title"] + '}')
            buttons.append({ "title": title, "payload": payload })
        dispatcher.utter_button_message(message, buttons)
        return [SlotSet("job_title", job_title)]

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


#internship actions
class InternshipAction(Action):
    def name(self):
        return "action_internship"
    def run(self, dispatcher, tracker, domain):
        user_id = (tracker.current_state())["sender_id"]
        internship_title ="islem"
        # get all internship titles
        possible_internship = [{"internship_title" : "web developer"}, {"internship_title": "web integrator"}, {"internship_title": "software developer"}]
        message = "those the available internship offers we have"
        buttons = []
        for job in possible_jobs:
            title = (job["internship_title"])
            payload = ('/slot{\"internship_title\": '+ job["internship_title"] + '}')
            buttons.append({ "title": title, "payload": payload })
        dispatcher.utter_button_message(message, buttons)
        return [SlotSet("internship_title", internship_title)]

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
        user_id = (tracker.current_state())["sender_id"]        
        #get contact of user_id 
        dispatcher.utter_message("hello")
        return []

class actionShowDetails(Action):
    def name(self):
        return "action_show_details"
    def run(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot("job_title")
        job_option = tracker.get_slot("JobOptions")  
        user_id = (tracker.current_state())["sender_id"]        
        #put stuff from database here 
        dispatcher.utter_message("get " + job_option+" of "+ job_title )
        return []

class actionAcquaintance(Action):
    def name(self):
        return "action_acquaintance"
    def run(self, dispatcher, tracker, domain):
        user_id = (tracker.current_state())["sender_id"]
        #data from data base here 
        dispatcher.utter_message("get acquaintance" + user_id)
        return []
