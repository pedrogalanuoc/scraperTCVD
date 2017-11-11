# scraperTCVD
Dataset containing info on 2016 Uab degrees made by scraping techniques, and the python scraper used code itself

## Dataset file history:

v1.0 (12/11/17)

Dataset file complete. It has 139 registers in .CSV format.

## Scraper code history:

v1.0 (12/11/17)

- Added suport to fetch data from Masters type degrees.
- Refined scraping to an upgraded version in some fields to do a best field selection in the page avoiding errors when the page structure has some errors.
- Added delay in webpage download to be polite with the server being crawled.

v1.0b (11/11/17)

The scraper now is able to crawl over the full pages set, and generates the complete .CSV as a result. The dataset generated is added to the repository.

bug fixes:

- Adding support to handle pages with missing values. Now, if a missing value is detected, the scraper puts a "NA" value in the .csv file.
- Minor changes to support minimal format changes on pages.

v0.2a (5/11/17)
Now, the scraper is able to scrape across several webpages and get data from them. 

v0.1a (30/10/17)
In this release, the scraper only gets data from one degree, and has no error controls and can't deal with NA values.
