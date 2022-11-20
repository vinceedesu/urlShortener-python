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
        
        print("Below is the Title and the new URL")
        print('\nTitle: ', title)
        print('New Link: ', short_link)
    except:
        status = data['url']['status']
        
        #updated the condition status error di ko nasama ito sa demo pero pahabol lang sir thank u po
        if status == 1:
            print('Error! The status error: ', status, ' >> The shortened link comes from the domain that shortens the link')
        elif status == 2:
            print('Error! The status error: ', status,' >> The entered link is not a link')
        elif status == 3:
            print('Error! The status error: ', status,' >> The preferred link name / alias is already taken')
        elif status == 4:
            print('Error! The status error: ', status,' >> Invalid API key')
        elif status == 5:
            print('Error! The status error: ', status,' >> The link has not passed the validation. Includes invalid characters')
        elif status == 6:
            print('Error! The status error: ', status,' >> The link provided is from a blocked domain')
        else:
            print('Uknown Error!')
        
while True:
    
    user_loop = input("\nDo you want to shorten a hyperlink?(y/n)?: ")
    
    #added user input
    if user_loop == 'y':
        print("\n<<==================================>>")
        link = input('\nEnter a link to shorten: >> ')
        name = input('\nGive a name to the link: >> ')
        print("\n<<==================================>>")
        #execute command
        shorten_Link(link, name)
    
    if user_loop == 'n':
        break
    

            
        