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

## about time
* greet
  - utter_greet
* give_time
  - action_show_time

## User wants to check upcoming holidays
* greet
  - utter_greet
* user_wants_to_check_upcoming_holidays
  - display_upcoming_holidays
  - utter_goodbye

## User wants to check admission status
* greet
  - utter_greet
* check_admission_status
  - user_wants_to_check_admission_status
  - action_admission_info
  - utter_goodbye