## 2. Register the DataFrame as a Table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")

df.registerTempTable('census2010')
tables = sqlCtx.tableNames
print(tables)

## 3. Querying ##

sqlCtx.sql('SELECT age FROM census2010').show()

## 4. Filtering ##

query = 'SELECT males, females FROM census2010 WHERE age BETWEEN 5 AND 15'
sqlCtx.sql(query).show()

## 5. Mixing Functionality ##

query = 'SELECT males, females FROM census2010'
sqlCtx.sql(query).describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')
df_2000 = sqlCtx.read.json("census_2000.json")
df_1990 = sqlCtx.read.json("census_1990.json")
df_1980 = sqlCtx.read.json("census_1980.json")

df_2000.registerTempTable('census2000')
df_1990.registerTempTable('census1990')
df_1980.registerTempTable('census1980')
tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

query = '''
SELECT census2010.total, census2000.total
FROM census2010 
INNER JOIN census2000 
ON census2010.age = census2000.age
'''

sqlCtx.sql(query).show(20) 

## 8. SQL Functions ##

query = """
SELECT SUM(census2010.total), SUM(census2000.total), SUM(census1990.total)
FROM census2010
INNER JOIN census2000
ON census2010.age = census2000.age
INNER JOIN census1990
ON census2010.age = census1990.age
"""
sqlCtx.sql(query).show()