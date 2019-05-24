This assignment uses 3 csv files (Hud_2005.csv, Hud_2007.csv, Hud_2013.csv).
It merges them together, cleans, and explores the data.
New merged data found in "Combined_hud.csv".

csvkit is used with following commands:

csvstack: for stacking rows from multiple CSV files.
  *  csvstack -n origin -g 1,2,3 file1.csv file2.csv file3.csv > final.csv
     -n (adds new column) 
     -g (adds values that differentiate each row based on csv file

csvlook: renders CSV in pretty table format.
  *  Head -10 final.csv | csvlook

csvcut: for selecting specific columns from a CSV file.
  *  csvcut -n Combined_hud.csv
     -n (parses and displays columns in CSV file along with an unique integer idenfifier)
  *  csvcut -c 1 Combined_hud.csv
     -c (selects an specific integer based on -n identifier
	
csvstat: for calculating descriptive statistics for some or all columns.
  * csvcut -c 4 Combined_hud.csv | csvstat
     -csvstat can use an a specific column based on csvcut -n / -c. 
     -csvstat goes after | as output
     -can use flag to select specific statistic values:
	e.g # Just the max value.
		csvcut -c 2 Combined_hud.csv | csvstat --max
	    # Just the mean value.
		csvcut -c 2 Combined_hud.csv | csvstat --mean

csvgrep: for filtering tabular data using specific criteria.
  * csvgrep -c 2 -m -9 Combined_hud.csv
     -c (selects specific csvcut column)
     -m (selects specific values for each row)
     -i (selects specific values for each row that do not match the pattern)


