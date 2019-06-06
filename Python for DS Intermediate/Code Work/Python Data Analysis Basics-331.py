## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for row in moma:
    date = row[6]
    if date != '':
        date = int(date)
    row[6] = date

## 2. Calculating Artist Ages ##

ages = []
for rows in moma:
    date = rows[6]
    birth = rows[3]
    if type(birth) == int:
        age = date - birth
    elif type(birth) != int:
        age = 0
    ages.append(age)
    
final_ages = []
for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)

## 3. Converting Ages to Decades ##

# The ages variable is available
# from the previous screen

decades = []

for age in ages:
    if age == "Unknown":
        decade = age
    elif age != "Unknown":
        decade = str(age)
        decade = decade[:-1]
        decade = decade + "0s"
    decades.append(decade)
        
    

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency = {}
for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade] = 1
    else:
        decade_frequency[decade] += 1

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
phrase = "{}'s birth year is {}".format(artist, birth_year)
print(phrase)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}
for item in moma:
    artist = item[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1

## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    artworks = artist_freq[artist]
    phrase = "There are {} artworks by {} in the data set".format(artworks, artist)
    print(phrase)
    
artist_summary("Henri Matisse")



## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for pair in pop_millions:
    country, population = pair
    phrase = "The population of {} is {:,.2f} million".format(country, population)
    print(phrase)
    


## 9. Challenge: Summarizing Artwork Gender Data ##

freq_gender = {}
for row in moma:
    gender = row[5]
    if gender not in freq_gender:
        freq_gender[gender] = 1
    else:
        freq_gender[gender] += 1

for key, value in freq_gender.items():
    phrase = "There are {:,} artworks by {} artists".format(value, key)
    print(phrase)