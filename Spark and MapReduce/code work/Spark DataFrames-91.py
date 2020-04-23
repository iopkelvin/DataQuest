## 1. The Spark DataFrame: An Introduction ##

with open('census_2010.json') as data:
    for i in range(4):
        print(data.readline())

## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()

## 4. Pandas vs Spark DataFrames ##

df.show(5)

## 5. Row Objects ##

# row_one = df.head(5)[0]
# print(row_one)
# # print(# Access value for age
# print(row_one.age)
# # print(# Access the first value
# print(row_one[0])

first_five = df.head(5)
for line in first_five:
    print(line.age)

## 6. Selecting Columns ##

# df[['age']].show()
df.select('age', 'males', 'females').show()

## 7. Filtering Rows ##

five_plus = df[df['age'] > 5]
five_plus.show()

## 8. Using Column Comparisons as Filters ##

df[df['females'] < df['males']].show(20)

## 9. Converting Spark DataFrames to pandas DataFrames ##

pandas_df = df.toPandas()
pandas_df.total.hist()