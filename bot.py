import discord

TOKEN = "///////////"

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("=Hola"):
		msg = "Holis {0.author.mention}".format(message)
		await message.channel.send(msg)

	if message.content.startswith("=hola"):
		msg = "Holis {0.author.mention}".format(message)
		await message.channel.send(msg)

	if message.content.startswith("=musica"):
		id = "<@234395307759108106>"
		diosmsg = "Lo siento, %s maneja la musica OwO" % id
		await message.channel.send(diosmsg)

@client.event
async def on_ready():
	print("Loggeado como:")
	print(client.user.name)
	print(client.user.id)
	print("------")

client.run(TOKEN)
