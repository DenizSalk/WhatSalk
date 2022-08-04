import time
import pywhatkit
import keyboard
message = "Message"
list = ["Numbers with list form"]
listleng = str(len(list))
listlengint = len(list)
print("Number of list items: " + listleng + " different numbers are found.")
print("message: " + message + " ||")
i = 0
while (i < listlengint):
    a = list[i]
    print(a)
    pywhatkit.sendwhatmsg_instantly(a, message, 5)
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.press_and_release('ctrl+w')
    i = i + 1


