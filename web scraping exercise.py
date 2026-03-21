import requests  #lets you download a webpage
from bs4 import BeautifulSoup
import warnings
warnings.simplefilter("ignore")

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
#print(soup.prettify())   #puts the html in a nested structure

#First, the document is converted to Unicode, (similar to ASCII), and HTML entities are converted to Unicode characters.
#Beautiful Soup transforms a complex HTML document into a complex tree of Python objects.
#The BeautifulSoup object can create other types of objects
#This looks at BeautifulSoup and Tag objects that here we say are identical, and NavigableString objects.


tag_object = soup.title
#print("tag object type:", type(tag_object))
#If there is more than one Tag with the same name, the first element with that Tag name is called, this corresponds to the most paid player

tag_object = soup.h3
tag_child = tag_object.b  #lebron
parent_tag = tag_child.parent
sibling_1 = tag_object.next_sibling #lebrons salary
sibling_2 = sibling_1.next_sibling #stephen curry
sibling_3 = sibling_2.next_sibling.string   #his salary
#print(tag_child['id'], tag_child.attrs)
tag_string=tag_child.string
unicode_string = str(tag_object)
#print(unicode_string)

html_table="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"
table = BeautifulSoup(html_table, "html.parser")

#The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.
#The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)

table_rows=table.find_all('tr')
first_row = table_rows[0]
print(first_row)
print(first_row.td, first_row.td.next_sibling)

#As row is a cell object, we can apply the method find_all to it and extract table cells in the object cells using
#the tag td, this is all the children with the name td. The result is a list,
# each element corresponds to a cell and is a Tag object, we can iterate through this list as well.
# We can extract the content using the string attribute.
'''for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print("column",j,"cell",cell.string)
list_input=table.find_all(name=["tr", "td"])
#print(table.find_all(id="flight"))
print(table.find_all('a', href=True))
print(soup.find_all(id = 'boldest'))
table_bs.find_all(string="Florida")'''

'''two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
table2 = BeautifulSoup(two_tables, 'html.parser')
x=table2.find("table", class_= 'pizza')
print(x.text)


#extracting data from a website:

url = "https://web.archive.org/web/20230224123642/https://www.ibm.com/us-en/"
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

for link in soup.find_all('a', href=True):
    print(link.get('href'))
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))'''

import pandas as pd
url = "https://en.wikipedia.org/wiki/World_population"
data  = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
tables = soup.find_all('table')
print(len(tables))
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
#print(tables[table_index].prettify().strip())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if col:
        rank = col[0].text.strip()
        country = col[1].text.strip()
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()

        # Create a temporary DataFrame for the new row
        new_row = pd.DataFrame([{"Rank": rank, "Country": country, "Population": population, "Area": area, "Density": density}])

        # Use concat
        population_data = pd.concat([population_data, new_row], ignore_index=True)
print(population_data)
#we can use the read_html function to create a DataFrame.
#Remember the table we need is located in tables[table_index]
#We can now use the pandas function read_html and give it the string version
#of the table as well as the flavor which is the parsing engine bs4

pd.read_html(str(tables[5]), flavor='bs4')  #always returns a list of data frames so you need to pick
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

print(population_data_read_html)

dataframe_list = pd.read_html(url, flavor='bs4')