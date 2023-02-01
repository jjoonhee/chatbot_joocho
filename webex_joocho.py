from webex_bot.webex_bot import WebexBot
import os
from translate import Translate
from GPT import GPT


webex_token = os.environ["WEBEX_TOKEN"]
bot = WebexBot(webex_token, approved_domains = ["cisco.com"])
bot.add_command(Translate())
bot.add_command(GPT())
bot.run()
