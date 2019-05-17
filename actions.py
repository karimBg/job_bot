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

class ApplyForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "apply_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["jobRef","name", "experience_years",
                "phone_number", "email","cv_link"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"jobRef": self.from_entity(entity="jobRef",
                                            intent=["inform_apply","inform_job"]),
                "name": self.from_entity(entity="name",
                                                intent="inform_apply"),                            
                "experience_years": [self.from_entity(entity="experience_years",
                                                intent=["inform_apply",
                                                        "apply_job"]),
                               self.from_entity(entity="experience_years")],
                "phone_number": [self.from_entity(entity="phone_number", intent=["inform","apply_job"]),
                               self.from_entity(entity="phone_number")],
                "email": [self.from_entity(entity="email", intent=["inform","apply_job"]),
                               self.from_entity(entity="email")],
                "cv_link": [self.from_entity(entity="cv_link", intent=["inform","apply_job"]),
                               self.from_entity(entity="cv_link")]}


    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False



    def validate_experience_years(self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate experience years value."""

        if self.is_int(value) and int(value) > 0:
            return value
        else:
            dispatcher.utter_template('utter_wrong_experience_years', tracker)
            # validation failed, set slot to None
            return None

    @staticmethod
    def validate_email(value: Text,
                                 dispatcher: CollectingDispatcher,
                                 tracker: Tracker,
                                 domain: Dict[Text, Any]) -> Any:
            return value

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        """in other words from here the applicant data goes to the database"""    
        # utter submit template
        dispatcher.utter_template('utter_apply_submit', tracker)
        return []
