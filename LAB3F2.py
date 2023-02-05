movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def func1(movie):
    if (movie["imdb"] > 5.5):
        return True
    return False


print(func1(movies[7]))


# Write a function that returns a sublist of movies with an IMDB score above 5.5.
def func2(movies):
    anslist = []
    for i in range(0, len(movies)):
        film = movies[i]
        if film["imdb"] > 5.5:
            anslist.append(film)
    return anslist


print(func2(movies))


# Write a function that takes a category name and returns just those movies under that category.
def func3(movies, cat):
    answer = []
    for i in movies:
        zh = i["category"]
        if cat == zh:
            answer.append(i)
    return answer


print(func3(movies, "Action"))


# Write a function that takes a list of movies and computes the average IMDB score.
def avrg(movies):
    numofmovies = len(movies)
    tot = 0
    for i in movies:
        tot = tot + i["imdb"]
    tot = tot / numofmovies
    print(tot)


avrg(movies)


# Write a function that takes a category and computes the average IMDB score.
def func5(movies, cat):
    catlist = []
    for i in movies:
        cot = i["category"]
        if cat == cot:
            catlist.append(i)
    return catlist


def func6(newlist):
    numoflist = len(newlist)
    av = 0
    for i in newlist:
        av = av + i["imdb"]
    av = av / numoflist
    print(av)


func6(func5(movies, "Romance"))
