import win32gui
#hwnd = win32gui.FindWindow(None, 'Window Title')
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

# win32gui.MoveWindow(hwnd, x0, y0, w-50, h-50, True)

win32gui.MoveWindow(hwnd, x0+100, y0, w+400, h+500, True)

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0 # width
h = y1 - y0 # height

print(f"x0 = " + str(x0))
print(f"y0 = " + str(y0))
print(f"x1 = " + str(x1))
print(f"y1 = " + str(y1))
print(f"h = " + str(h))
print(f"w = " + str(w))