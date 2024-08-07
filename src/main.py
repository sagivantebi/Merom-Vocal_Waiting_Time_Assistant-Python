import time
from pprint import pprint
import openai
from config import API_KEY
from protocols.py import loop_prompt

openai.api_key = API_KEY

if __name__ == '__main__':
    api_prompt = ".".join(loop_prompt)

    Uncomment and adjust the following lines if you want to play audio
    instance = vlc.Instance('--no-xlib')
    media = instance.media_new('Audio/Merom.mp3')
    duration = media.get_duration()
    duration_seconds = duration / 1000
    player = vlc.MediaPlayer("Audio/Merom.mp3")
    player.play()
    time.sleep(duration_seconds + 0.01)
    player.stop()

    while True:
        # Make API call to OpenAI
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=api_prompt,
            temperature=0,
            max_tokens=1200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.3,
            stop=["$$$"]
        )

        # Print the response
        pprint(response)
