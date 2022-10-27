import pandas

#Read Excel File and returns DataFrame
def readExcelFile(excelInput):
    try:
        excelFile = pandas.ExcelFile(excelInput + ".xlsx")
    except FileNotFoundError as excelErr:
        return excelErr #TODO return proper error

    excelDF = pandas.read_excel(excelFile)
    return(excelDF)

#Creates Excel File using data from dictionary (EX: dataDict = { ColumnName : Everything under column as a list, ....})
def writeExcelFile(indexArray,dataDict,excelOutput,sheetName):
    try:
        ExcelDataFrame = pandas.DataFrame(data = dataDict,index = indexArray)
    except Exception as e:
        return None #TODO return proper error

    with pandas.ExcelWriter(excelOutput + ".xlsx") as writer:
        ExcelDataFrame.to_excel(writer,sheet_name = sheetName)
