import random


class Song():
    def __init__(self, name, author, duration, key):
        self.name = name
        self.author = author
        self.duration = duration
        self.key = key

    def __str__(self):
        return "{0} by {1} for {2} seconds long.".format(self.name, self.author, str(self.duration))

class Jukebox():
    def __init__(self):
        self.song_list = []
        self.queue = []

    def play(self, key):
        song = self.getSong(key)
        print("Play: {0} by {1}".format(song.name, song.author))
        self.queue.append(song)
        return self.queue

    def getSong(self, check):
        for song in self.song_list:
            if (song.key == check):
                return song

    def createList(self):
        songs = ['title', 'self', 'channel 5', 'ligma', 'testing', 'NootNoot', 'Rick', 'numba 5', 'ezzz']
        authors = ['tyler', 'mitchel', 'keevan', 'dank', 'drippy']
        
        let = ['A', 'B', 'C']
        nums = ['1', '2', '3', '4', '5']
        links = []

        for i in range(len(let)):
            for j in range(len(nums)):
                link = "{0}-{1}".format(let[i], nums[j])
                links.append(link)

        for i in range(len(songs)):
            song = Song(songs[i], authors[random.randint(0, len(authors)-1)], random.randint(60, 300), links[i])
            print(song)
            self.song_list.append(song)
        
        return self.song_list

jukebox = Jukebox()
jukebox.createList()
jukebox.play('A-4')