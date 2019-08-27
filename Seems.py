import discord
import random
import re

with open("seems_token", "r") as file:
    TOKEN = file.read()

client = discord.Client()

def only_letters(message):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    message = message.lower()
    for letter in message:
        if letter not in letters:
            return False
    return True

def uncombine(word):
    return 'willy love'

def roller(dice):
    rolls = []
    sum = 0
    number = int(dice.split('d')[0])
    type = int(dice.split('d')[1])
    for i in range(0, number):
        roll = random.randint(1, type)
        rolls.append(str(roll))
        sum += roll
    return str(rolls).replace("'", "") + str(sum)

#return str(rolls).replace("'", "") + '\nTotal: ' + str(sum)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.author.id == "585050654330847232":
        if only_letters(message.content):
            uncombine(message.content)
        msg = random.choice(['Fuck you {0.author.mention}', 'I love you {0.author.mention}',
                            'Why do you never put the dishes away {0.author.mention}?',
                            'You\'re the sweetest {0.author.mention}',
                            '{0.author.mention} please, we\'ve talked about this']).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!roll'):
        totsum = 0
        msg = ""
        cleanstr = message.content.replace('!roll', '')
        cleanstr = cleanstr.replace(' ', '')
        messlist = filter(None, re.split("[^+^-]", cleanstr))
        print(messlist)
        #try:
        for sec in messlist:
            print(sec)
            '''if 'd' in sec:
                rolls = []
                sum = 0
                number = int(sec.split('d')[0])
                type = int(sec.split('d')[1])
                for i in range(0, number):
                    roll = random.randint(1, type)
                    rolls.append(str(roll))
                    sum += roll
                msg += str(rolls).replace("'", "")
                totsum += sum
            else:
                msg += str(sec)
                totsum += int(sec)'''
        msg += '\nTotal: ' + str(totsum)
        '''except (ValueError):
            msg = "You dumb fucking cretin, you fucking fool \nabsolute fucking buffoon, " \
                  "you bumbling idiot, dice don't work like that! Fuck you."
        except :
            msg = "Too much power! Try something more manageable"'''
        await client.send_message(message.channel, msg)

    if message.content.startswith('*test*'):
        print(message.author.id)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
