# Review-Validator
This Project is Mainly focused on classifying the restaurent reviews into good and bad. The Steps involved here are
1) Scraping reviews of a restaurent.
2) Classifying them using NLP.

Step 1:Folder base scraping consists of a scrape_nlp.py which scrapes data using BeautifulSoup from the website tripadvisor(https://www.tripadvisor.in/) This file takes any restaurent link from tripadvisor (like https://www.tripadvisor.in/Restaurant_Review-g297588-d12212099-Reviews-Cascades-Visakhapatnam_Visakhapatnam_District_Andhra_Pradesh.html) and scrapes the reviews and stores them in a csv file like reviews.csv The second folder is for scraping the reviews on well known google maps page. The file infinite_scroll.py takes input link of any restaurent from google maps. As google reviews are loaded while scrolling as AJAX (Asynchronous Javascript and XML)is used while writing the code we need selenium library and webdriver for scrolling and while scrolling we scrape the data and save it into a csv file like fresh_stocks.csv.

Step 2: Here we use Bag of words model to process the words of reviews(stemming,removing stop words,etc) of both input and scraped datasets and then we create the bag of words model.Then we train the dataset using any classification model Here we used Kernel SVM.After training we predict the result for previously scraped review set and calculate the positivity percentage. Here we got 59.2%.



