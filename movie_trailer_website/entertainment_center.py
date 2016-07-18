import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous "
                        "when a new spaceman figure supplants him as top toy in "
                        "a boy's room.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a "
                     "unique mission becomes torn between following his orders "
                     "and protecting the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_intouchables = media.Movie("The Intouchables",
                               "After he becomes a quadriplegic from a "
                               "paragliding accident, an aristocrat hires a "
                               "young man from the projects to be his caregiver.",
                               "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
                               "https://www.youtube.com/watch?v=34WIbmXkewU")


def open():
    movies = [toy_story, avatar, the_intouchables]
    fresh_tomatoes.open_movies_page(movies)


def main():
    open()

if __name__ == '__main__':
    main()

