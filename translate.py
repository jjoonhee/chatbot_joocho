import os
import openai
from webex_bot.models.command import Command as cmd
import json
openai.api_key = "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"


with open("C:/Users/joocho/Desktop/dev/webex_bot/translate.json", "r") as card:
    INPUT_CARD = json.load(card)

class Translate(cmd):
    def __init__(self):
        super().__init__(
            command_keyword = "hey",
            card = INPUT_CARD,
            help_message= "hey --> Translate a message to Korean"
        )

    def pre_execute(self, message, attachment_actions, activity):
        return "working on it... pls wait"
    
    def execute(self, message, attachment_actions, activity):
        input_text = attachment_actions.inputs["input_text"]
        response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt = "translate the following in Korean\n\n" + input_text,
                    temperature=0.3,
                    max_tokens = 3500,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
        )             
        return response["choices"][0]["text"]