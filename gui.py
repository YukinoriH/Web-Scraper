import PySimpleGUI as pGUI
import threading
import webScraper
import time
import re

appTitle = "Web Scraper"

def main():

    pGUI.theme('Light Blue 2')

    inputLayout = [
      [
        [pGUI.Text('Please select the correct excel files')],
        [pGUI.Text('Scrape List:',size=(8,1)),pGUI.Input(), pGUI.FileBrowse(key="-READEXCEL-")],
        [pGUI.Text('Vendor List:',size=(8,1)),pGUI.Input(), pGUI.FileBrowse(key="-VENDORS-")],
        [pGUI.Button('Enter'), pGUI.Button('Exit')]
      ],
      [
        pGUI.Multiline(size=(30, 10), autoscroll=True, key="-ITEM LIST-")
      ]
    ]

    inputWindow = pGUI.Window(appTitle,inputLayout,resizable = True)
    #threading.Thread(target=errorMsg,args=("",inputWindow),daemon=True).start()

    while True:
        event, values = inputWindow.read(timeout=100)
        if(event == pGUI.WIN_CLOSED or event == 'Exit'):
            break
        elif (event == 'Enter'):
            if(values["-READEXCEL-"] == "" and values["-VENDORS-"] == ""):
                pGUI.popup('Please choose valid Excel files')
            else:
                excelLoc = values["-READEXCEL-"].split("\\")
                excelFile = excelLoc[len(excelLoc)-1].split(".")
                vendorLoc = values["-VENDORS-"].split("\\")
                vendorFile = vendorLoc[len(vendorLoc)-1].split(".")

                errorMsg("Scraping List...",inputWindow)
                webScraper.startWebScrape(excelFile[0],vendorFile[0])
                #threading.Thread(target=webScraper.startWebScrape,args=(excelFile[0],vendorFile[0]),daemon=True).start()
                errorMsg("Completed Scraping List!",inputWindow)

    inputWindow.close()

def errorMsg(error,Window):
    Window["-ITEM LIST-"].print(error)
    #Window.write_event_value("-ITEM LIST-",error)

if __name__ == "__main__":
    main()
