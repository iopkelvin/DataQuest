## 3. Tokenizing the Headlines ##

tokenized_headlines = []
for row in submissions['headline']:
    tokenized_headlines.append(row.split())
    


## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []

for item in tokenized_headlines:
    words = []
    for word in item:
        word = word.lower()
        for punc in punctuation:
            word = word.replace(punc, '')
        words.append(word)
    clean_tokenized.append(words)    

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
unique_tokens = []
single_tokens = []


for list_words in clean_tokenized:
    for word in list_words:
        if word not in single_tokens:
            single_tokens.append(word)
        else:
            unique_tokens.append(word)    
# for list_words in clean_tokenized:
#     for word in list_words:
#         if word in single_tokens:
#             unique_tokens.append(word)

counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for index, words_list in enumerate(clean_tokenized):
    for word in words_list:
        if word in unique_tokens:
            counts.iloc[index][word] += 1
    

## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and counts
word_counts = counts.sum(axis=0)
counts = counts.loc[:, (word_counts >= 5) & (word_counts <= 100)]

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

mse = sum((predictions - y_test) ** 2) / len(y_test)    