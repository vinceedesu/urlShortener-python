#I use a virtual environment to callout the library of requests
import requests

#function for the parameters
def shortenLink(fullLink, linkName):

    #This is an API generated in cutt.ly
    APIkey = 'c68fc2d0a74f7d9cb9e6738b5286df2a6d6c7'

    #This is the base url for the urlshortener
    BASEurl = 'https://cutt.ly/api/api.php'
    
   #create dictionary for the payLoad
    payLoad = {'key':APIkey, 
               'short':fullLink, 
               'name':linkName}