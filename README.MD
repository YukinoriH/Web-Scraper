# Web Scraper

This is a Python application used to export the image link and stock description from a given vendor's website into a .xlsx file.
Initially created to extract the data required to display items for web stores.

![WindowEx1](/images/window_ex1.JPG "Screenshot Example 1")

![WindowEx2](/images/window_ex2.JPG "Screenshot Example 2")

![WindowEx3](/images/window_ex3.JPG "Screenshot Example 3")

This application requires 2 separate excel files requiring the following columns.
* A list of items to scrape:
  * ID
  * Vendor(Website)
  * Part Number(Search Term)
  * Item Name
* A list of Vendors and their website URLs with the html search terms:
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

## Python Libraries Used
* BeautifulSoup
* pandas
* PySimpleGUI
