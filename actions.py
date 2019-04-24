from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionJob(Action):
    def name(self):
        return "action_job"
    def run(self, dispatcher, tracker, domain):
        job_title = tracker.get_slot('job_title')
        job_dept = "tracker.get_slot('job_titles')"
        if job_title:
            dispatcher.utter_message("based on job title search")
        else :
            dispatcher.utter_message("all jobs")
        return [SlotSet('job_title',job_title)]

class Actioncontact(Action):
    def name(self):
        return "action_contact"
    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message("hello")
        return []

class ActionInternship(Action):
    def name(self):
        return "action_internship"
    def run(self, dispatcher, tracker, domain):
        
        dispatcher.utter_message("hello")
        return []

class ActionLocation(Action):
    def name(self):
        return "action_location"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("hello")
        return []
