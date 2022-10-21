import requests
from bs4 import BeautifulSoup

class VendorObject:

    def __init__(self,venName,venWebsite,venURL):
        self.venName = venName
        self.venWebsite = venWebsite
        self.venURL = venURL
        self.searchID = ""
        self.searchWrapper = ""
        self.searchItem = ""
        self.imageWrapper = ""
        self.imageSrc = ""
        self.descWrapper = ""
        self.descSrc = ""

    #Defines html elements required to choose item after a search is conducted
    def searchBarElements(self,searchID,searchWrapper,searchItem):
        self.searchID = searchID
        self.searchWrapper = searchWrapper
        self.searchItem = searchItem

    #Defines html elements required to get the image and descripton on an item page
    def itemPageElements(self,imageWrapper,imageSrc,descWrapper,descSrc):
        self.imageWrapper = imageWrapper
        self.imageSrc = imageSrc
        self.descWrapper = descWrapper
        self.descSrc = descSrc
