from project.album import Album, album
from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if self.name in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album.name)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name in self.albums:
            self.albums.remove(album_name)
            return f"Album {album_name} has been removed."
        if album.published:
            return f"Album has been published. It cannot be removed."
        if album_name not in self.name:
            return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n{''.join(self.albums)}"



