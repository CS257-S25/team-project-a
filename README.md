# CS257-Team-A

## TD5 Option A:
Code Smells:  
app.py line 14 dead code  
removed the commented out dead code from the old flask app

test_app.py 90 and 100, 177 and 195 and 213 and 230 unnecisary duplicated code  
Removed the duplication of data source creation and mocking and moved it all to each test classes setUp method  
This prevents this code from being in each individual method and makes the code cleaner and easier to understand  

I also added a singleton data source meta class in order to prevent the code smell of unnesisary creation of data source objects.  
To do this I added a singleton meta class in singleton_meta.py.  

Fixed docsrings to all be truthful about method functions specificly in app 110 and 123 

Fixing of typos in various files.  

## TD5 Option B:

The drug sale arrest page would cause a python error when non numbers or nothing was input to the form. So in the drug sale arrest page I added on lines 65 and 67 better descripions for the input labels on the form. Adidionaly I made it so the form only takes integers and it will not cause an error when it is submited without any passed in parameters. This was all done in the sell_arrests.html page. 

When people were testing the page they had lots of trouble knowing what information each of the pages contained. In all of the pages HTML at line 26 on the main navigation bar I changed the name of Data Overview to Graph and also on the homepage at line 56 I changed the name of info to data overview so that it is easier for people to know where the information about the database is and also so the place where you can draw conclusions from the data is more clear as it is now called graph which is more likely to invoke a feeling of comparison in the user.  

## Scanability

The website has a main heading that tells the user what site they are on and is immediately obvious what information is is meant to give them. Adidionaly there are navigation buttons at the top so the user doesnt have to think how to navigate arround the page. 

## Satisficing

There are not too many options for things to do on the page with only the navigation bar being interactable. This makes it so the user will at least get to an interesting page even if they don't click on the page they wanted to reach first. 

## Muddling through

There is information for how to use the site on the main page but it is not necissary to read it to navigate the site. This is because the user does not have to find the best way to navigate as there are only a few buttons that they need to use and they all have fairly self explanatory names.

Usage in the command line:  
python3 cl.py --meeting-frequency  
python3 cl.py --meeting-count  
python3 cl.py --sellArrests lowerBoundCount upperBoundCount  
eg. python3 cl.py --sellArrests 1 3  

Database copy command: \copy drug_data FROM 'Data/smallData.csv' DELIMITER ',' CSV
