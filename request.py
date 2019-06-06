# We are going to request the server for the predictions.

#import  packages
import requests

#set url for localhost
url = 'http://localhost:5000/api'

# you can use the url when deployed in the online server
url2 = "http://djangoposts.pythonanywhere.com/api"

#send request
experince = input("write year of experience:")

r = requests.post(url2,json={'exp':float(experince),})

#print result
print("Your salaray is $ {}".format(r.json()))
