import io
import os

# Imports the Google Cloud client library
from google.cloud import speech

#client = Client.from_service_account_json('ArckinFinal-48cf72756e29.json')
# Instantiates a client
speech_client = speech.Client()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    'audio.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    sample = speech_client.sample(
        content,
        source_uri=None,
        encoding='LINEAR16',
        sample_rate_hertz=16000)

# Detects speech in the audio file
alternatives = sample.recognize('hi-IN')
input = ""
for alternative in alternatives:
#    input = ('Transcript: {}'.format(alternative.transcript.encode('utf-8')))
     input = (alternative.transcript.encode('utf-8'))
print input
