import pygetwindow

# Write names of windows/programs into this list. Only the first instance of 
# each will be recorded (i.e. multiple Chrome windows would be ignored).
target_titles = ["Discord", "Outlook", "Google Chrome"]

found_windows = []

for title in target_titles:
    try:
        win = pygetwindow.getWindowsWithTitle(title)[0]
        found_windows.append(f"{title}: {win.left}, {win.top}, {win.width}, {win.height}\n")
    except IndexError:
        print(f"No window found named {title}!")

with open("window_info.txt", "w") as file:
    file.writelines(found_windows)
