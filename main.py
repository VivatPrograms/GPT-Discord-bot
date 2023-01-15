import openai, nextcord
from nextcord import Interaction
from keys import *

openai.api_key = openai_api_key
intentss = nextcord.Intents.default()
intentss.message_content = True
client = nextcord.Client(intents=intentss)
serverID = 773165389244268565

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.slash_command(name='ask',description='Ask a very simple question',guild_ids=[serverID])
async def test_command(interaction:Interaction, question:str):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{question}"),
        max_tokens=512,
        stop=None,
        temperature=0.5)

    embed = nextcord.Embed(title="OpenAI", description="If it doesn't respond :\n  *The answer is too demanding", color=0x5865f2)
    embed.add_field(name='User text', value=question, inline=False)
    embed.add_field(name='OpenAI text', value=response["choices"][0]["text"], inline=False)
    await interaction.response.send_message(embed=embed)

client.run(bot_token)