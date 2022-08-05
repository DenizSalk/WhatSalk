import time
import pywhatkit
import keyboard
import PySimpleGUI as sg
import pandas as pd
sg.theme('DarkGreen2')
layout = [

          [sg.Column([[sg.Image(filename='WHATSALK.png')]],justification='center')],
          [sg.Text('Mesajınızı Girin'), sg.Text(size=(15,1))],
          [sg.InputText(size=(35, 3))],
          [sg.Column([[sg.FileBrowse(key="2")],[sg.Button('Tamam')]],justification='center')]]

window = sg.Window("WhatSalk", icon='icon.ico').Layout(layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Tamam':
        break
event, values = window.read()
window.close()

message = str(values[1])
df_sheet_all = pd.read_excel(values['2'], sheet_name=None)
print(df_sheet_all)
mylist = df_sheet_all['Telefon'].values.tolist()
print(mylist)
listlengint = len(mylist)
print("Numara Sayısı: " + str(listlengint) )
print("Mesaj " + message)
i = 0


while (i < listlengint):
    print(mylist[i])
    a = mylist[i]
    correcta = "+90" + str(mylist[i])
    pywhatkit.sendwhats_image( correcta, "fairy.jpg", "Yazılı test")
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.press_and_release('ctrl+w')
    i = i + 1
    time.sleep(0.5)


