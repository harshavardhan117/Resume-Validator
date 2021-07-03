# Review-Validator
The aim of this project is to classify the reviews into good or bad. Mainly focused on restaurant reviews. 

First folder i.e base_scraping consists of 2 files scrape_nlp.py and reviews.csv. scrape_nlp.py contains the python code to extract the reviews of a particular hotel from the website(https://www.tripadvisor.in/).
For ex:(https://www.tripadvisor.in/Restaurant_Review-g297588-d12212099-Reviews-Cascades-Visakhapatnam_Visakhapatnam_District_Andhra_Pradesh.html). The other csv file contains reviews scraped from the website.

The second folder i.e Scrape_selenium consists of 3 files infinite_reviews.py which consists of python code where Selenium library is used, Since google reviews are loaded as we
scroll down (using Jquery) so we have to use selenium functions to scroll the data using css selector. Note:the code does not work without chromedriver.exe file in the base folder 
where you are executing py file.The other csv file consists of all the reviews.


Now we have to use the reviews from either of the methods and process them using final.ipynb



