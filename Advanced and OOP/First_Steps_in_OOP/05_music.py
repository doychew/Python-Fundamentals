class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Ot izvora", "Ivana", "ot izvora se pie na kolene i na kolene se blagodari")
print(song.print_info())
print(song.play())
