import pygetwindow

with open("window_info.txt", "r") as file:
    window_list = [line.strip().split(":") for line in file.readlines()]

for name, box_str in window_list:
    win = pygetwindow.getWindowsWithTitle(name)[0]
    win.box = tuple(map(int, box_str.split(",")))
