import vendorObj
import pandas
import requests
import sys
from bs4 import BeautifulSoup

availableVendors = []

def main(fileName):
    excelFile = pandas.ExcelFile(fileName + ".xlsx")
    excelDF = pandas.read_excel(excelFile)
    #createVendorList()
    readAndCreateExcelFile(excelDF)

def createVendorList():
    obj1 = vendorObj("NAPOLEON","https://www.napoleon.com","https://www.napoleon.com/en/ca/barbecues/product-search?search= _xxx_&sort=search_api_relevance&order=desc")
    obj1.searchBarElements("main","link-wrapper","view-card select-item")
    obj1.itemPageElements("image-wrapper mobile","data-src","description","p")
    
    obj2 = vendorObj("COLUMBIA SPORTSWEAR CO.","https://www.columbiasportswear.ca","https://www.columbiasportswear.ca/en/search?q=_xxx_&lang=en_CA&searchMethod=manualSearch&pos=0")
    obj3 = vendorObj("HELLY HANSEN","https://www.hellyhansen.com","https://www.hellyhansen.com/en_ca/catalogsearch/result/?q=_xxx_&ct=regular_search")
    obj4 = vendorObj("TIMBERLAND","https://www.timberland.ca","https://www.timberland.ca/shop/VFSearchDisplay?catalogId=10102&storeId=7121&langId=-12&searchTerm=_xxx_")

    availableVendors.append(obj1)
    availableVendors.append(obj2)
    availableVendors.append(obj3)
    availableVendors.append(obj4)

def webScrapeItem(searchNum):
    itemPage = scrapeSearch(searchNum)
    return(scrapeItemPage(itemPage))

def scrapeSearch(searchNum, Vendor):
    URL = "NAPOLEON": "https://www.napoleon.com/en/ca/barbecues/product-search?search=" + searchNum + "&sort=search_api_relevance&order=desc",
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id = "main")
    job_elements = results.find_all("div", class_ = "link-wrapper")
    for job_element in job_elements:
        findURL = job_element.find("a",class_ = "view-card select-item")
        productURL = findURL["href"]
        return("https://www.napoleon.com" + productURL)

def scrapeItemPage(itemURL):
    imgAndDesc = ["",""]
    try:
        page = requests.get(itemURL)
    except:
        return imgAndDesc
    soup = BeautifulSoup(page.content, "html.parser")

    imageTag = soup.find('div', class_="image-wrapper mobile")
    image = imageTag.find('img')
    try:
        imgAndDesc[0] = (image['data-src'])
    except:
        return imgAndDesc
    descTag = soup.find('section', class_="description")
    try:
        imgAndDesc[1] = (descTag.find('p'))
    except:
        return imgAndDesc

    return imgAndDesc

def readAndCreateExcelFile(excelDF):

    progress = 0
    reportLength = len(excelDF)
    loadingBar(progress,reportLength)

    IDArray,DisplayName,PartNumber,VendorArray,imageURLArray,DescArray = ([] for i in range(6))
    imgAndDesc = []
    for index, row in excelDF.iterrows():
        IDArray.append(row['Internal ID'])
        VendorArray.append(row['Vendor'])
        DisplayName.append(row['Display Name'])
        PartNumber.append(row['Part Number'])
        imgAndDesc = webScrapeItem(row['Part Number'],row['Vendor'])
        imageURLArray.append(imgAndDesc[0])
        DescArray.append(imgAndDesc[1])
        progress = 1 + progress
        loadingBar(progress,reportLength)

    createOutputFile(IDArray,DisplayName,PartNumber,VendorArray,imageURLArray,DescArray)

#Cretes an Excel file with a list of all items with new Display names
def createOutputFile(IDArray,DisplayName,PartNumber,VendorArray,imageURLArray,DescArray):
    d1 = {'Vendor': VendorArray, 'Display Name': DisplayName,'New Name': PartNumber, 'Image': imageURLArray, 'Description': DescArray}
    DF1 = pandas.DataFrame(data=d1,index = IDArray)

    with pandas.ExcelWriter("WebScrapedItems.xlsx") as writer:
        DF1.to_excel(writer,sheet_name="UpdatedList")

#Loading bar taken from stack overflow
def loadingBar(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

if __name__ == "__main__":
    main(sys.argv[1])
