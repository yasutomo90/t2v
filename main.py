import discord
from get_token import discord_token
from create_voice import text_to_speech

def main(discord_token):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_message(message):
        print(message.content)
        text_to_speech(message.content)

    client.run(discord_token)

if __name__ == "__main__":
    main(discord_token())