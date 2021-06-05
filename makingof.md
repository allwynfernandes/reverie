






# Tries
I tried using pyautogui since I had prior experience builing stuff with it. However, it tanked. It kept asking for this other app, "scrot" apart from sounding rather unapetising, it also drew me away fom the goal of being super minimalist with the requirements. I had already commited a sin by importing opencv and didn't want to add to the bulk.
```python

    # Capture Screen
    # screenshot = pyautogui.screenshot()
    # screenshot.save(scrImageName)
    # print("Screenshot captured")

```
I resorted to reading up on the options available, and stumbled across MSS. This library was below 10KB and only 2 lines of code to save an image screenshot to disk. Amen! I said.

