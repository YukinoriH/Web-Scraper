# Web Scraper

This is a web scraper used to export the image link and stock description into an excel file.

![WindowEx1](/images/window_ex1.jpg "Screenshot Example")

This application requires 2 separate excel files with the following columns.
* A list of items to scrape:
  * ID
  * Vendor(Website)
  * Part Number(Search Term)
  * Name
* A list of Vendors and their website URLs:
  * Vendor Name
  * Website
  * SearchURL
  * SearchID
  * SearchWrapper
  * SearchItem
  * ImageWrapper
  * ImageSrc
  * DescWrapper
  * DescSrc

##Python Libraries Used
* BeautifulSoup
* pandas
* PySimpleGUI
