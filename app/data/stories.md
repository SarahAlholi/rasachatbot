## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## check marks
* greet
  - utter_greet
* check_marks
  - action_ask_id
* submitted_id
  - action_ask_password
* submitted_password
  - validate_marks
  - utter_goodbye

## check attendence
* greet
  - utter_greet
* check_attendance
  - action_ask_id
* submitted_id
  - action_ask_password
* submitted_password
  - validate_attendance
  - utter_goodbye

## upcoming holidays
* greet
  - utter_greet
* check_upcoming_holidays
  - upcoming_holidays
  - utter_goodbye

## admission status
* greet
  - utter_greet
* check_admission_status
  - action_admission_info
  - utter_goodbye