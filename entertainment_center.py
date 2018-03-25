import media
import fresh_tomatoes

i_m_d = "https://ia.media-imdb.com/images/M/"  #media domain for imdb
y_t_d = "https://www.youtube.com/watch?v="     #media domain for youtube

#Creating Movie Instances with media.Movie(Title, Storyline, PosterUrl, TrailerUrl)

wedding_crashers = media.Movie(
    "Wedding Crashers",
    "John Beckwith and Jeremy Grey, a pair of committed womanizers who sneak into weddings",  #NOQA
    i_m_d+"MV5BZmJkNzViYjYtZWZlNy00OGE4LWI2MzUtYTcwNjY3Y2MyODIwXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
    y_t_d+"ZeUSo8voIXM")

meet_joe_black = media.Movie(
    "Meet Joe Black",
    "Death, who takes the form of a young man, asks a media mogul to act as a guide to teach him about life on Earth",  #NOQA
    i_m_d+"MV5BNTc0MzRmMTgtMTk4OS00MzdkLWJjNWMtZWJmZjlkYTI0YWRiL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  #NOQA
    y_t_d+"_zIOjl93WrU")

big_daddy = media.Movie(
    "Big Daddy",
    "A lazy law school grad adopts a kid to impress his girlfriend, but everything doesn't go as planned and he becomes the unlikely foster father",  #NOQA
    i_m_d+"MV5BYjAzNzQ4YzEtZWFlOS00YWVkLWE2NDctZDBiZTUxYjgwOTYzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  #NOQA
    y_t_d+"fUtfe0r1zT0")

do_over = media.Movie(
    "The Do Over",
    "Two down-on-their-luck guys decide to fake their own deaths and start over with new identities",  #NOQA
    i_m_d+"MV5BMTYyNDY2NzAxNV5BMl5BanBnXkFtZTgwOTMxMzg2ODE@._V1_SY1000_SX675_AL_.jpg",  #NOQA
    y_t_d+"1LxNRKuWZZ8")

meet_the_fockers = media.Movie(
    "Meet The Fockers",
    "All hell breaks loose when the Byrnes family meets the Focker family for the first time.",  #NOQA
    i_m_d+"MV5BMWZjODQxMWMtZmIzYS00YjMwLWFiZTctYmFiZmJiNjljYWVmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX675_AL_.jpg",  #NOQA
    y_t_d+"r5Vpw5QP8FU")

i_love_you_man = media.Movie(
    "I Love You Man",
    "Friendless Peter Klaven goes on a series of man-dates to find a Best Man for his wedding",  #NOQA
    i_m_d+"MV5BMTU4MjI5NTEyNV5BMl5BanBnXkFtZTcwNjQ1NTMzMg@@._V1_.jpg",  #NOQA
    y_t_d+"kRLf04gH7mc")

#Creating the array for movie list
movies = [wedding_crashers, meet_joe_black, big_daddy, do_over, meet_the_fockers, i_love_you_man]

fresh_tomatoes.open_movies_page(movies)
