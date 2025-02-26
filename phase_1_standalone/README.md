Installing and Testing Clipboard Monitoring with pyperclip
Step 1: Install pyperclip

To enable clipboard monitoring, you first installed pyperclip.

Run this command in PowerShell:

pip install pyperclip

Installation Output:

Collecting pyperclip
  Downloading pyperclip-1.9.0.tar.gz (20 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: pyperclip
  Building wheel for pyperclip (pyproject.toml) ... done
  Created wheel for pyperclip: filename=pyperclip-1.9.0-py3-none-any.whl size=11066 sha256=...
  Stored in directory: C:\Users\SELVAKUMAR\AppData\Local\pip\cache\wheels...
Successfully built pyperclip
Installing collected packages: pyperclip
Successfully installed pyperclip-1.9.0
? pyperclip was installed successfully!

Step 2: Create a Test Script
You created a test script test_clipboard.py to check if clipboard monitoring works.


Explanation of Clipboard Monitoring Code
This program monitors the clipboard for copied text and prints it in real time. It uses the pyperclip library to access the clipboard.

Code Breakdown
import pyperclip
import time

def monitor_clipboard():
    print("Clipboard Monitor Running... Copy some text!")
    last_copied_text = ""  # Stores the last copied text to avoid duplicate prints

    while True:
        copied_text = pyperclip.paste()  # Get current clipboard content
        if copied_text != last_copied_text:  # Check if new text was copied
            print(f"Copied text detected: {copied_text}")  # Print copied text
            last_copied_text = copied_text  # Update the last copied text
        time.sleep(1)  # Wait for 1 second before checking again

if __name__ == "__main__":
    monitor_clipboard()

How It Works
1?The program checks the clipboard every second using pyperclip.paste().
2?If the copied text changes, it prints the new text.
3? last_copied_text is used to avoid duplicate prints of the same text.
4? The loop runs indefinitely until manually stopped (Ctrl+C).
