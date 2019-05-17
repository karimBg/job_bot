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

## Generated Story 8362015419805915240
* inform_internship
    - action_internship

## Generated Story 8362015419805915240
* inform_internship
    - action_internship
    - internship_form
    - form{"name": "internship_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform_internship{"internshipRef": "Ref-12188"}
    - slot{"internshipRef": "Ref-12188"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}

## apply happy path
* greet
    - utter_greet
* apply_job
    - apply_form
    - form{"name": "apply_form"}
    - form{"name": null}
    - utter_apply_slots_values
* thankyou
    - utter_noworries

## Generated Story 4928413376213491340
* apply_job
    - apply_form
    - form{"name": "apply_form"}
    - slot{"requested_slot": "jobRef"}
* form: inform_apply{"jobRef": "job-54212"}
    - slot{"jobRef": "job-54212"}
    - form: apply_form
    - slot{"jobRef": "job-54212"}
    - slot{"requested_slot": "name"}
* form: inform_apply{"name": "Mohamed Karim"}
    - slot{"name": "Mohamed Karim"}
    - form: apply_form
    - slot{"name": "Mohamed Karim"}
    - slot{"requested_slot": "experience_years"}
* form: inform_apply{"experience_years": "2"}
    - slot{"experience_years": "2"}
    - form: apply_form
    - slot{"experience_years": "2"}
    - slot{"requested_slot": "phone_number"}
* form: inform_apply{"phone_number": "50730571"}
    - slot{"phone_number": "50730571"}
    - form: apply_form
    - slot{"phone_number": "50730571"}
    - slot{"requested_slot": "email"}
* form: inform_apply{"email": "islem@email.com"}
    - slot{"email": "islem@email.com"}
    - form: apply_form
    - slot{"email": "islem@email.com"}
    - slot{"requested_slot": "cv_link"}
* inform_apply{"cv_link": "https://www.linkedin.com/in/islem-mezghani-1a4369144/"}
    - slot{"cv_link": "https://www.linkedin.com/in/islem-mezghani-1a4369144/"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}

## apply job stop and really stop path
* greet
    - utter_greet
* apply_job
    - apply_form
    - form{"name": "apply_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## apply job stop but continue path
* apply_job
    - apply_form
    - form{"name": "apply_form"}
* stop
    - utter_ask_continue
* affirm
    - apply_form
    - form{"name": null}
    - utter_apply_slots_values
* thankyou
    - utter_noworries