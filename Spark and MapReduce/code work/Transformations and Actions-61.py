## 1. Introduction to the Data ##

raw_hamlet = sc.textFile('hamlet.txt')
raw_hamlet.take(5)

## 2. The Map Method ##

split_hamlet = raw_hamlet.map(lambda x:x.split('\t'))

## 5. Filter Using a Named Function ##

def filter_hamlet_speaks(line):
    if 'HAMLET' in line:
        return line

hamlet_spoken_lines = split_hamlet.filter(lambda line: filter_hamlet_speaks(line))
hamlet_spoken_lines.take(5)

## 6. Actions ##

spoken_count = 0
spoken_101 = list(hamlet_spoken_lines.collect()[100])
spoken_count = hamlet_spoken_lines.count()
