import random
from pydub import AudioSegment

time = 0
list=[]
while time < 240000:
    title = str(random.randint(0, 12))
    newAudio = AudioSegment.from_mp3("MP3/"+title+".mp3")
    bTime = random.randint(1000, len(newAudio)-1000)
    pTime = random.randint(1000, 5000)
    newAudio = newAudio[bTime:bTime+pTime]
    list.append(newAudio)
    time += pTime
finalAudio=sum(list)
finalAudio.export('essais/finalAudio6.mp3', format="mp3") #Exports to a mp3 file in the current path.
