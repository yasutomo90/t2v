import requests
import json
import time
import re
import simpleaudio

def audio_query(text, speaker, max_retry):
    # 音声合成用のクエリを作成する
    query_payload = {"text": text, "speaker": speaker}
    for query_i in range(max_retry):
        r = requests.post("http://127.0.0.1:50021/audio_query", 
                        params=query_payload, timeout=(10.0, 300.0))
        if r.status_code == 200:
            query_data = r.json()
            break
        time.sleep(1)
    else:
        raise ConnectionError("リトライ回数が上限に到達しました。 audio_query : ", "/", text[:30], r.text)
    return query_data
def synthesis(speaker, query_data,max_retry):
    synth_payload = {"speaker": speaker}
    for synth_i in range(max_retry):
        r = requests.post("http://127.0.0.1:50021/synthesis", params=synth_payload, 
                          data=json.dumps(query_data), timeout=(10.0, 300.0))
        if r.status_code == 200:
            #音声ファイルを返す
            return r.content
        time.sleep(1)
    else:
        raise ConnectionError("音声エラー：リトライ回数が上限に到達しました。 synthesis : ", r)


def text_to_speech(texts, speaker=8, max_retry=20):
    #voicevoxへ音声合成クエリを送信し、音声を再生する。
    if texts==False:
        texts="ちょっと、通信状態悪いかも？"
    texts=re.split("(?<=！|。|？)",texts)
    play_obj=None
    for text in texts:
        # audio_query
        query_data = audio_query(text,speaker,max_retry)
        # synthesis
        voice_data=synthesis(speaker,query_data,max_retry)
        #音声の再生
        if play_obj != None and play_obj.is_playing():
            play_obj.wait_done()
        wave_obj=simpleaudio.WaveObject(voice_data,1,2,24000)
        play_obj=wave_obj.play()