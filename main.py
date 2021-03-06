#Imports
import discord
from discord.ext import commands
import jeux
import asyncio
import configparser

#Config file
config = configparser.ConfigParser()
config.read('config.ini')
bot_key = config.get("Bot", "key") #bot's key
pcmd = config.get("Bot", "Command_Prefix") #command s'Prefix

#bot client
Client = commands.Bot(command_prefix=pcmd) 
Client.remove_command('help')

@Client.event
async def on_ready():
    print("Starting Bot!")
    print("Bot Id = " + Client.user.id)

@Client.command()
async def ping():
    await Client.say("Pong!")

@Client.command()
async def help():
    await Client.say("Bot en Construction!")

Client.run(bot_key)
