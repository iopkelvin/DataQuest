import read
from collections import Counter
open = read.load_data()
block = ""
for i in open["headline"]:
	block += " "+str(i)
block = block.lower().split()
#print(block)
count = Counter()
for word in block:
	count[word] += 1
	
print(count.most_common(100))

