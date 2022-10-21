import vendorObj
import ExcelReadWrite
import pandas
import requests
import sys
from bs4 import BeautifulSoup

def main(fileName):
    excelFile = ExcelReadWrite.readExcelFile(fileName)
    vendorDF = ExcelReadWrite.readExcelFile("vendorList")
    vendorList = createVendorList(vendorDF)
    readAndCreateExcelFile(excelFile,vendorList)

def createVendorList(vendorDF):
    availableVendors = []
    for index, vendor in vendorDF.iterrows():
        tempVendorObj = vendorObj(index['Vendor'],index['Website'],index['SearchURL'])
        tempVendorObj.searchBarElements(index['searchID'],index['searchWrapper'],index['searchItem'])
        tempVendorObj.itemPageElements(index['imageWrapper'],index['imageSrc'],index['descWrapper'],index['descSrc'])
        availableVendors.append(tempVendorObj)

'''
Using the website's serach methods, finds the most relevant item given the parameter.
Always takes the first item from the results. Returns the item page
From the item page, finds and returns the item image and description as a list.
list[0] -> Image & list[1] -> Description.
Any errors return empty elements in the list
'''
def webScrapeItem(searchNum,scrapeData):
    requestURL = self.venURL.replace("_xxx_",searchNum)
    requestPage = requests.get(requestURL)
    pageContent = BeautifulSoup(requestPage.content, "html.parser")

    results = pageContent.find(id = self.searchID)
    job_elements = results.find_all("div", class_ = self.searchWrapper)
    for job_element in job_elements:
        findURL = job_element.find("a",class_ = self.searchItem)
        productURL = findURL["href"]
        itemURL = (self.venWebsite + productURL)

    imgAndDesc = ["",""]
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

def readAndCreateExcelFile(excelDF,vendorList):

    IDArray,DisplayName,PartNumber,VendorArray,imageURLArray,DescArray = ([] for i in range(6))
    imgAndDesc = []
    for index, row in excelDF.iterrows():
        IDArray.append(row['Internal ID'])
        VendorArray.append(row['Vendor'])
        DisplayName.append(row['Display Name'])
        PartNumber.append(row['Part Number'])
        # scrapeData = vendorList.loc[df['Vendor'] == row['Vendor']]
        imgAndDesc = webScrapeItem(row['Part Number'],scrapeData)
        imageURLArray.append(imgAndDesc[0])
        DescArray.append(imgAndDesc[1])

    dataDict = {'Vendor': VendorArray, 'Display Name': DisplayName,'New Name': PartNumber, 'Image': imageURLArray, 'Description': DescArray}
    ExcelReadWrite.writeExcelFile(IDArray,dataDict,"WebScrapedItems","UpdatedList")


if __name__ == "__main__":
    main(sys.argv[1])
