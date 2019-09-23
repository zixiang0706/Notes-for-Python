from PIL import Image
from pytesseract import image_to_string
import pyautogui
import time

img = Image.open("asset/test1.png")
text = image_to_string(img)
print(text)
img = pyautogui.screenshot(region=(438*2, 194*2, 140, 40))
# img.show()

while True:
    time.sleep(0.2)
    img = pyautogui.screenshot(region=(438 * 2, 194 * 2, 140, 40))
    text = image_to_string(img)
    print(text)

