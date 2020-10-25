# These functions start, resize, and move windows on Windows machines
import win32gui
from pywinauto import Desktop
windows = Desktop(backend="uia").windows()
# print([w.window_text() for w in windows])
from pywinauto.application import Application
app = Application(backend="uia").start('notepad.exe')

# describe the window inside Notepad.exe process
dlg_spec = app.UntitledNotepad
# wait till the window is really open
actionable_dlg = dlg_spec.wait('visible')
hwnd = win32gui.FindWindow(None, 'Untitled - Notepad')

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0 # width
h = y1 - y0 # height

print(f"x0 = " + str(x0))
print(f"y0 = " + str(y0))
print(f"x1 = " + str(x1))
print(f"y1 = " + str(y1))
print(f"h = " + str(h))
print(f"w = " + str(w))
win32gui.MoveWindow(hwnd, 10, 10, 2500, 1500, True)

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0 # width of window
h = y1 - y0 # height

print(f"new x0 = " + str(x0))
print(f"new y0 = " + str(y0))
print(f"new x1 = " + str(x1))
print(f"new y1 = " + str(y1))
print(f"new h = " + str(h))
print(f"new w = " + str(w))
# import cv2
# # Exit on key press
# cv2.waitKey(0)
# cv2.destroyAllWindows()
