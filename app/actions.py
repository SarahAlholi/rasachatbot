# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/core/actions/#custom-actions/


# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from datetime import date
# from typing import Any, Text, Dict, List
# import sqlite3
# import pandas as pd

# class ActionMarks(Action):

#     def name(self) -> Text:
#         return "validate_marks"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
#             messages = []
#             for event in (list(tracker.events)):
#                 if event.get("event") == "user":
#                     messages.append(event.get("text"))
#             print("Messages : ",messages)


#             reg_no = messages[-2]
#             password = str((tracker.latest_message)['text'])
#             conn = sqlite3.connect('University.db')
#             query = "select * from Student_details where regno = '{0}' and password = '{1}'".format(reg_no,password)
#             print("Final query : ",query)
#             df = pd.read_sql(query, conn)
#             if df.shape[0] == 1:
#                 values = list(df.values)[0]
#                 name = values[0]
#                 subjects_col = ['sub1', 'sub2', 'sub3', 'sub4', 'lab1', 'lab2']
#                 marks_df = df[subjects_col]
#                 val_dict = (marks_df.to_dict('r'))[0]
#                 failed_subjects = ''
#                 total_marks = sum(list(val_dict.values()))
#                 content = "Below are the details " + name + "\n\n\n"

#                 for k, v in val_dict.items():
#                     if v < 25:
#                         failed_subjects = failed_subjects + k + ', '
#                     content = content + k + "  : " + str(v) + "\n"

#                 content = content + "Total : " + " : " + str(total_marks) + "\n"
#             else:
#                 content = "Sorry your credentials are incorrect. Please enter valid credentials next time"
#             dispatcher.utter_message(text=content)
#             return []