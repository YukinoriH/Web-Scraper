import vendorObj
import ExcelReadWrite
import gui
import time
import threading
import pandas
import requests
import sys
import os
from bs4 import BeautifulSoup

def startWebScrape(fileName,vendorList,inputWindow):
    excelFile = ExcelReadWrite.readExcelFile(fileName)
    vendorDF = ExcelReadWrite.readExcelFile(vendorList)
    vendorList = createVendorList(vendorDF)
    threading.Thread(target=readAndCreateExcelFile,args=(excelFile,vendorList,inputWindow),daemon=True).start()

def searchVendorList(vendor,vendorList):
    for ven in vendorList:
        if(ven.venName == vendor):
            return ven
    return -1

def createVendorList(vendorDF):
    availableVendors = []
    for index, vendor in vendorDF.iterrows():
        availableVendors.append(vendorObj.VendorObject(
                                            vendor['Vendor'],
                                            vendor['Website'],
                                            vendor['SearchURL'],
                                            vendor['searchID'],
                                            vendor['searchWrapper'],
                                            vendor['searchItem'],
                                            vendor['imageWrapper'],
                                            vendor['imageSrc'],
                                            vendor['descWrapper'],
                                            vendor['descSrc']
                                        ))
    return availableVendors

'''
Using the website's serach methods, finds the most relevant item given the parameter.
Always takes the first item from the results. Returns the item page
From the item page, finds and returns the item image and description as a list.
list[0] -> Image & list[1] -> Description.
Any errors return empty elements in the list
'''
def webScrapeItem(searchNum,scrapeData):
    imgAndDesc = ["",""]
    requestURL = scrapeData.venURL.replace("_xxx_",searchNum)
    requestPage = requests.get(requestURL)
    pageContent = BeautifulSoup(requestPage.content, "html.parser")

    results = pageContent.find(id = scrapeData.searchID)
    job_elements = results.find_all("div", class_ = scrapeData.searchWrapper)
    for job_element in job_elements:
        findURL = job_element.find("a",class_ = scrapeData.searchItem)
        productURL = findURL["href"]
        itemURL = (scrapeData.venWebsite + productURL)

    try:
        page = requests.get(itemURL)
    except:
        return imgAndDesc
    soup = BeautifulSoup(page.content, "html.parser")

    imageTag = soup.find('div', class_= scrapeData.imageWrapper)
    image = imageTag.find('img')
    try:
        imgAndDesc[0] = (image[scrapeData.imageSrc])
    except:
        return imgAndDesc
    descTag = soup.find('section', class_= scrapeData.descWrapper)
    try:
        imgAndDesc[1] = (descTag.find(scrapeData.descSrc))
    except:
        return imgAndDesc

    return imgAndDesc

def readAndCreateExcelFile(excelDF,vendorList,inputWindow):

    IDArray,DisplayName,PartNumber,VendorArray,imageURLArray,DescArray = ([] for i in range(6))
    imgAndDesc = []
    Max = len(excelDF)
    Min = 0

    for index, row in excelDF.iterrows():
        Min = Min + 1
        gui.messageBox(progressBar(Min,Max),inputWindow,1)
        IDArray.append(row['Internal ID'])
        VendorArray.append(row['Vendor'])
        DisplayName.append(row['Display Name'])
        PartNumber.append(row['Part Number'])

        scrapeData = searchVendorList(row['Vendor'],vendorList)
        if(scrapeData == -1):
            imgAndDesc = ["",""]
        else:
            imgAndDesc = webScrapeItem(row['Part Number'],scrapeData)
            #imgAndDesc = ["",""]

        imageURLArray.append(imgAndDesc[0])
        DescArray.append(imgAndDesc[1])

    dataDict = {'Vendor': VendorArray, 'Display Name': DisplayName,'Part Number': PartNumber, 'Image': imageURLArray, 'Description': DescArray}
    ExcelReadWrite.writeExcelFile(IDArray,dataDict,"WebScrapedItems","UpdatedList")
    gui.messageBox("Completed Scraping!",inputWindow,0)

def progressBar(count, total):
    barLength = 50
    filled = int(round(barLength * count / float(total)))
    percent = round(100.0 * count / float(total), 1)
    bar = '|' * filled + '-' * (barLength - filled)
    return('%s%s...[%s]\r\n' % (percent, '%', bar))
