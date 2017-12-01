import telebot
from telebot import types
import random
from random import randint

bot = telebot.TeleBot("478165831:AAFFDbgwIYleR_7nqtQQCK7nVOSkUWn7I2g")

class Objeto(object):
    pass

user = Objeto()
inimigo = Objeto()
dado = Objeto()

@bot.message_handler(commands=['start']) 
def start(message):
    user.id = message.from_user.id

    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btnHomem = types.KeyboardButton('Homem')
    btnMulher = types.KeyboardButton('Mulher')
    markup.add(btnHomem,btnMulher)
    bot.send_message (user.id,'''Olá aventureiro, eu serei seu mestre nessa jornada!
        \n
        Você é Homem ou Mulher?''', reply_markup=markup)
    bot.register_next_step_handler(message, gender)

def gender(message):
    global g
    global ga
    user.sexo = message.text
    if user.sexo == "Homem":
        bot.send_message(user.id, ' hmmm... Você com certeza deve ser um homem corajoso! ')
        g = 'o'
        ga=''
        
    elif user.sexo == "Mulher":
        bot.send_message(user.id,'Claramente uma delicada moça!')
        g = 'a'
        ga = 'a' 

    bot.send_message(user.id, '''Agora me diga o seu nome para podermos iniciarmos 
    a nossa aventura !!''')

    #logger.info("Genero do %s: %s" % (message.from_user.first_name, message.from_user.text)

    bot.register_next_step_handler(message, photo)

def photo (message):
    user.nick = message.text

    bot.send_message(user.id , '''Agora deixe-me ver como você se aparenta... 
    \nEnvie-me uma boa foto sua.''')


@bot.message_handler(content_types=['photo'])
def download(message):
    user.id_photo = message.photo[-1].file_id
    file_info = bot.get_file(user.id_photo)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    #logger.info("Foto do %s: %s" % (user.first_name, 'user_photo.jpg'))
    name(message)

def name(message):

    #logger.info("Bio do %s: %s" % (user.first_name, update.message.text))
    if user.sexo == "Homem":
        bot.send_message(user.id,'Seu nome é ' + user.nick + '? É com certeza um nome imponente, digno de um bravo heroi!')
        
    elif user.sexo == "Mulher":
        bot.send_message(user.id,'Seu nome é ' + user.nick + '? Um belo nome para uma bela dama!')
    #logger.info("Bio do %s: %s" % (user.first_name, update.message.text))
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btnGuerreiro = types.KeyboardButton('Guerreiro')
    btnArqueiro = types.KeyboardButton('Arqueiro')
    btnMago = types.KeyboardButton('Mago')
    markup.add(btnGuerreiro,btnArqueiro,btnMago)
    bot.send_message(user.id,'''Agora irei explicar-lhe como essa aventura funcionará:\n
                             \nVocê poderá escolher entre três classes: Guerreiro, Arqueiro e Mago, cada um deles tem seus prós e contras, escolha sabiamente:''', reply_markup=markup)
    bot.register_next_step_handler(message, atrib)

def atrib(message):
    user.classe = message.text
    
    if (user.classe == "Guerreiro"):
        bot.send_message(user.id,'Vi em sua postura o furor de um' + ga + ' poderoso Guerreir' + g + ' !')
        user.ataque  = 3
        user.defesa = 8
        user.vitalidade = 7
        user.vida = user.vitalidade*10
        user.agilidade = 1
        bot.send_message(user.id,'''Agora deixe-me explicar como as classes funcionam, exixtem 5 atribulos base para todas as classes: Força, Destreza, Inteligencia, Vitalidade e Agilidade.
        \nForça é o que ira definir seus pontos de ataque e defesa em combates, atributo essencial para Guerreiros.
        \nVitalidade é o que define seus pontos de vida, atributo essencial para Guerreiros.
        \nAgilidade é o que define quem fara a primeira ação no turno, atributo essencial para Arqueiros.
        \nEu mesmo destribui seus pontos com base na classe que escolheu.''')

    elif (user.classe == "Arqueiro"):
        bot.send_message(user.id,'Vi em suas mãos a habilidade de um' + ga + ' preciso Arqueir' + g + ' !')
        user.ataque = 5
        user.defesa = 5
        user.vitalidade = 5
        user.vida = user.vitalidade*10
        user.agilidade = 3
        bot.send_message(user.id,'''Agora deixe-me explicar como as classes funcionam, exixtem 5 atribulos base para todas as classes: Força, Destreza, Inteligencia, Vitalidade e Agilidade.
        \nForça é o que ira definir seus pontos de ataque e defesa em combates, atributo essencial para Guerreiros.
        \nVitalidade é o que define seus pontos de vida, atributo essencial para Guerreiros.
        \nAgilidade é o que define quem fara a primeira ação no turno, atributo essencial para Arqueiros.
        \nEu mesmo destribui seus pontos com base na classe que escolheu.''')

    elif (user.classe == "Mago"):
        bot.send_message(user.id, 'Vi em suas mãos a habilidade de um' + ga + ' experiente Mag' + g + ' !')
        user.ataque = 5
        user.defesa = 3
        user.vitalidade = 3
        user.vida = user.vitalidade*10
        user.agilidade = 2
        bot.send_message(user.id,'''Agora deixe-me explicar como as classes funcionam, exixtem 5 atribulos base para todas as classes: Força, Destreza, Inteligencia, Vitalidade e Agilidade.
        \nForça é o que ira definir seus pontos de ataque e defesa em combates, atributo essencial para Guerreiros.
        \nVitalidade é o que define seus pontos de vida, atributo essencial para Guerreiros.
        \nAgilidade é o que define quem fara a primeira ação no turno, atributo essencial para Arqueiros.
        \nEu mesmo destribui seus pontos com base na classe que escolheu.''')
    
    status(message)
 
def status(message):

    photo = open('C:\\Users\\kseve\\Desktop\\image.jpg')
    bot.send_photo(user.id, user.id_photo)
    bot.send_message(user.id ,
    'Nome: ' +user.nick + 
    '\nClasse: ' + user.classe + 
    '\nVida: ' +str(user.vida) +
    '\n********Atributos********' + 
    '\nAtaque: ' + str(user.ataque) + 
    '\nVitalidade: ' +str(user.vitalidade) + 
    '\nAgilidade: ' +str(user.agilidade))

    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btnComecar = types.KeyboardButton('Começar')
    markup.add(btnComecar)

    bot.send_message(user.id, "Clique no botão quando quiser iniciar a aventura.", reply_markup=markup)
    bot.register_next_step_handler(message, mensagem)

def mensagem(message):

    bot.send_message(user.id, '''## INICIANDO CAMPANHA ##\n\n\n\n\n\n''')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btnCurto = types.KeyboardButton('Caminho Curto')
    btnLongo = types.KeyboardButton('Caminho Longo')
    markup.add(btnCurto, btnLongo)

    bot.send_message(user.id, '''Você foi recrutado para uma expedição em busca de uma reliquia antiga,
    sua missão é vasculhar uma catacumba que fica além das montanhas de Nhor, além do vale frio.
    ''')

    bot.send_message(user.id, '''Para esta catabumba existem dois caminhos, o caminho mais longo e seguro,
    e o caminho por onde os mercadores levão seus bens, é mais curto... porém perigoso... por onde irá?''',reply_markup=markup)


    bot.register_next_step_handler(message, escolhas)

def escolhas (message):
    
    if(message.text == "Caminho Curto"):
        bot.send_message(user.id, '''Você optou pelo caminho mais curto, enquanto andava pela estrada avistou
        um mercador pedindo por socorro, ele parece estar sendo assaltado por badernistas ladinos. O mercador
        clama por ajuda e os ladinos te cercão.''')
        inimigo.nome = "Ladino"
        inimigo.ataque = 7
        inimigo.vida = 20
        inimigo.defesa = 3
        inimigo.agilidade = 6

    elif (message.text == "Caminho Longo"):
        bot.send_message(user.id, '''Você optou pelo caminho longo, demorou duas horas a mais para chegar ao
        vale frio e está se sentindo um pouco cansado. Ao chegar no vale frio você escuta susurros e uma nevoa
        fria lhe cerca, são espectros da nevoa, você terá que lutar!''')
        user.vida -= 10
        inimigo.nome = "Espectro"
        inimigo.ataque = 5
        inimigo.vida = 15
        inimigo.defesa = 10
        inimigo.agilidade = 3
    
    user.dado = randint(0,9)
    inimigo.dado = randint(0,9)
 
    bot.send_message(user.id, 'Rodaremos os dados do turno para saber quem ataca primero: Lá vai ... você tirou ' + str(user.dado))
    
    dado.user = int(user.agilidade + user.dado)
    dado.inimigo = int(inimigo.agilidade + inimigo.dado)

    bot.send_message(user.id, 'Seus pontos de agilidade somam:' + str(dado.user) + ' Seu inimigo tirou:' + str(dado.inimigo))

    user.turno = int(dado.user)
    inimigo.turno = int(dado.inimigo)

    
    if user.turno > inimigo.turno:
       bot.send_message(user.id, 'Você ataca primeiro! \nRode um dado para atacar!')
       user.dado = randint(0,9)
       dado.ataque_user = int(user.dado + user.ataque - inimigo.defesa)
       bot.send_message(user.id, 'Você tirou: ' + str(user.dado) + '! \nSeus pontos de ataque somam: ' + str(dado.ataque_user))
       inimigo.vida -= int(dado.ataque_user - inimigo.vida)

    elif inimigo.turno > user.turno:
        bot.send_message(user.id, inimigo.nome + ' ataca primeiro! \nEle rodará um dado para atacar!')
        inimigo.dado = randint(0,9)
        dado.ataque_inimigo = int(inimigo.dado + inimigo.ataque)
        bot.send_message(user.id, 'Tirou: ' + str(inimigo.dado) + '! \nSeus pontos de ataque somam: ' + str(dado.ataque_inimigo)) 
        user.vida = int(dado.ataque_inimigo - user.vida)
    
    batalha(message)


def batalha (message):
    while(user.vida > 0 or inimigo.vida > 0):
        user.dado = randint(0,9)
        inimigo.dado = randint(0,9)
        dado.user = int(user.agilidade + user.dado)
        dado.inimigo = int(inimigo.agilidade + inimigo.dado)
        bot.send_message(user.id, 'Rodaremos os dados do turno para saber quem ataca primero: Lá vai ... você tirou ' + str(user.dado))
        bot.send_message(user.id, 'Seus pontos de agilidade somam:' + str(dado.user) + ' Seu inimigo tirou:' + str(dado.inimigo))
        
        
        user.turno = int (user.agilidade + user.dado)
        inimigo.turno = int (inimigo.agilidade + inimigo.dado)

        if user.turno > inimigo.turno:
            bot.send_message(user.id, 'Você ataca primeiro! \nRode um dado para atacar!')
            user.dado = randint(0,9)
            dado.ataque_user = int(user.dado + user.ataque - inimigo.defesa)
            bot.send_message(user.id, 'Você tirou: ' + str(user.dado) + '! \nSeus pontos de ataque somam: ' + str(dado.ataque_user))
            inimigo.vida = int(dado.ataque_user - inimigo.vida)

        elif inimigo.turno > user.turno:
            bot.send_message(user.id, inimigo.nome + ' ataca primeiro! \nEle rodará um dado para atacar!')
            inimigo.dado = randint(0,9)
            dado.ataque_inimigo = int(inimigo.dado + inimigo.ataque)
            bot.send_message(user.id, 'Tirou: ' + str(inimigo.dado) + '! \nSeus pontos de ataque somam: ' + str(dado.ataque_inimigo))
            user.vida = int(dado.ataque_inimigo - user.vida)
        bot.send_message(user.id, str(user.vida) + "\n" + str(inimigo.vida))

        if inimigo.vida <= 0:
            bot.send_message(user.id, "Você matou o inimigo !!!")
            status(message)
            break
        elif user.vida <= 0:
            bot.send_message(user.id, "Você PERDEU!!!")
            break
bot.stop_polling()

bot.polling()
