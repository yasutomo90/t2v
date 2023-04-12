import os
from dotenv import load_dotenv

def discord_token():
    try:
        token = os.environ["discord_token"]
    except:
        load_dotenv('.env') 
        token = os.getenv("discord_token")
        if not token:

            #discord_tokenの入力を求める
            print('input your discord api key')
            token = input()

            # .envファイルにAPIキーを保存する
            with open('.env', 'a') as f:
                f.write(f"discord_token={token}\n")

    return token

# discord_token()