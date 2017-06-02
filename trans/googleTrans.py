from wxconv import WXC
from translate import Translator
from gtts import gTTS
import os,io

#input = "Hello sir aap kaise hai"
#con = WXC(order='wx2utf', lang='hin')
#input2 = con.convert(input) 
#print input2
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

input2 = u""
for alternative in alternatives:
#    print('Transcript: {}'.format(alternative.transcript.encode('utf-8')))
     input2 = (alternative.transcript.encode('utf-8'))


#print input2
translator= Translator(to_lang="en")
translation = translator.translate(input2.decode('utf-8','ignore'))

#tts = gTTS(text=translation, lang="en")
#tts.save("hello.mp3")
#os.system("omxplayer hello.mp3")

