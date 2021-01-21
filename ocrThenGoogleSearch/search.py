import sys
import webbrowser

search = sys.argv[1]
url = "https://www.google.com.tr/search?q={}".format(search) #Designed for Google search. Can be changed to Bing/DuckDuckGo if necessary
b = webbrowser.get('chrome') #Used Chrome, can also be changed into firefox,safari
b.open(url)
