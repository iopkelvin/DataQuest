## 2. Introduction to the Data Set ##

import pandas as pd
columns = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
titanic = pd.read_csv("train.csv")
titanic = titanic[columns]
titanic = titanic.dropna()


## 3. Creating Histograms In Seaborn ##

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(titanic["Age"])
plt.show()

## 4. Generating A Kernel Density Plot ##

sns.kdeplot(titanic["Age"], shade = True)
plt.xlabel("Age")
plt.show()

## 5. Modifying The Appearance Of The Plots ##

sns.set_style("white")
sns.kdeplot(titanic["Age"], shade = True)
plt.xlabel("Age")
sns.despine(left= True, bottom = True)


## 6. Conditional Distributions Using A Single Condition ##

g = sns.FacetGrid(titanic, col = "Pclass", size = 6)
g.map(sns.kdeplot, "Age", shade = True)
sns.despine(left= True, bottom = True)
plt.show()

## 8. Creating Conditional Plots Using Three Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = "Sex", size = 3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()



## 9. Adding A Legend ##

fg = sns.FacetGrid(titanic, col ="Survived", row ="Pclass", hue ="Sex", size =3)
fg.map(sns.kdeplot, "Age", shade = True).add_legend()
sns.despine(bottom=True, left=True)
plt.show()
