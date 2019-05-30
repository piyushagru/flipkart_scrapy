# Mobile-Scraper

This scraper can be used to scrap data from Flipkart, using this spider we can scrap Mobile name, their price and their rating.

## Steps

To use this scraper clone this repo and run below commands in your command promt.

Command to store data in json format
```
scrapy crawl flipkart_spider -o mi_phone.json
```
Command to store data in csv format
```
scrapy crawl flipkart_spider -o mobile.csv
```


## Requirements
```
pip install scrapy
```