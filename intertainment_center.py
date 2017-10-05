import fresh_tomatoes
import media

toy_story = media.Movie(
    "toy story",
    "a story of a boy and his toys that come to life !",
    "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

THOR = media.Movie(
    "THOR",
    "a boy playing with his toy",
    "http://www.tahrirnews.com/files/cached/images/b501ac993c0086373c408223b6aea6e6_920_420.jpg",
    "https://www.youtube.com/watch?v=v7MGUNV8MxU&t=3s"
    )

fast_furious_8 = media.Movie(
    "fast & furious 8",
    "is a film talking about car racing",
    "https://media.premiumtimesng.com/wp-content/files/2017/04/fate-of-the-furious-poster-header-image.jpg",
    "https://www.youtube.com/watch?v=uisBaTkQAEs&t=1s"
    )

Hrob_Edtrary = media.Movie(
    "Hrob Edtrary",
    "is an action film",
    "http://www.el-tareeq.net/images/NewsArticle/16680.jpg",
    "https://www.youtube.com/watch?v=kRiQRPHC9O4"
    )

JUSTICE_LEAGUE = media.Movie(
    "JUSTICE LEAGUE",
    "Justice League is an upcoming American superhero film based on the DC Comics superhero team of the same name, distributed by Warner Bros",
    "http://www.konbini.com/us/files/2017/07/league.jpg",
    "https://www.youtube.com/watch?v=3cxixDgHUYw"
    )

music_maker = media.Movie(
    "music player",
    "a man who playing on piano",
    "https://i.ytimg.com/vi/W2I9b5WZuYA/hqdefault.jpg",
    "https://www.youtube.com/watch?v=1GCPDChh8m0"
    )

school_of_rock = media.Movie(
    "School of rock",
    "School of Rock is a 2003 musical comedy film directed by Richard Linklater, produced by Scott Rudin, and written by Mike White",
    "https://i.ytimg.com/vi/SfStJdDyeQo/hqdefault.jpg",
    "https://www.youtube.com/watch?v=z5aLjGxdX_0"
    )

movies = [toy_story, THOR, fast_furious_8, Hrob_Edtrary, JUSTICE_LEAGUE, music_maker, school_of_rock]
fresh_tomatoes.open_movies_page(movies) #is related to fresh tomatoes page which is responsible for openin the page in the browser
