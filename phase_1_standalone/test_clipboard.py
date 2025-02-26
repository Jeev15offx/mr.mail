import pyperclip
import time

print(" Clipboard Monitor Running... Copy some text!")

while True:
    copied_text = pyperclip.paste()
    if copied_text:
        print(" Copied text detected:", copied_text)
    time.sleep(2)  # Check every 2 seconds
