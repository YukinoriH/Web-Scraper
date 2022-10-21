import PySimpleGUI as pGUI
import webScraper

appTitle = "Web Scraper"

def main():

    pGUI.theme('Light Blue 2')

    inputLayout = [
      [
        [pGUI.Text('Please select the correct excel files')],
        [pGUI.Text('Scrape List:',size=(8,1)),pGUI.Input(), pGUI.FileBrowse(key="-READEXCEL-")],
        [pGUI.Text('Vendor List:',size=(8,1)),pGUI.Input(), pGUI.FileBrowse(key="-VENDORS-")],
        [pGUI.Button('Enter'), pGUI.Button('Cancel')]
      ],
      [
        pGUI.Listbox(values=[], enable_events=True, size=(60, 10), key="-ITEM LIST-")
      ]
    ]

    inputWindow = pGUI.Window(appTitle,inputLayout,resizable = True)

    while True:
        event, values = inputWindow.read(timeout=100)
        if(event == pGUI.WIN_CLOSED or event == 'Cancel'):
            break
        elif (event == 'Enter'):
            if(values["-READEXCEL-"] is None):
                pGUI.popup('Please Enter')
            else:
                excelInput(values["-READEXCEL-"])

    inputWindow.close()

def excelInput(x):
    pGUI.popup('You entered', x)

if __name__ == "__main__":
    main()
