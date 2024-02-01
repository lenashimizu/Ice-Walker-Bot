import pyautogui
from PIL import ImageGrab
import math
from time import sleep
import keyboard

global running 
running = False

def find_nearest_color(color, tolerance=10):
    screen = ImageGrab.grab()
    width, height = screen.size

    for x in range(0, width, 3):
        for y in range(0, height, 3):
            current_color = screen.getpixel((x, y))
            distance = color_distance(color, current_color)

            if distance <= tolerance:
                return x, y

    return None

def color_distance(color1, color2):
    return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))

def color_distance_bad(color1, color2):
    return sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2))

def move_mouse_to_color(target_color, tolerance=10):

    result = find_nearest_color(target_color, tolerance)
    if result is None:
        target_x, target_y = pyautogui.position()
    elif result is not None:
        target_x, target_y = result
        pyautogui.moveTo(target_x, target_y)
        pyautogui.rightClick()

def main():
    global running
    while not running:
            test_for_running()
    while True:
        test_for_running()
        if running:
            move_mouse_to_color((169, 198, 241))

def test_for_running():
    global running
    if keyboard.is_pressed("["):
        if running:
            running = False
            print("Stopping")
            sleep(1)
        else:
            running = True
            print("Starting")
            sleep(1)

main()