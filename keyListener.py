#
# Author: Patrik Sokolowski
# Date: 10/17/2022

from pynput.keyboard import Listener
import obspython as obs

print("Listener ONLINE")

#num-9

fileName = "X:\Python\OBSeventListener\timeLOG.txt"

start = 'Key.end'
highlight = 'Key.down'
cut = 'Key.page_down'
end = 'Key.left'

def on_press(key):
    if(str(key) == start):
        f = open("X:\Python\OBSeventListener\timeLOG.txt", "a")
        f.write(str(key) + "\n")
        print(key)
        print("TimeStamp Start")
        f.close()
    if(str(key) == highlight):
        f = open("X:\Python\OBSeventListener\timeLOG.txt", "a")
        f.write(str(key) + "\n")
        print(key)
        print("TimeStamp Highlight")
        f.close()
    if(str(key) == cut):
        f = open("X:\Python\OBSeventListener\timeLOG.txt", "a")
        f.write(str(key) + "\n")
        print(key)
        print("TimeStamp Cut")
        f.close()
    if(str(key) == end):
        f = open("X:\Python\OBSeventListener\timeLOG.txt", "a")
        f.write(str(key) + "\n")
        print(key)
        print("TimeStamp End")
        f.close()
        

def on_release(key):
    print("")

if __name__ == '__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


