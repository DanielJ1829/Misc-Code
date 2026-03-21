#XML
#stands for extensible markup language
#very scalable so good for software engineering
#great way to hierarchically structure our data
#platform/application independent; if a python file reads in/saves files
#as an xml file, a c++ file can then read in the same xml file to process


#two modules allow us to work with xml, SAX and DOM
#1: SAX - Simple API for XML - mainly used when you have limited memory or very large XML files
# it never loads the full xml file into the ram
# SAX makes it really hard to manipulate xml data; you can only read xml files in using SAX
import xml.sax
#we need 2 things, a handler and a parser
#1 content handler to handle/work with the xml file
#2 parser to translate the file into a python script

#handler = xml.sax.ContentHandler() but this isn't great for customising our handler
#this will just print the names of stuff (10 lines)
'''
class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs): #attrs = attributes btw
        print(name)

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('menu.xml')
'''

class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs): #attrs = attributes btw
        self.current = name
        if self.current == "person":
            print("ID: {}".format(attrs['id']))

    def characters(self, content):
        if self.current == "name":
            self.name = content #content is the 'mike smith' part of the xml file
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print("Name: {}".format(self.name))
        elif self.current == "age":
            print("Age: {}".format(self.age))
        elif self.current == "weight":
            print("Weight: {}".format(self.weight))
        elif self.current == "height":
            print("Height: {}".format(self.height))
        self.current = ""

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('person list.xml')
#2: DOM - Document Object Model

import xml.dom.minidom
#work with 'domtrees' that build a hierarchical structure called a tree, every element/tag in an xml file is a
#branch in that tree
#working with person list:
domtree = xml.dom.minidom.parse('person list2') #domtree; parses the whole xml into our scrip
#tree is now loaded in our ram
group = domtree.documentElement #in 'person list' this is group, in menu it's breakfast menu
#to get a collection of all persons:

#above lines: gets you to the person element, get all elements w/tagname name
#get the first one then get all the child nodes, get the first child node then extract the data from that

#we can manipulate xml files with dom
#need to manipulate it in our script in our ram then export this into the file

'''persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
persons[0].setAttribute('id', '100')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-10"
domtree.writexml(open('person list2.xml', 'w'))'''

newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Paul Jones'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('25'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('90'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('198'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

def remove_whitespace_nodes(node):
    for child in list(node.childNodes):
        if child.nodeType == child.TEXT_NODE and not child.data.strip():
            node.removeChild(child)
        elif child.hasChildNodes():
            remove_whitespace_nodes(child)
remove_whitespace_nodes(domtree)

group.appendChild(newperson) #our domtree is called group, so this appends it to the domtree


with open("person list2", "w", encoding="utf-8") as f:
    domtree.writexml(f, indent="  ", addindent="  ", newl="\n")
    # this gives better formatting than: domtree.writexml(open('person list2.xml', 'w'))

persons = group.getElementsByTagName('person')
#get a collection of all the elements w/tag 'person' saved into an object
for person in persons:
    print("-----PERSON-----")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))

    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))

#what an xml file looks like (menu):
'''
<breakfast_menu>
<food>
<name>Belgian Waffles</name>
<price>$5.95</price>
<description>
Two of our famous Belgian Waffles with plenty of real maple syrup
</description>
<calories>650</calories>
</food>
<food>
<name>Strawberry Belgian Waffles</name>
<price>$7.95</price>
<description>
Light Belgian waffles covered with strawberries and whipped cream
</description>
<calories>900</calories>
</food>
<food>
<name>Berry-Berry Belgian Waffles</name>
<price>$8.95</price>
<description>
Light Belgian waffles covered with an assortment of fresh berries and whipped cream
</description>
<calories>900</calories>
</food>
<food>
<name>French Toast</name>
<price>$4.50</price>
<description>
Thick slices made from our homemade sourdough bread
</description>
<calories>600</calories>
</food>
<food>
<name>Homestyle Breakfast</name>
<price>$6.95</price>
<description>
Two eggs, bacon or sausage, toast, and our ever-popular hash browns
</description>
<calories>950</calories>
</food>
</breakfast_menu>
'''
#another xml file (films):
'''
<CATALOG>
<CD>
<TITLE>Empire Burlesque</TITLE>
<ARTIST>Bob Dylan</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>Columbia</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1985</YEAR>
</CD>
<CD>
<TITLE>Hide your heart</TITLE>
<ARTIST>Bonnie Tyler</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>CBS Records</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1988</YEAR>
</CD>
<CD>
<TITLE>Greatest Hits</TITLE>
<ARTIST>Dolly Parton</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>RCA</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1982</YEAR>
</CD>
<CD>
<TITLE>Still got the blues</TITLE>
<ARTIST>Gary Moore</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>Virgin records</COMPANY>
<PRICE>10.20</PRICE>
<YEAR>1990</YEAR>
</CD>
<CD>
<TITLE>Eros</TITLE>
<ARTIST>Eros Ramazzotti</ARTIST>
<COUNTRY>EU</COUNTRY>
<COMPANY>BMG</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1997</YEAR>
</CD>
<CD>
<TITLE>One night only</TITLE>
<ARTIST>Bee Gees</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>Polydor</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1998</YEAR>
</CD>
<CD>
<TITLE>Sylvias Mother</TITLE>
<ARTIST>Dr.Hook</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>CBS</COMPANY>
<PRICE>8.10</PRICE>
<YEAR>1973</YEAR>
</CD>
<CD>
<TITLE>Maggie May</TITLE>
<ARTIST>Rod Stewart</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>Pickwick</COMPANY>
<PRICE>8.50</PRICE>
<YEAR>1990</YEAR>
</CD>
<CD>
<TITLE>Romanza</TITLE>
<ARTIST>Andrea Bocelli</ARTIST>
<COUNTRY>EU</COUNTRY>
<COMPANY>Polydor</COMPANY>
<PRICE>10.80</PRICE>
<YEAR>1996</YEAR>
</CD>
<CD>
<TITLE>When a man loves a woman</TITLE>
<ARTIST>Percy Sledge</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>Atlantic</COMPANY>
<PRICE>8.70</PRICE>
<YEAR>1987</YEAR>
</CD>
<CD>
<TITLE>Black angel</TITLE>
<ARTIST>Savage Rose</ARTIST>
<COUNTRY>EU</COUNTRY>
<COMPANY>Mega</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1995</YEAR>
</CD>
<CD>
<TITLE>1999 Grammy Nominees</TITLE>
<ARTIST>Many</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>Grammy</COMPANY>
<PRICE>10.20</PRICE>
<YEAR>1999</YEAR>
</CD>
<CD>
<TITLE>For the good times</TITLE>
<ARTIST>Kenny Rogers</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>Mucik Master</COMPANY>
<PRICE>8.70</PRICE>
<YEAR>1995</YEAR>
</CD>
<CD>
<TITLE>Big Willie style</TITLE>
<ARTIST>Will Smith</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>Columbia</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1997</YEAR>
</CD>
<CD>
<TITLE>Tupelo Honey</TITLE>
<ARTIST>Van Morrison</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>Polydor</COMPANY>
<PRICE>8.20</PRICE>
<YEAR>1971</YEAR>
</CD>
<CD>
<TITLE>Soulsville</TITLE>
<ARTIST>Jorn Hoel</ARTIST>
<COUNTRY>Norway</COUNTRY>
<COMPANY>WEA</COMPANY>
<PRICE>7.90</PRICE>
<YEAR>1996</YEAR>
</CD>
<CD>
<TITLE>The very best of</TITLE>
<ARTIST>Cat Stevens</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>Island</COMPANY>
<PRICE>8.90</PRICE>
<YEAR>1990</YEAR>
</CD>
<CD>
<TITLE>Stop</TITLE>
<ARTIST>Sam Brown</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>A and M</COMPANY>
<PRICE>8.90</PRICE>
<YEAR>1988</YEAR>
</CD>
<CD>
<TITLE>Bridge of Spies</TITLE>
<ARTIST>T'Pau</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>Siren</COMPANY>
<PRICE>7.90</PRICE>
<YEAR>1987</YEAR>
</CD>
<CD>
<TITLE>Private Dancer</TITLE>
<ARTIST>Tina Turner</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>Capitol</COMPANY>
<PRICE>8.90</PRICE>
<YEAR>1983</YEAR>
</CD>
<CD>
<TITLE>Midt om natten</TITLE>
<ARTIST>Kim Larsen</ARTIST>
<COUNTRY>EU</COUNTRY>
<COMPANY>Medley</COMPANY>
<PRICE>7.80</PRICE>
<YEAR>1983</YEAR>
</CD>
<CD>
<TITLE>Pavarotti Gala Concert</TITLE>
<ARTIST>Luciano Pavarotti</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>DECCA</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1991</YEAR>
</CD>
<CD>
<TITLE>The dock of the bay</TITLE>
<ARTIST>Otis Redding</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>Stax Records</COMPANY>
<PRICE>7.90</PRICE>
<YEAR>1968</YEAR>
</CD>
<CD>
<TITLE>Picture book</TITLE>
<ARTIST>Simply Red</ARTIST>
<COUNTRY>EU</COUNTRY>
<COMPANY>Elektra</COMPANY>
<PRICE>7.20</PRICE>
<YEAR>1985</YEAR>
</CD>
<CD>
<TITLE>Red</TITLE>
<ARTIST>The Communards</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>London</COMPANY>
<PRICE>7.80</PRICE>
<YEAR>1987</YEAR>
</CD>
<CD>
<TITLE>Unchain my heart</TITLE>
<ARTIST>Joe Cocker</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>EMI</COMPANY>
<PRICE>8.20</PRICE>
<YEAR>1987</YEAR>
</CD>
</CATALOG>
'''