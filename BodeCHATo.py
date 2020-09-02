from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging

logging.basicConfig(level=logging.CRITICAL)


chato = ChatBot('ChatoBode')


trainer = ListTrainer(chato)
trainer.train("./sabe.yml")
#trainer.export_for_training('./my_export.json')

with open("./sabe.txt") as f:
    conversation = f.readlines()
    #chato.set_trainer(ListTrainer)
    #chato.trainer(conversation)

while True:
    try:
        user_input = input('User: ')    	

        bot_response = chato.get_response(user_input)


        print ('BodeCHATo: ', bot_response)
        
           
    except (KeyboardInterrupt, SystemExit):
    	break
    	
    	
