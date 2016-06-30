#man bc from terminal for calculator manual entry

#integers
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

#exponents = **
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)

#order of operations
ans = 2 + 3*4
print(ans)

ans = (2 + 3) * 4
print(ans)

#floats - any number with a decimal point
ans = 0.1 + 0.1
print(ans)

ans = 0.2 + 0.2
print(ans)

ans = 2 * 0.1
print(ans)

ans = 2 * 0.2
print(ans)

ans = 0.2 +0.1
print(ans)
ans = round(ans,1)
print(ans)

ans = 3 * 0.1
print(ans)
ans = round(ans,1)
print(ans)
print("The answer is " + str(ans))

#integers within a string
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

#practice - operations
ans = 2 + 6
print(ans)

ans = 12 - 4
print(ans)

ans = 2 * 4
print(ans)

ans = 16 / 2
print(ans)

#math.--- operations, see results by inputing different values for variable ans (postive, negative) 
import math
print(math.trunc(ans))
print(math.floor(ans))
print(math.trunc(8.566))
print(math.floor(8.566))
print(math.ceil(8.566))

#test with different numbers
ans = 1.422
print("number is " + str(ans))
print("trun:\t" + str(math.trunc(ans)))
print("floor:\t" + str(math.floor(ans)))
print("ceil:\t" + str(math.ceil(ans)))

#more string integer statements

#options for playing audio in python
#pymedia needs to be downloaded then imported, tried other methods like afplay
#still need a while or execute statement to continue to print other messages while playing audio
'''
import time
import time
import wave
import pymedia.audio.sound as sound

f = wave.open('Desktop\jeopardy-theme-song.wav','rb')
sampleRate = f.getframerate()
channels = f.getchannels()
format = sound.AFMT_S16_LE
snd = sound.Output(sampleRate, channels, format)
s = f.readframes(300000)
snd.play(s)

import sys
fname = "Desktop\jeopardy\theme-song.wav"
def playWAV( fname ):
  import pymedia.audio.sound as sound
  import time, wave
  f= wave.open( fname, 'rb' )
  sampleRate= f.getframerate()
  channels= f.getnchannels()
  format= sound.AFMT_S16_LE
  snd1= sound.Output( sampleRate, channels, format )
  s= ' '
  while len( s ):
    s= f.readframes( 1000 )
    snd1.play( s )
  
  # Since sound module is not synchronous we want everything to be played before we exit
  while snd1.isPlaying(): time.sleep( 0.05 )
'''
#import time for delay and subprocess to call function afplay to play the .wav file
#still want to figure out a way to play the .wav file while running continuing to run scripts
#(while command? something like while afplay runs print ... every 2 seconds, when ends run ans DESCARTES!)

import time
import subprocess

print("\n\n\nAND NOW FOR SOMETHING COMPLETELY DIFFERENT!\n\n\n")
time.sleep(3)
favorite_number = 3**2 * 7**2 * 11**2 * 13**2 * 22021
message = str(favorite_number) + " is my favorite number."

print(message)
time.sleep(3)
print("\t\t\t\t\tWho am I?")

subprocess.call(["afplay", "/Users/einatkorman/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/Jeopardy-theme-song.wav"])

print("\t\t\t\t\t\t\tDESCARTES!!!")

    

