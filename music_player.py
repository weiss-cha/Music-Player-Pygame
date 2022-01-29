#dependencies: pygame

from pygame import mixer
import os
import random

os.chdir('D:\\root\\Etc\\280120') #folder location
a=random.choice(os.listdir('D:\\root\\Etc\\280120'))

mixer.init()
mixer.music.load(a)
mixer.music.play()
print(a)

b=input('Shuffle?')

while b=='yes':

    a=random.choice(os.listdir('D:\\root\\Etc\\280120'))
    mixer.init()
    mixer.music.load(a)
    mixer.music.play()
    print(a)
    b=input('Shuffle?')
