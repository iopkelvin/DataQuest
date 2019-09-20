## 1. Introduction ##

import pandas as pd
hn = pd.read_csv("hacker_news.csv")

## 2. The Regular Expression Module ##

import re

titles = hn["title"].tolist()

python_mentions = 0
pattern = "[Pp]ython"
for title in titles:
    if re.search(pattern, title):
        python_mentions += 1

## 3. Counting Matches with pandas Methods ##

pattern = '[Pp]ython'
titles = hn['title']
python_mentions = titles.str.contains(pattern).sum()

## 4. Using Regular Expressions to Select Data ##

pattern = "[Rr]uby"
titles = hn["title"]
ruby_titles = titles[titles.str.contains(pattern)]
ruby_titles.head(3)

## 5. Quantifiers ##

# The `titles` variable is available from
# the previous screens
pattern = "e-?mail"
email_bool = titles.str.contains(pattern)
email_count = titles[email_bool].count()
email_titles = titles[email_bool]

## 6. Character Classes ##

pattern = "\[\w+\]"
tag_titles = titles.str.contains(pattern)
tag_count = tag_titles.sum()

## 7. Accessing the Matching Text with Capture Groups ##

pattern = r"\[(\w+)\]"
tag_freq = titles.str.extract(pattern).value_counts()

## 8. Negative Character Classes ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return all_matches

pattern = r"[Jj]ava[^Ss]"
java_titles = first_10_matches(pattern)



## 9. Word Boundaries ##

def first_10_matches(pattern):
    matches = titles[titles.str.contains(pattern)]
    return matches 
pattern = r"\b[Jj]ava\b"
java_titles = first_10_matches(pattern)

## 10. Matching at the Start and End of Strings ##

pattern = r"^\[\w+\]"
beginning_count = titles.str.contains(pattern).sum()
pattern_end = r"\[\w+\]$"
ending_count = titles.str.contains(pattern_end).sum()

## 11. Challenge: Using Flags to Modify Regex Patterns ##

import re

email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL'])
email_mentions = titles.str.contains(r"e[ -]?mail", flags = re.I).sum()