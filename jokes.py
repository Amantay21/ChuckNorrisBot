from joke.jokes import *

from joke.joke.jokes import geek, icanhazdad, chucknorris, icndb

# This will import all joke-functions (geek, icanhazdad, chucknorris, icndb)
# Now you can use them to get some jokes.
all_jokes = [geek, icanhazdad, chucknorris, icndb]


for i in range(10):
    print(chucknorris())

# Or get a random joke-function.
from random import choice
print(choice([geek, icanhazdad, chucknorris, icndb])())

for func in all_jokes:
    print(func())