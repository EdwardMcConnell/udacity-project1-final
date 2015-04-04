# Movie class
import media

# Udacity Fresh tomatoes module
import fresh_tomatoes

# Create Movie objects
toy_story = media.Movie("Toy Story", 
                        "https://www.movieposter.com/posters/archive/main/15/A70-7642",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "G",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.",
                        81,
                        "November 22, 1995")

avatar = media.Movie("Avatar",
                     "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "PG-13",
                     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
                     178,
                     "December 18, 2009")

usual_suspects = media.Movie("The Usual Suspects",
                             "http://www.impawards.com/1995/posters/usual_suspects_ver2.jpg",
                             "https://www.youtube.com/watch?v=oiXdPolca5w",
                             "R",
                             '"The greatest trick the devil ever pulled was convincing the world he didn\'t exist," says con man Kint (Kevin Spacey), drawing a comparison to the most enigmatic criminal of all time, Keyser Soze. Kint attempts to convince the feds that the mythic crime lord not only exists, but is also responsible for drawing Kint and his four partners into a multi-million dollar heist that ended with an explosion in San Pedro Harbor - leaving few survivors.',
                             108,
                             "August 16, 1995")

# Add Movies to list
movies = [toy_story, avatar, usual_suspects]

# Generate HTML and open in browser
fresh_tomatoes.open_movies_page(movies)
