url = "https://en.wikipedia.org/wiki/World_population"
import pandas as pd
dataframe_list = pd.read_html(url, flavor='bs4')  #this only extracts tables from websites by design
#print(dataframe_list)    #this extracts all the tables from the website
print(dataframe_list[5])

#also, we can use the match argument
x =pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
print(type(x))
