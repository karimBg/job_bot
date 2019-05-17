# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional
from rasa_core_sdk import Action
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

# Our packages
from repository.job_data import get_job_data, list_jobs, generate_job_buttons
from repository.internship_data import list_internships, generate_internship_buttons

# jobs action
class action_job(Action):
    def name(self):
        return "action_job"
    def run(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot("job_title")
        user_id = (tracker.current_state())["sender_id"]

        # creates a list out of the existing jobs.
        possible_jobs = list_jobs(user_id)

        message = "These are the available job offers that i know about!"

        # generates a list of buttons from the list of possible_jobs
        buttons = generate_job_buttons(possible_jobs)

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

        # get all internship reference and project title ( recommended )
        possible_internships = list_internships(user_id)

        message = "These are the available internship offers that we have right now, use the Internship Reference to learn more about an offer!"

        # generates a list of buttons from the list of possible_internships
        buttons = generate_internship_buttons(possible_internships)

        dispatcher.utter_button_message(message, buttons)
        return []
        
#do nothing here
class internshipform(FormAction):
    """Example of a custom form action"""
    def name(self):
        """Unique identifier of the form"""
        return "internship_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["internshipRef"]
    def submit(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot("internshipRef")
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

# Job Option Action
class actionShowDetails(Action):
    def name(self):
        return "action_show_details"
    def run(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot("job_title")
        job_option = tracker.get_slot("JobOptions")
        user_id = (tracker.current_state())["sender_id"]

        #getting data from DB
        job_data = get_job_data(job_option, job_title, user_id)

        #put stuff from DB here 
        dispatcher.utter_message(f"{job_data}")
        return []

class actionAcquaintance(Action):
    def name(self):
        return "action_acquaintance"
    def run(self, dispatcher, tracker, domain):
        user_id = (tracker.current_state())["sender_id"]
        #data from data base here 
        dispatcher.utter_message("get acquaintance" + user_id)
        return []

        