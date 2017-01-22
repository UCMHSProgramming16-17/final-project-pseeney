#I wasn't sure how we were supposed to create a file that would create the graph, so instead I created these files. When the contents of these files are copied and pasted into interactive mode they will create the graphs. 
import bokeh
import requests
import json
# import all needed modules

temp2 = ""
temp3 = ""

def nyc():
    global temp2
    #url and paramaters
    address = 'New York City'
    url1 = "https://maps.googleapis.com/maps/api/geocode/json"
    payload1 = {"key":"AIzaSyBoTmth2T-kwxGh9U5_6qIdUynQvjyildA", "address":str(address)}
    
    #make a request
    r1 = requests.get(url1, params=payload1)
    
    
    #process data
    data = r1.json()
    location = data['results'][0]
    
    geometry = location['geometry']['location']
    
    lat = geometry['lat']
    lon= geometry['lng']
    
    endpoint = 'https://api.darksky.net/forecast/'
    key = '6a91085db4b222e9d433b00a8b05b871'
    
    
    url = endpoint + key + '/' + str(lat) + ', ' + str(lon) #create the url
    
    r = requests.get(url) #request data from the url
    weather = r.json() #convert the data into usable form
    temp2 = weather['currently']['temperature']
    return temp2

def bstn():
    global temp3
    #url and paramaters
    address = 'Boston'
    url1 = "https://maps.googleapis.com/maps/api/geocode/json"
    payload1 = {"key":"AIzaSyBoTmth2T-kwxGh9U5_6qIdUynQvjyildA", "address":str(address)}
    
    #make a request
    r1 = requests.get(url1, params=payload1)
    
    
    #process data
    data = r1.json()
    location = data['results'][0]
    
    geometry = location['geometry']['location']
    
    lat = geometry['lat']
    lon= geometry['lng']
    
    endpoint = 'https://api.darksky.net/forecast/'
    key = '6a91085db4b222e9d433b00a8b05b871'
    
    
    url = endpoint + key + '/' + str(lat) + ', ' + str(lon) #create the url
    
    r = requests.get(url) #request data from the url
    weather = r.json() #convert the data into usable form
    temp3 = weather['currently']['temperature']
    return temp3
    

nyc()
bstn()

from bokeh.models import Title
from bokeh.plotting import figure, show, output_file
#import necessary parts of bokeh

output_file('tempbar.html')
#create and name file which will be created by the code

p = figure(title = "Boston vs NYC Temperature", width=400, height=400)
#create title and size of graph

p.vbar(x=[1.5], width=0.25, bottom=0,
       top=[temp2], color="firebrick", legend = "NYC")
#create bar for NYC, using it's own color and data

p.vbar(x=[1], width=0.25, bottom=0,
       top=[temp3], color="blue", legend = "Boston")
#create bar for Boston, using it's own color and data

p.add_layout(Title(text="City", align="center"), "below")
p.add_layout(Title(text="Temperature (F)", align="center"), "left")
#create x and y axis titles

show(p)
#show the graph