# https://t.me/dictionary_Ircha_bot
# @dictionary_Ircha_bot

# Telegram Bot Documentation: https://core.telegram.org/bots
# API Documentation: https://core.telegram.org/bots/api

# (from telegram.ext) showed an Error due to Package version.

# Terminal:
# >>> pip install python-telegram-bot
# >>> /Users.../TelegramBot2/bin/python -m pip install --upgrade pip

# >>> pip install requests
# >>> pip install lxml
# >>> pip install bs4


# Telegram-bot Library:
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
# Web-scraping Libraries:
import requests
import bs4


with open("token.txt", "r") as f:
    TOKEN = f.read()

updater = Updater(TOKEN, use_context=True)



def start(update, context):
    update.message.reply_text("Hi, welcome. Please write /help to see the commands available.")


def help(update, context):
    update.message.reply_text("""
    Write /whatIs command followed by a word, to receive a translation.
    """)



def what_is(update, context):

    update.message.reply_text("You wrote '%s'" % update.message.text)

    user_input = update.message.text
    no_command_text = user_input[8::]
    no_spaces_on_sides = no_command_text.strip()
    lower_case = no_spaces_on_sides.lower()
    print(lower_case)

    #Serch Urban:
    urban_seach(lower_case)


    # Reply
    #update.message.reply_to_message(""" UrbanDictionary: """)



def urban_seach(lower_case2):
    urb_search = requests.get(f"https://www.urbandictionary.com/define.php?term={lower_case2}")
    urban_soup = bs4.BeautifulSoup(urb_search.text, "lxml") #lxml is a parsing engine
    first_item = urban_soup.select(".break-words meaning mb-4")[0]

    print(first_item.text)








def youtube_url(update, context):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/")




def unknown(update, context):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update, context):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def main():
#Command Harndlers:
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('whatIs', what_is))

    updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))


# Filters out unknown commands:
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
# Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    updater.start_polling()


if __name__ == '__main__':
    main()