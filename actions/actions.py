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

import re
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

class ActionHandleIdNumber(Action):
    def name(self) -> Text:
        return "action_handle_id_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получаем введенный ИИН из слота
        id_number = re.sub(r'\D', '', tracker.get_slot('id_number'))
        id_first_half = id_number[:6]

        id_second_half = id_number[6:]
        
        # Здесь можно добавить логику для обработки ИИН, например, сохранение в базу данных

        dispatcher.utter_message(text=f"Ваш ИИН {id_number} сохранен.")
        
        return []


# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionHandleIDNumber(Action):

#     def name(self) -> Text:
#         return "action_handle_id_number"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         id_number = tracker.get_slot('id_number')
        
#         if len(id_number) == 12 and id_number.isdigit():
#             first_half = id_number[:6]
#             second_half = id_number[6:]
            
#             # Устанавливаем слоты для первой и второй половин
#             return [
#                 {"event": "slot", "name": "id_first_half", "value": first_half},
#                 {"event": "slot", "name": "id_second_half", "value": second_half}
#             ]
#         else:
#             dispatcher.utter_message(text="ИИН должен состоять из 12 цифр. Пожалуйста, попробуйте снова.")
#             return []

# class ActionHandleFirstHalf(Action):

#     def name(self) -> Text:
#         return "action_handle_first_half"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         first_half = tracker.get_slot('id_first_half')
        
#         if first_half == "123456":  # Пример правильной первой половины
#             dispatcher.utter_message(text="Первая половина верна. Пожалуйста, укажите вторую половину.")
#         else:
#             dispatcher.utter_message(text="Первая половина неверна. Пожалуйста, попробуйте снова.")
        
#         return []

# class ActionHandleSecondHalf(Action):

#     def name(self) -> Text:
#         return "action_handle_second_half"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         second_half = tracker.get_slot('id_second_half')
        
#         if second_half == "123456":  # Пример правильной второй половины
#             dispatcher.utter_message(text="Вторая половина верна. Ваш ИИН подтвержден.")
#         else:
#             dispatcher.utter_message(text="Вторая половина неверна. Пожалуйста, попробуйте снова.")
        
#         return []
