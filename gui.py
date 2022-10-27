import PySimpleGUI as pGUI
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
        pGUI.Multiline(size=(60, 5), autoscroll=True, horizontal_scroll=False, key="-ITEM LIST-")
      ]
    ]

    inputWindow = pGUI.Window(appTitle,inputLayout,resizable = True)


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
                webScraper.startWebScrape(excelFile[0],vendorFile[0],inputWindow)

    inputWindow.close()

def messageBox(message,Window,type):
    if(type == 0):
        Window["-ITEM LIST-"].print(message)
    else:
        Window["-ITEM LIST-"].update(message)

if __name__ == "__main__":
    main()
