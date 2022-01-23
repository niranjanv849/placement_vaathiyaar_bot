from cgitb import text
from email.mime import image
from telegram import *
from telegram.ext import *
from telegram.ext import updater
from telegram.ext import dispatcher
from telegram.utils.helpers import mention_markdown
import random

bot = Bot("5068447006:AAFCEFlNF7pWK-AC-WAeUNgP4htoAr1EWB8")
updater=Updater("5068447006:AAFCEFlNF7pWK-AC-WAeUNgP4htoAr1EWB8",use_context=True)
dispatcher=updater.dispatcher

#BYTES_NOTES
def byts_notes(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="நம்ம கிட்ட\nகாடு இருந்தா எடுத்துகிறுவானுக\nரூவா இருந்தா புடிங்கிக்கிறுவானுக\nஆனா படிப்ப மட்டும்\nநம்ம கிட்ட இருந்து எடுத்துக்கவே\nமுடியாது சிதம்பரம்🙌\n\nPadichu Nalla vaa pa🥇\n📚🔗 https://bit.ly/BYTS_NOTES",
    )


start_value=CommandHandler('byts_notes',byts_notes)
dispatcher.add_handler(start_value)

#CODING_QUEST

questions=[
'🐣',
'🐥',
'🐤']
level=['Easy🥉','Medium🥈','Hard🥇']
def coding_quest(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="🚀 Here you go!👩‍💻\n\n📄 Question:\n\n🔍 "+random.choice(questions),
    )


start_value=CommandHandler('coding_quest',coding_quest)
dispatcher.add_handler(start_value)


#UPCOMING_COMPANIES

def upcoming_companies(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="⏳\tCompanies and Packages:\n------------------------------------------------------------\n🚀\t\t\tLowe's - 19.14 LPA\n🚀\t\t\tPaypal - 18.0 LPA\n🚀\t\t\tJuspay - 15.0 LPA \n🚀\t\t\tInformatica - 12.5 LPA\n🚀\t\t\tTiger Analytics - 8.5 LPA\n🚀\t\t\tThoughtworks - 8.3 LPA\n🚀\t\t\tZohocorp - 8.4 LPA\n🚀\t\t\tInfosys - 8.2 LPA\n🚀\t\t\tRently - 8.0 LPA\n🚀\t\t\tPresidio - 8.0 LPA\n🚀\t\t\tKaar Tech - 8.0 LPA\n🚀\t\t\tQuinbay - 7.5 LPA\n🚀\t\t\tSoliton - 6.0 LPA\n🚀\t\t\tTemenos - 6.0 LPA\n⏳\t\t\tOdessa - 6.0 LPA\n------------------------------------------------------------\n⏳Ongoing\t\t\t✅Visited\t\t\t🚀Yet to come",   
        )


start_value=CommandHandler('upcoming_companies',upcoming_companies)
dispatcher.add_handler(start_value)

#CONTESTS_UPDATES

def contests_updates(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="⚠The Data provided below may not be accurate\n⚠And it is recommended to follow instructions \n🏳given by Training & Placement Team.\n🤖This bot gives only summary about updates and\n🌊You can use this as just a remainder which comes handy🙏"
        )
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="👩‍💻Ongoing Contests | Basic Details:\n---------------------------------------------------------\n\n🔍\t\t\tContest:  InfyTQ 2022 - 8 LPA\n\n🔗\t\t\tRegistration: closed🔒 \n\n📅\t\t\tContest Date: Feb 6,7,8",
        )
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="👩‍💻Ongoing Contests | Basic Details:\n---------------------------------------------------------\n\n🔍\t\t\tContest:  HackWithInfy 2022\n\n🔗\t\t\tRegistration: closed🔒 \n\n📅\t\t\tContest Date: Feb 6,7,8",
        )
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="👩‍💻Ongoing Contests | Basic Details:\n---------------------------------------------------------\n\n🔍\t\t\tContest:  Goldman Sachs - 20 LPA\n\n🔗\t\t\tRegistration: closed🔒 \n\n📅\t\t\tAptitude Test Date: Ended on Jan 16th 4:00pm ⏱\n\nCandidates waiting for results⏳",
        )


start_value=CommandHandler('contests_updates',contests_updates)
dispatcher.add_handler(start_value)

#Luck epudinu papom
def luck(update:Update,context:CallbackContext):
    bot.send_dice(
        chat_id=update.effective_chat.id,
        emoji="🎰",
    )


start_value=CommandHandler('luck',luck)
dispatcher.add_handler(start_value)


#start
def anon(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Things I can do 🎉:\n\n/byts_notes - BYTS Training written notes 📚\n\n/coding_quest - practice programming 💻\n\n/upcoming_companies - Latest updates from T & P cell ✅\n\n/contests_updates - Pending & ongoing contests 🎖\n\n/luck - Check your Luck Today 💎",
    )


start_value=CommandHandler('start',anon)
dispatcher.add_handler(start_value)


#dont touch
updater.start_polling()     