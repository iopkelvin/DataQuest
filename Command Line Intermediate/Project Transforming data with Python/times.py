import read
from dateutil import parser
def extract(text):
	return parser.parse(text).hour
data = read.load_data()
print(data["submission_time"].apply(extract).value_counts())
	
