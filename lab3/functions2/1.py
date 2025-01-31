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

#1
def first(movies):
    good={}
    for films in movies:
        if films["imdb"]>5.5:
            good.update({films["name"]:True})
    return good
print(first(movies))
print()
print()
print()


#2
def second(movies):
    ar=[]
    for mov in movies:
        if mov['imdb']>5.5:
            ar.append(mov['name'])
    return ar
print(second(movies))
print()
print()
print()

#3
def third(movies):
    cat=[]
    for films in movies:
        cat.append(films['category'])
    ar3=list(set(cat))
    mydict={}
    for c in ar3:
        mydict.update({c:[]})
    for c in ar3:
        for films in movies:
            if films["category"]==c:
                mydict[c].append(films["name"])
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
    arr=[]
    avg=0
    cnt=0
    total=0
    for mov in movies:
        arr.append(mov['category'])
    categor=list(set(arr))
    d={}
    for cat in categor:
        avg=0
        cnt=0
        for film in movies:
            if film["category"]==cat:
                avg+=film["imdb"]
                cnt+=1
        total=avg/cnt
        d.update({str(cat):total})
    return d
        
print(fifth(movies))
