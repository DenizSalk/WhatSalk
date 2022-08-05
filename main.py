import time
import pywhatkit
import keyboard
import PySimpleGUI as sg
import pandas as pd
sg.theme('Blue')
layout = [

          [sg.Column([[sg.Image(filename='icon.png')]],justification='center')],
          [sg.Text('Mesajınızı Girin'), sg.Text(size=(15,1))],
          [sg.InputText()],
          [sg.FileBrowse(key="2")],
          [sg.Button('Tamam')]]

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
mylist = df_sheet_all['Telefon'].tolist()
print(mylist)
listlengint = len(mylist)
print("Numara Sayısı: " + str(listlengint) )
print("Mesaj " + message)
i = 0
while (i < listlengint):
    print(mylist[i])
    a = mylist[i]
    correcta = "+" + mylist[i]
    pywhatkit.sendwhatmsg_instantly(correcta, message, 5)
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.press_and_release('ctrl+w')
    i = i + 1


