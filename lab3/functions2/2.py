# Dictionary of movies

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


def first(movies):
    a=input('MOVIE NAME: ')
    for films in movies:
        if films['name']==a and films['imdb']>5.5:
            return True
print(first(movies))
print()
print()
print()



#2
def second(movies):
    arr=[]
    for each in movies:
        if each['imdb'] >5.5
        arr.append(each)
print(second(movies))
print()
print()
print()



#3
def third(movies):
    cat=input("CATEGORY: ")
    mydict={cat:[]}
    for film in movies:
        if film['category']==cat:
            mydict[cat].append(film['name'])
    return mydict
print(third(movies))
print()
print()
print()



#4
def fourth(movies):
    sum=0
    for mov in movies:
        sum+=mov['imdb']
    return sum/len(movies)
print(fourth(movies))
print()
print()
print()

#5
def fifth(movies):
    cat=input("CATEGORY: ")
    sum=0
    cnt=0
    for films in movies:
        if films['category']==cat:
            sum+=films['imdb']
            cnt+=1
    return sum/cnt
print(fifth(movies))

