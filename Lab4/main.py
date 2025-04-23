

class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def play(self, movie):
        print(f"Playing movie: {movie}")

    def off(self):
        print("DVD Player is OFF")


class Projector:
    def on(self):
        print("Projector is ON")

    def set_wide_screen_mode(self):
        print("Projector set to widescreen mode")

    def off(self):
        print("Projector is OFF")


class AudioSystem:
    def on(self):
        print("Audio System is ON")

    def set_surround_sound(self):
        print("Surround sound enabled")

    def off(self):
        print("Audio System is OFF")


# Fasada

class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, projector: Projector, audio: AudioSystem):
        self.dvd = dvd
        self.projector = projector
        self.audio = audio

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.projector.on()
        self.projector.set_wide_screen_mode()
        self.audio.on()
        self.audio.set_surround_sound()
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.dvd.off()
        self.projector.off()
        self.audio.off()


if __name__ == "__main__":
    dvd = DVDPlayer()
    projector = Projector()
    audio = AudioSystem()

    theater = HomeTheaterFacade(dvd, projector, audio)

    theater.watch_movie("Inception")
    print("\n---\n")
    theater.end_movie()
