
import requests
from bs4 import BeautifulSoup

class VendorObject:

    def __init__(self,venName,venWebsite,venURL):
        self.venName = venName
        self.venWebsite = venWebsite
        self.venURL = venURL
        self.searchNum = ""
        self.searchWrapper = ""
        self.searchItem = ""
        self.imageWrapper = ""
        self.imageSrc = ""
        self.descWrapper = ""
        self.descSrc = ""

    #Defines html elements required to choose item after a search is conducted
    def searchBarElements(self,searchID,searchWrapper,searchItem):
        self.searchNum = searchID
        self.searchWrapper = searchWrapper
        self.searchItem = searchItem

    #Defines html elements required to get the image and descripton on an item page
    def itemPageElements(self,imageWrapper,imageSrc,descWrapper,descSrc):
        self.imageWrapper = imageWrapper
        self.imageSrc = imageSrc
        self.descWrapper = descWrapper
        self.descSrc = descSrc

    #Using the website's serach methods, finds the most relevant item given the parameter.
    #Always takes the first item from the results. Returns the item page
    def searchBarScrape(self,searchNum):
        requestURL = self.venURL.replace("_xxx_",searchNum)
        requestPage = requests.get(requestURL)
        pageContent = BeautifulSoup(requestPage.content, "html.parser")

        results = pageContent.find(id = self.searchNum)
        job_elements = results.find_all("div", class_ = self.searchWrapper)
        for job_element in job_elements:
            findURL = job_element.find("a",class_ = self.searchItem)
            productURL = findURL["href"]
            return(self.venWebsite + productURL)

    #From the item page, finds and returns the item image and description as a list.
    #list[0] -> Image & list[1] -> Description.
    #Any errors return empty elements in the list
    def itemPageScrape(self,searchNum):
        imgAndDesc = ["",""]
        itemURL = venURL.replace("_xxx_",searchNum)
        try:
            page = requests.get(itemURL)
        except:
            return imgAndDesc
        soup = BeautifulSoup(page.content, "html.parser")

        imageTag = soup.find('div', class_= self.imageWrapper)
        image = imageTag.find('img')
        try:
            imgAndDesc[0] = (image[self.imageSrc])
        except:
            return imgAndDesc
        descTag = soup.find('section', class_= self.descWrapper)
        try:
            imgAndDesc[1] = (descTag.find(self.descSrc))
        except:
            return imgAndDesc

        return imgAndDesc
