## story 01
* acquaintance
    - action_acquaintance

## story 02
* greet
    - utter_greet

## story 03
* how_are_you
    - utter_how_are_you

## story 04 
* nice_to_meet_you
    - utter_nice_to_meet_you

# story 08
* inform_contact
    - action_contact

## story 09 
* goodbye
    - utter_goodbye
    
## Generated Story -973804493632658673
* inform_job
    - action_job
    - jobs_form
    - form{"name": "jobs_form"}
    - slot{"job_title": "web designer"}
    - slot{"requested_slot": "job_title"}
    - utter_ask_detail
* ask_detail{"JobOptions": "description"}
    - slot{"JobOptions": "description"}
    - action_show_details
    - action_deactivate_form
    - slot{"job_title": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -973804493632658672
* inform_job
    - action_job
    - jobs_form
    - form{"name": "jobs_form"}
    - slot{"job_title": "web designer"}
    - slot{"requested_slot": "job_title"}
    - utter_ask_detail
* ask_detail{"JobOptions": "description"}
    - slot{"JobOptions": "description"}
    - action_show_details
    - action_deactivate_form
    - slot{"job_title": null}
    - form{"name": null}
    - slot{"requested_slot": null}

#story 88
* ask_detail{"JobOptions": "mission"}
    - slot{"JobOptions": "mission"}
    - action_show_details

#story 8522
* acquaintance
    - action_acquaintance