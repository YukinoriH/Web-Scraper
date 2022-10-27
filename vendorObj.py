class VendorObject:

    #Defines html elements required to choose item after a search is conducted
    #Defines html elements required to get the image and descripton on an item page
    def __init__(self,venName,venWebsite,venURL,searchID,searchWrapper,searchItem,imageWrapper,imageSrc,descWrapper,descSrc):
        self.venName = venName
        self.venWebsite = venWebsite
        self.venURL = venURL
        self.searchID = searchID
        self.searchWrapper = searchWrapper
        self.searchItem = searchItem
        self.imageWrapper = imageWrapper
        self.imageSrc = imageSrc
        self.descWrapper = descWrapper
        self.descSrc = descSrc
