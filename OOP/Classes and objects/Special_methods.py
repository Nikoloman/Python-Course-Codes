class Movie:
    #Constructor of the class
    def __init__(self, title, duration, release) -> None:
        self.title = title
        self.duration = duration
        self.release = release
        print(f"The movie {self.title} was created")

    #Destructor of the class
    def __del__(self) -> None:
        print(f"The movie is being deleted")

    #Redefining string method
    def __str__(self) -> str:
        return f"{self.title} released in {self.release} with a duration of {self.duration} minutes"

    #Redefining len method
    def __len__(self):
        return self.duration

new_movie = Movie("Doctor Strange", 115, 2016)
print(str(new_movie))
print(len(new_movie))
del(new_movie)