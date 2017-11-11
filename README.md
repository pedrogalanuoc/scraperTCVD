# scraperTCVD
Dataset containing info on 2016 Uab degrees made by scraping techniques, and the python scraper used code itself

v0.1a
In this release, the scraper only gets data from one degree, and has no error controls and can't deal with NA values.

v0.2a 
Now, the scraper is able to scrape across several webpages and get data from them. 

v1.0b (11/11/17)

The scraper now is able to crawl over the full pages set, and generates the complete .CSV as a result. The dataset generated is added to the repository

bug fixes:

- Adding support to handle pages with missing values. Now, if a missing value is detected, the scraper puts a "NA" value in the .csv file
- Minor changes to support minimal format changes on pages
