import PySimpleGUI as sg
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging
import random
import time


# animação do bode {pyglet}
image_bode = "BodeCHATo.gif"


logging.basicConfig(level=logging.CRITICAL)
## TREINAMENTO
chato = ChatBot('ChatoBode', database_uri='sqlite:///database.db')


trainer = ListTrainer(chato)
trainer.train("./sabe.yml")
# trainer.export_for_training('./my_export.json')

with open("./sabe.yml") as f:
    lines = f.readlines()

## FIM DO TREINAMENTO

def show_about():
    sg.popup('Sobre','Um programa em Python utilizando PySimpleGUI!', 
	      '          Gleriston Sampaio',
	      '               2020')


sg.change_look_and_feel('SystemDefault')


menu_def = [
    [
        "Arquivo",
        [
            "Abrir Texto",
            "Fechar",
            "---",
            "Preferências...",
            "---",
            "Sair",
        ],
    ],
    ["Editar", ["Voltar", "---", "Recortar", "Copiar", "Colar", "Deletar", "Selecionar Tudo",]],
    ["Ajuda", ["Sobre..."]],
]

layout = [
            [sg.Menu(menu_def, tearoff=False)],              
            [sg.Text('Diz ai o que tu quer?', size=(40, 1))],
            [sg.Image(filename=image_bode)],
            [sg.MLine(size=(30, 5), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('Mandar', button_color=(
               sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
           sg.Button('Se Mandar', button_color=(sg.YELLOWS[0], sg.GREENS[0]))
           ],
            [sg.Output(size=(110, 30), font=('Helvetica 10'))]
          ]

window = sg.Window('ChatoBode', layout, font=('Helvetica', ' 13'), default_button_element_size=(8, 2), size=(800,600))




while True:   
    event, values = window.read()
    if event in ('Se Mandar', None):           
        break
        
    if event == "Sobre...":
        show_about()    

    if event == 'Mandar':
        query = values['-QUERY-'].rstrip()
        bot_response = chato.get_response(query)
        # executa a resposta
        print('\nVocê: ', query)
        print('\nBodeCHATo: ', bot_response)
        #tempo de espera e ele faz uma pergunta aleatória
        time.sleep(5)
        print('\nBodeCHATo: ', random.choice(lines))
     
     
     
