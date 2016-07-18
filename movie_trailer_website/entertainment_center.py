import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Story about toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_intouchables = media.Movie("The Intouchables",
                               "The story of the friendship between the two men",
                               "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
                               "https://www.youtube.com/watch?v=34WIbmXkewU")


def open():
    movies = [toy_story, avatar, the_intouchables]
    fresh_tomatoes.open_movies_page(movies)


def main():
    open()

if __name__ == '__main__':
    main()

