import os
import discord
import asyncio
from keep_alive import keep_alive
from discord.ext import commands
from background_tasks import bg_tasks
bot = commands.Bot(
	command_prefix='?',
	case_insensitive=True
)


# regex to find all print statements \n\s*print\([^()]*\)
class initialized:
	def __init__(self):
		self.started = False

	def __call__(self):
		if not self.started:
			self.started = True
			return False
		else:
			return True


started = initialized()

extensions = [
	'Commands.dev_cmds',
	'Commands.data_tweaking',
	'Commands.moderation',
	'Moderation.main',
	'Commands.fun',
	'Commands.help',

]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)


@bot.event
async def on_ready():
	print("bot is ready")
		
			


bot.run(os.getenv("token"))
