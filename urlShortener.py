#I use a virtual environment to callout the library of requests
import requests

#function for the parameters
def shorten_Link(fullLink, linkName):

    #This is an API generated in cutt.ly
    APIkey = 'c68fc2d0a74f7d9cb9e6738b5286df2a6d6c7'

    #This is the base url for the urlshortener
    BASEurl = 'https://cutt.ly/api/api.php'
    
   #create dictionary for the payLoad
    payLoad = {'key':APIkey, 
               'short':fullLink, 
               'name':linkName}
    
    #using the requests library
    request = requests.get(BASEurl, params=payLoad)
    data = request.json()
    
    print('')
    
    #conditions
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        
        print('Title: ', title)
        print('Link: ', short_link)
    except:
        status = data['url']['status']
        print('Error! The status error: ', status)
        
while True:
    
    user_loop = input("\nDo you want to shorten a hyperlink?(y/n)?: ")
    
    #added user input
    if user_loop == 'y':
        print("<<==================================>>")
        link = input('Enter a link to shorten: >> ')
        name = input('\nGive a name to the link: >> ')
        print("<<==================================>>")
        print("Below is the Title and the new URL")
        #execute command
        shorten_Link(link, name)
    
    if user_loop == 'n':
        break
    

            
        