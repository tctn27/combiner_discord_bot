import random
import time
import discord
from discord.ext import commands

TOKEN = "NTg1MDUwNjU0MzMwODQ3MjMy.XPpY8w.3JQ7QwlJhLTFjzXH_LyFX3Qmmrc"

client = commands.Bot(command_prefix="~")

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
        try:
            if message.content == "e" or message.content == "E":
                await message.channel.send("https://i.kym-cdn.com/entries/icons/original/000/026/008/Screen_Shot_2018-04-25_at_12.24.22_PM.png")
            else:
                words = give_eligible_words(message)
                if len(message.content.split(" ")) == 2 and len(words) > 0:
                    set_of_two = words[random.randint(0, len(words) - 1)]
                    combined = combine(set_of_two[0], set_of_two[1])
                    print(combined)
                    await message.channel.send("*" + combined + "*")
                elif len(words) > 0 and random.randint(0, 0) == 0:
                    set_of_two = words[random.randint(0, len(words) - 1)]
                    combined = combine(set_of_two[0], set_of_two[1])
                    print(combined)
                    await message.channel.send("*" + combined + "*")
        except ValueError as e:
            with open("logs/" + str(time.time()) + ".log", "w+") as f:
                f.write(str(time.time()) + "\n")
                f.write(str(e))
            await message.channel.send("<@227336569881624576> <@191357391453945856> error")

client.run(TOKEN)
