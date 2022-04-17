import numpy as np
from numpy import random

class MoviesDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}

    def add_movie(self, title, year, category, rating):
        self.titles.append(title)
        self.movies[title] = {'year': year,'category':category, 'rating':rating}
        print(f'{title} ({year}) added to the database.')

    def what_to_watch(self, category = 'all'):
        if category == 'Action':
            action = {key: value for (key, value) in self.movies.items() if value['category'] == 'Action'}
            print('action', action)
            
            action_titles = []
            for t in action:
                action_titles.append(t)

            print('action_titles', action_titles)
            
            choice = random.choice(action_titles)
            movie = self.movies[choice]
            print(f"Your move today is {choice} ({movie['year']}), which is a {movie['category']} movie")

        else:
            choice = random.choice(self.titles)
            movie = self.movies[choice]
            print(f"Your move today is {choice} ({movie['year']}), which is a {movie['category']}")
    
def main():
    
    mdb = MoviesDataBase()

    mdb.add_movie('Fight CLub',' 1999','Action', '8.8')
    mdb.add_movie('Inception', '2010', 'Action', '8.8')
    mdb.add_movie('3 Idiots', '2009', 'Comedy', '8.4')
    mdb.add_movie('Hamilton', '2020', 'Musical', '8.5')

    print(mdb.what_to_watch(category='Action'))


if __name__ == "__main__": main()