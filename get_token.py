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