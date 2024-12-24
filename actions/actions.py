# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionComoFuncionaAuxilio(Action):
    def name(self) -> str:
        return "action_como_funciona_auxilio"

    def run(self, dispatcher, tracker, domain):
        # Recuperando o valor do slot 'auxilio-bolsa'
        print("to akiiii")
        auxilio = tracker.get_slot("auxilio-bolsa")
        
        # Lógica para determinar qual resposta usar com base no valor do slot
        if auxilio == "PIBIC":
            dispatcher.utter_template("utter_como_funciona_pibic", tracker)
        elif auxilio == "PIBIT":
            dispatcher.utter_template("utter_como_funciona_pibit", tracker)
        elif auxilio == "PID":
            dispatcher.utter_template("utter_como_funciona_pid", tracker)
        elif auxilio == "BIA":
            dispatcher.utter_template("utter_como_funciona_bia", tracker)
        elif auxilio == "emergencial":
            dispatcher.utter_template("utter_como_funciona_aux_emergencial", tracker)
        elif auxilio == "creche":
            dispatcher.utter_template("utter_como_funciona_aux_creche", tracker)
        elif auxilio == "moradia":
            dispatcher.utter_template("utter_como_funciona_aux_moradia", tracker)
        else:
            dispatcher.utter_message(text="Desculpe, não reconheci o tipo de bolsa ou auxílio. Pode me dar mais informações?")
        
        return []