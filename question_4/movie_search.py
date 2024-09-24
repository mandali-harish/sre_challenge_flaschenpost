"""
Movie search script
"""

import sys
import requests
import traceback

# URL for film database
film_db_url = 'https://jsonmock.hackerrank.com/api/movies/search/'

def getMovieTitles( search_str: str) -> list:
    """
    A funtion that queries a films database and returns a list of movies based on the search string.

    Parameters:
        search_str (str): Input string to be searched in the film database

    Returns: 
        titles (list): Movie titles in ascending order
    """
    try:
        titles = [] # initialize the titles array to store the movie titles
        # Parameters for the http request
        search_parameters = dict(Title = search_str, page = 1) # initialize page number to 1

        while True:
            # Get the response from url for the search string and page number in json format
            response = requests.get(url=film_db_url, params=search_parameters).json()

            # Iterate through each movie and store the title
            titles.extend([movie['Title'] for movie in response["data"]])
            
            # Go to next page
            search_parameters['page'] += 1 

            # Break the loop if next page number is greater than total pages available in the response 
            if search_parameters['page'] > response["total_pages"]:
                break

        titles.sort() #sort the titles in ascending order
        return titles
    
    except Exception as e:
        traceback.print_exc()
        raise e


if __name__=="__main__":
    # Check if argument is provided by user while calling the script
    if len(sys.argv) == 2:
        search_str = sys.argv[1]
    # If no argument is provided then ask the user to enter the argument
    else:
        search_str = input("Enter the movie search string: ")
    
    print(getMovieTitles(search_str))