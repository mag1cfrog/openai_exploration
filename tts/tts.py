import os
from pathlib import Path
from openai import OpenAI
client = OpenAI()

# check if audio directory exists
audio_dir = Path(__file__).parent / 'audio'
if not os.path.exists(audio_dir):
    os.makedirs(audio_dir)


# create_speech function
def create_speech(filename: str, text: str, voice: str = "onyx", model: str = "tts-1", voice_file_format: str = "mp3"):
    filename = filename + f'_{model}' + f'_{voice}' + f'.{voice_file_format}'
    speech_file_path = Path(__file__).parent / 'audio' / filename
    response = client.audio.speech.create(
    model=model,
    voice=voice,
    input=text
    )

    response.stream_to_file(speech_file_path)


def main():
    # create speech
    create_speech(
      "test_speech", 
      "Hello, my name is OpenAI's text to speech API. I'm excited to talk to you today.",
      model="tts-1-hd"
    )


if __name__ == "__main__":
    main()