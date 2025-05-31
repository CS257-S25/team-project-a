# CS257-Team-A

## TD5 Option A:
Code Smells:  
app.py line 14 dead code  
removed the commented out dead code from the old flask app

test_app.py 90 and 100, 177 and 195 and 213 and 230 unnecisary duplicated code  
Removed the duplication of data source creation and mocking and moved it all to each test classes setUp method  
This prevents this code from being in each individual method and makes the code cleaner and easier to understand

## TD5 Option B:

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
