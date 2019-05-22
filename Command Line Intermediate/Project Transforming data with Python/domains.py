import pandas as pd
import read
#import tldextract as tldex
hn = read.load_data()
#def urls(text):
#	return tldex.extract(text).registered_domain

#hn = hn["url"].apply(urls)
		
hn_value = hn["url"].value_counts()[:100]

for key,value in hn_value.items():
	print("{}: {}".format(key,value))


