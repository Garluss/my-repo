import pygame as pg

class Song():
    songs = []
    def __init__(self, name, file):
        self.file = file
        self.name = name
        Song.songs.append(self)
    
    def get_path(self):
        return self.file
    
    @classmethod
    def get_songs(self):
        list = []
        for i in Song.songs:
            list.append(i.name)
        return list

ss = Song("snitch", "D:\\SKOLE\\Programmer - IT2\\Del 4\\audio\\Sneaky Snitch.wav")

pg.init()
pg.mixer.init()
print("")

cont = True
while cont:
    action = input("What is your action? ").lower()
    match action:
        case "play":
            t = 0
            for i in Song.get_songs():
                t += 1
                print(f"{t}: {i}")
            song = int(input("Choose a song from the list. "))
            if song <= t and song > 0:
                pg.mixer.music.load(Song.songs[song-1].get_path())
                pg.mixer.music.play()
                while True:
                    action = input("Perform an action? ")
                    match action:
                        case "pause":
                            if pg.mixer.music.get_busy() == True:
                                pg.mixer.music.pause()
                            else:
                                pg.mixer.music.unpause()
                        case "stop":
                            pg.mixer.music.stop()
                            break
                        case "rewind":
                            pg.mixer.music.rewind()
                        case "volume":
                            print(f"Current volume: {pg.mixer.music.get_volume()}")
                            vol = float(input("New volume: "))
                            pg.mixer.music.set_volume(vol)
                        case _:
                            print("Commands include: pause, stop, rewind, volume.")
        case "quit":
            print("Quitting...")
            cont = False
        case _:
            print("Commands include: play, quit.")