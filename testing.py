from vendorObj import *
import webScraper
import requests
from bs4 import BeautifulSoup

availableVendors = []

def main():
    testInput = "C:\\Users\\yhayashi\\Documents\\Yuki's Folder\\Python\\Web Scraper\\itemList.xlsx"
    fileLoc = testInput.split("\\")
    inputFile = fileLoc[len(fileLoc)-1].split(".")
    print(inputFile[0])
    webScraper.startWebScrape(inputFile[0])
    #createVendorList()
    #test = availableVendors[0]
    #temp = test.searchBarScrape("55015")


#Tests if the correct item data is given and recieved
def testCase1():
    return None

#Test if inaccurate item data returns the correct errors
def testCase2():
    return None

def createVendorList():
    obj1 = VendorObject("NAPOLEON","https://www.napoleon.com","https://www.napoleon.com/en/ca/barbecues/product-search?search= _xxx_&sort=search_api_relevance&order=desc")
    obj1.searchBarElements("main","link-wrapper","view-card select-item")
    obj1.itemPageElements("image-wrapper mobile","data-src","description","p")
    availableVendors.append(obj1)
    '''
    obj2 = vendorObj("COLUMBIA SPORTSWEAR CO.","https://www.columbiasportswear.ca","https://www.columbiasportswear.ca/en/search?q=_xxx_&lang=en_CA&searchMethod=manualSearch&pos=0")
    availableVendors.append(obj2)

    obj3 = vendorObj("HELLY HANSEN","https://www.hellyhansen.com","https://www.hellyhansen.com/en_ca/catalogsearch/result/?q=_xxx_&ct=regular_search")
    availableVendors.append(obj3)

    obj4 = vendorObj("TIMBERLAND","https://www.timberland.ca","https://www.timberland.ca/shop/VFSearchDisplay?catalogId=10102&storeId=7121&langId=-12&searchTerm=_xxx_")
    availableVendors.append(obj4)
    '''

if __name__ == "__main__":
    main()
