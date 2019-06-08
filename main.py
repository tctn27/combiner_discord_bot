import random
import time
import email_devs
import discord
from discord.ext import commands

with open("token", "r") as f:
    TOKEN = f.read()

client = commands.Bot(command_prefix="~")

whitelist = []
with open("whitelist", "r+") as f:
    for i in f:
        whitelist.append(int(i))

blacklist = []
with open("blacklist", "r+") as f:
    for i in f:
        blacklist.append(int(i))

def combine(first_word, second_word):
    vowels = ["a", "e", "i", "o", "u"]
    out_word = ""

    first = True
    for i in first_word:
        if first:
            out_word += i
            first = False
        else:
            if i not in vowels:
                out_word += i
            else:
                break

    i = -1
    for l in second_word:
        i += 1
        if l in vowels:
            out_word += second_word[i:]
            return out_word

    return out_word

def give_eligible_words(sentence):
    words = sentence.content.lower().split(" ")
    long = 2
    eligible_words = []
    was_long = False
    buffer = ""

    for i in words:
        if len(i) >= long and was_long:
            eligible_words.append([buffer, i])
            buffer = i
        elif len(i) >= long:
            buffer = i
            was_long = True
        else:
            was_long = False

    return eligible_words

@client.event
async def on_ready():
    print("Bot online")

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.channel not in blacklist:
            try:
                if "modok" in message.content or "MODOK" in message.content or "M.O.D.O.K." in message.content:
                    await message.channel.send("https://vignette.wikia.nocookie.net/assistme/images/9/92/Modok.png/revision/latest?cb=20120710014024")
                if message.content == "e" or message.content == "E":
                    await message.channel.send("https://i.kym-cdn.com/entries/icons/original/000/026/008/Screen_Shot_2018-04-25_at_12.24.22_PM.png")
                if "modok" in message.content or "MODOK" in message.content or "M.O.D.O.K." in message.content:
                    await message.channel.send("https://vignette.wikia.nocookie.net/assistme/images/9/92/Modok.png/revision/latest?cb=20120710014024")
                else:
                    words = give_eligible_words(message)
                    if len(words) > 0 and message.channel in whitelist:
                        set_of_two = words[random.randint(0, len(words) - 1)]
                        combined = combine(set_of_two[0], set_of_two[1])
                        print(combined)
                        await message.channel.send("*" + combined + "*")
                    elif len(message.content.split(" ")) == 2 and len(words) > 0:
                        set_of_two = words[random.randint(0, len(words) - 1)]
                        combined = combine(set_of_two[0], set_of_two[1])
                        print(combined)
                        await message.channel.send("*" + combined + "*")
                    elif len(words) > 0 and random.randint(0, 10) == 0:
                        set_of_two = words[random.randint(0, len(words) - 1)]
                        combined = combine(set_of_two[0], set_of_two[1])
                        print(combined)
                        await message.channel.send("*" + combined + "*")
            except ValueError as e:
                with open("logs/" + str(time.time()) + ".log", "w+") as f:
                    f.write(str(time.time()) + "\n")
                    f.write(str(e))
                email_devs.error_email(e)
                await message.channel.send("<@227336569881624576> <@191357391453945856> error")

client.run(TOKEN)
