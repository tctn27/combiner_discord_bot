import random
import discord
from discord.ext import commands

TOKEN = "NTg1MDUwNjU0MzMwODQ3MjMy.XPpMxw.bTNXJs9OrRBHTm8KwEl18uGevtk"

client = commands.Bot(command_prefix="~")

def combine(first_word, second_word):
    vowels = ["a", "e", "i", "o", "u"]
    out_word = ""

    for i in first_word:
        if i not in vowels:
            out_word += i
        else:
            break

    temp = ""
    first_consonants = True
    for i in second_word[::-1]:
        if first_consonants and i not in vowels:
            temp += i
        elif i in vowels:
            temp += i
            first_consonants = False
        else:
            out_word += temp[::-1]
            return out_word.lower()

def give_eligible_words(sentence):
    words = sentence.content.split(" ")
    long = 3
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
    words = give_eligible_words(message)
    if len(words) > 2 and random.randint(0, 0) == 0:
        set_of_two = words[random.randint(0, len(words) - 1)]
        combined = combine(set_of_two[0], set_of_two[1])
        print(combined)
        await message.channel.send(combined)

client.run(TOKEN)