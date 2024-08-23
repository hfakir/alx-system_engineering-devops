## API advanced

**Function Prototypes :floppy_disk:**

*0-subs.py*: ```def number_of_subscribers(subreddit)```
*1-top_ten.py*: ```def top_ten(subreddit)```
*2-recurse.py*: ```def recurse(subreddit, hot_list=[])```
*100-count.py*: ```def count_words(subreddit, word_list)```

**Tasks 📃:**

# 0. How many subs?
    💠 Python function that returns the total number of subscribers for a given subreddit.
    💠 Returns ```0``` if an invalid subreddit is given.

# 1. Top Ten:
    💠Python function that prints the top ten hottest posts for a given subreddit.
    💠 Prints ```None``` if an invalid subreddit is given.

# 2. Recurse it:
    💠 Python function that recusively returns a list of titles for all hot articles on a given subreddit.
    💠 Returns ```None``` if no results are found on the given subreddit.

# 3. Count it:
    💠 Python function that recursively prints a sorted count of given keywords parsed from titles of all hot articles on a given subreddit.
    💠 Keywords are case-insensitive and delimited by spaces.
    💠 Results are printed in descending order by count.
    💠 Words with identical counts are sorted alphabetically.
    💠 Words with no matches are skipped.
    💠 Results are based on the number of times a keyword appears - ie. ```jave java java``` counts as three separate instances of ```java```.