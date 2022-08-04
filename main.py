import time
import pywhatkit
import keyboard
message = "Whatsalk cümleten iyi geceler diler. Bu gecelik son mesajım. Mis gibi çalışıyor. Bayramda toplu tebrik hizmetim de olacak. https://www.youtube.com/watch?v=gunZ49SGLg8"
list = ["+90 532 391 81 54","+90 553 334 34 92","+90 542 543 34 91"]
listleng = str(len(list))
listlengint = len(list)
print("listede " + listleng + " farklı numara bulunmaktadır.")
print("mesajınız: " + message + " || doğru yazdığından emin ol")
i = 0
while (i < listlengint):
    a = list[i]
    print(a)
    pywhatkit.sendwhatmsg_instantly(a, message, 5)
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.press_and_release('ctrl+w')
    i = i + 1


