### Overview
A Python program to to retrieve information from a films database. 
Queries a films database based on a search string and returns a list of movies matching it.

### Requirements:
    - Python 3.x
    - External modules: `requests`, allows you to send HTTP request easily

To install modules:
```
pip install -r requirements.txt
```
### Usage:
```
Script can be run in two ways:

python3 movie_search.py <search string> 

#example
python3 movie_search.py bat

or

python3 movie_search.py
>Enter the movie search string: bat 

```

Output:
```
['Aquaman: Battle for Atlantis', 'Batman: Rise of Sin Tzu', 'Eastern Promises: Two Guys Walk Into a Bathhouse', 'Harry Batt', 'Hold at All Costs: The Story of the Battle of Outpost Harry', 'Memorias sin batallas y otros muertos', 'Sin on the Sabbath', 'Siu bat sin', 'Superman, Spiderman or Batman', 'The Astounding Harry Bates', 'The Story of the Battle of Outpost Harry', 'Three Actresses Walk Into a Bathroom...', 'WWE: Batista - I Walk Alone']
```