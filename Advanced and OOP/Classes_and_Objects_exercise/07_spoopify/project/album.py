from project.band import Band
from project.song import Song
class Album:
    def __init__(self, name, song):
        self.name = name
        self.published = False
        self.songs = []
        self.song = song

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        else:
            self.songs.append(song.name)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if song_name not in self.songs:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        self.songs.remove(song_name)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):

        return f"Album {self.name}\n" f"== {''.join(self.songs)}"




