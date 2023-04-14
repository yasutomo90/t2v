import discord
from create_voice import text_to_speech
import os
from dotenv import load_dotenv

def discord_token():
    try:
        discord_token = os.environ["discord_token"]
    except:
        load_dotenv('.env') 
        discord_token = os.getenv("discord_token")
        if not discord_token:

            #discord_tokenの入力を求める
            print('input your discord api key')
            discord_token = input()

            # .envファイルにAPIキーを保存する
            with open('.env', 'a') as f:
                f.write(f"discord_token={discord_token}\n")

    return discord_token

def discord_run():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.eventpy
    async def on_message(message):
        print(message.content)
        text_to_speech(message.content)

    client.run(discord_token())
