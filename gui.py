import PySimpleGUI as pGUI
import webScraper
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
        pGUI.Output(size=(30, 10), key="-ITEM LIST-")
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

                webScraper.startWebScrape(excelFile[0],vendorFile[0])
                #for i in range(1,10000):
                    #pGUI.one_line_progress_meter('My Meter', i+1, 10000, 'key','Optional message')

    inputWindow.close()

def progressMeter(cur,end):
    pGUI.one_line_progress_meter('My Meter', cur, end, 'key','Optional message')

if __name__ == "__main__":
    main()
