import telebot
import sys
import os

try:
  
  chat_id = int(sys.argv[1])
  file = str(chat_id)+'.png'
  bot = telebot.TeleBot("7752565239:AAHH1b1Y_1fsYaYBxZicO59G3PNZWPiYhTA)
  img = open(file, 'rb')
  bot.send_photo(chat_id, img)
  os.remove(file)

except:
  pass
