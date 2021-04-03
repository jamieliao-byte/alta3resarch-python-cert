#!/usr/bin/env python3

'''By Jamie Liao
A program search data for you favorite TV show
Enter TV show name to search
'''

import requests, crayons

# get show name 
def enter_show():
    print(crayons.blue('***************************************', bold=True))
    print(crayons.red('* All About TV Shows                   *', bold=True))
    print(crayons.blue('***************************************', bold=True))

    x = input("\nTell me the name of your favorite TV Show:")
    return x.lower()

# give out facts
# name, language, rating and summary
def show_facts(mfact):
    # looping through show data
    for tshow in mfact:
        print(crayons.yellow('\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', bold=True))
        print("\nName:", tshow.get("show").get("name"), sep=" ")
        print("\nLanguage:", tshow.get("show").get("language"), sep=" ")
        print("\nRating:", tshow.get("show").get("rating").get("average"), sep=" ")
        print("\nSummary:", tshow.get("show").get("summary"), sep=" ")

def main():
    #define API url
    SHOWAPI = "http://api.tvmaze.com/search/shows?q="
    
    # read show title 
    tsearch = enter_show()

    # make the API request
    mfacts = requests.get(SHOWAPI + tsearch)

    # make sure we got back a 200 response
    if mfacts.status_code != 200:
        print(f"Uh oh, something went wrong, it returned {mfacts.status_code}")
        exit()

    # strip of JSON if we did get back 200 response
    mfact = mfacts.json()

    # grab data from JSON that we want to loop through
    show_facts(mfact)


if __name__ == "__main__":
    main()

