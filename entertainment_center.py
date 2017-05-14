import fresh_tomatoes
import media

sling_blade = media.Movie(
            "Sling Blade",
            "Karl Childers, a simple man hospitalized since his childhood\
            murder of his mother and her lover, is released to start a new life\
            in a small town.Karl Childers, a simple man hospitalized since his\
            child",
            "https://upload.wikimedia.org/wikipedia/en/4/44/Slingbladeposter.jpg",
            "https://www.youtube.com/watch?v=-RLVfo4SZfg")

taxi_driver = media.Movie(
            "Taxi Driver",
            "A mentally unstable Vietnam war veteran works as a\
            nighttime taxi driver in New York City where the\
            perceived decadence and sleaze feeds his urge to\
            violently lash out, attempting to save a teenage",
            "https://upload.wikimedia.org/wikipedia/en/8/8f/Taxi_Driver_original_movie_poster.jpg",
            "https://www.youtube.com/watch?v=cujiHDeqnHY")


apocalypse_now = media.Movie(
               "Apocalypse Now",
               "During the Vietnam War, Captain Willard is sent on a dangerous\
                mission into Cambodia to assassinate a renegade colonel who has\
                set himself up as a god among a local tribe.",
               "https://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
               "https://www.youtube.com/watch?v=FTjG-Aux_yQ")

who_is_afraid_of_virginia_woolf = media.Movie(
                                "Who's Afraid of Virginia Woolf?",
                                "The volatile marriage of a middle-aged married\
                                 couple",
                                "https://upload.wikimedia.org/wikipedia/en/7/7c/Original_movie_poster_for_the_film_Who%27s_Afraid_of_Virginia_Woolf%3F.jpg",
                                "https://www.youtube.com/watch?v=hZEKQnMCze8")

movies = [sling_blade, taxi_driver, apocalypse_now, who_is_afraid_of_virginia_woolf]
fresh_tomatoes.open_movies_page(movies)
