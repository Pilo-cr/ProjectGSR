from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file("warning.mp3", format="mp3")
play(song)
