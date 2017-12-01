from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import logging

# Habilitar o registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER, PHOTO, NAME, BIO = range(4)



def start(bot, update):
    reply_keyboard = [['Homem', 'Mulher']]

    update.message.reply_text(
        'Olá aventureiro, eu serei seu mestre nessa jornada!'
        '\n'
        'Você é Homem ou Mulher?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER

def gender(bot, update):
    user = update.message.from_user
    global sexo
    global g
    global ga
    sexo = update.message.text
    if sexo == "Homem":
        update.message.reply_text('hmmm... Você com certeza deve ser um homem corajoso!')
        g = 'o'
        ga=''
        
    elif sexo == "Mulher":
        update.message.reply_text('Claramente uma delicada moça!')
        g = 'a'
        ga = 'a' 
        
    logger.info("Genero do %s: %s" % (user.first_name, update.message.text))
    update.message.reply_text('Agora deixe-me ver como você se aparenta... '
                              '\nEnvie-me uma boa foto sua, ou envie /skip se você for um troll melequento e não quiser ser visto.',
                              reply_markup=ReplyKeyboardRemove())

    return PHOTO

def name(bot, update):
    user = update.message.from_user
    logger.info("Bio do %s: %s" % (user.first_name, update.message.text))
    global nome
    nome = update.message.text
    if sexo == "Homem":
        update.message.reply_text('Seu nome é ' + nome + '? É com certeza um nome imponente, digno de um bravo heroi!')
        
    elif sexo == "Mulher":
        update.message.reply_text('Seu nome é ' + nome + '? Um belo nome para uma bela dama!')
    
    reply_keyboard = [['Guerreiro', 'Arqueiro', 'Mago']]
    user = update.message.from_user
    logger.info("Bio do %s: %s" % (user.first_name, update.message.text))
    update.message.reply_text('Agora irei explicar-lhe como essa aventura funcionará:'
                             '\nVocê poderá escolher entre três classes: Guerreiro, Arqueiro e Mago, cada um deles tem seus prós e contras, escolha sabiamente:',
    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    return BIO

    


def photo(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('user_photo.jpg')
    logger.info("Foto do %s: %s" % (user.first_name, 'user_photo.jpg'))
    update.message.reply_text('Este é você? ...ok! Agora diga-me seu nome.')

    return NAME


def skip_photo(bot, update):
    user = update.message.from_user
    logger.info("Usuário %s não enviou a foto." % user.first_name)
    if sexo == "Homem":
        update.message.reply_text('Não quer ser vist' + g  + ' certo? ok... '
                              'pelo menos eu posso saber seu nome, misterioso aventureiro?')
        
    elif sexo == "Mulher":
        update.message.reply_text('Não quer ser vist' + g + ' certo? ok... '
                              'pelo menos eu posso saber o nome desta misteriosa dama?')
    

    return NAME


def bio(bot, update):
    global forca
    global dex
    global inteli
    global vit
    global agi
    global classe
    global atri

    classe = update.message.text
    if (classe == "Guerreiro"):
        update.message.reply_text('Vi em sua postura o furor de um' + ga + ' poderoso Guerreir' + g + ' !')
        forca  = 3
        dex = 2
        inteli = 1
        vit = 3
        agi = 1
        update.message.reply_text('Agora deixe-me explicar como as classes funcionam, exixtem 5 atribulos base para todas as classes: Força, Destreza, Inteligencia, Vitalidade e Agilidade.')
        update.message.reply_text('Força é o que ira definir seus pontos de ataque e defesa em combates, atributo essencial para Guerreiros.')
        update.message.reply_text('Destreza é o que define sua mira, pericia com armas e habilidades, atributo essencial para Arqueiros e Magos.')
        update.message.reply_text('Inteligencia é o que define seu dano magico com habilidades e seus pontos de mana, atributo essencial para Magos e recomendavel para Arqueiros.')
        update.message.reply_text('Vitalidade é o que define seus pontos de vida, atributo essencial para Guerreiros')
        update.message.reply_text('Agilidade é o que define quem fara a primeira ação no turno, atributo essencial para Arqueiros.')
        update.message.reply_text('Eu mesmo destribui seus pontos com base na classe que escolheu, você pode ve-los e progredi-los a qualquer momento digitando: </status> ')
        
    if (classe == "Arqueiro"):
        update.message.reply_text('Vi em suas mãos a habilidade de um' + ga + ' preciso Arquei' + g + ' !')
        forca  = 1
        dex = 3
        inteli = 2
        vit = 1
        agi = 3
        update.message.reply_text('Agora deixe-me explicar como as classes funcionam, exixtem 5 atribulos base para todas as classes: Força, Destreza, Inteligencia, Vitalidade e Agilidade.')
        update.message.reply_text('Força é o que ira definir seus pontos de ataque e defesa em combates, atributo essencial para Guerreiros.')
        update.message.reply_text('Destreza é o que define sua mira, pericia com armas e habilidades, atributo essencial para Arqueiros e Magos.')
        update.message.reply_text('Inteligencia é o que define seu dano magico com habilidades e seus pontos de mana, atributo essencial para Magos e recomendavel para Arqueiros.')
        update.message.reply_text('Vitalidade é o que define seus pontos de vida, atributo essencial para Guerreiros')
        update.message.reply_text('Agilidade é o que define quem fara a primeira ação no turno, atributo essencial para Arqueiros.')
        update.message.reply_text('Eu mesmo destribui seus pontos com base na classe que escolheu, você pode ve-los e progredi-los a qualquer momento digitando: </status> ')
        
    if (classe == "Mago"):
        update.message.reply_text('Vi em suas mãos a habilidade de um' + ga + ' experiente Mag' + g + ' !')
        forca  = 1
        dex = 3
        inteli = 3
        vit = 1
        agi = 2
        update.message.reply_text('Agora deixe-me explicar como as classes funcionam, exixtem 5 atribulos base para todas as classes: Força, Destreza, Inteligencia, Vitalidade e Agilidade.')
        update.message.reply_text('Força é o que ira definir seus pontos de ataque e defesa em combates, atributo essencial para Guerreiros.')
        update.message.reply_text('Destreza é o que define sua mira, pericia com armas e habilidades, atributo essencial para Arqueiros e Magos.')
        update.message.reply_text('Inteligencia é o que define seu dano magico com habilidades e seus pontos de mana, atributo essencial para Magos e recomendavel para Arqueiros.')
        update.message.reply_text('Vitalidade é o que define seus pontos de vida, atributo essencial para Guerreiros')
        update.message.reply_text('Agilidade é o que define quem fara a primeira ação no turno, atributo essencial para Arqueiros.')
        update.message.reply_text('Eu mesmo destribui seus pontos com base na classe que escolheu, você pode ve-los e progredi-los a qualquer momento digitando: </status> ')

    return PHOTO

def status(bot, update):
    update.message.reply_text('Nome: ' + nome)
    update.message.reply_text('Sexo: ' + sexo)
    update.message.reply_text('Força: ' + str(forca))
    update.message.reply_text('Vitalidade: ' + str(vit))
    update.message.reply_text('Destresa: ' + str (dex))
    update.message.reply_text('Inteligencia: ' + str (inteli))
    update.message.reply_text('Agilidade: ' + str (agi))

def error(bot, update, error):
    logger.warn('Update "%s" erro causado por "%s"' % (update, error))


def main():
    # Cria o EventHandler e passa o token do seu bot.
    updater = Updater("478165831:AAFFDbgwIYleR_7nqtQQCK7nVOSkUWn7I2g")

    # Obter o dispatcher para registar os manipuladores
    dp = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [RegexHandler('^(Homem|Mulher)$', gender)],

            NAME: [MessageHandler(Filters.text, name)],

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],
            BIO: [MessageHandler(Filters.text, bio),
                  RegexHandler('^(Guerreiro|Arqueiro|Mago)$', bio)]

        },

        fallbacks=[CommandHandler('status', status)],
        
        
        
    )

    dp.add_handler(conv_handler)

    # Logar todos os erros
    dp.add_error_handler(error)

    # Inicia o Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
