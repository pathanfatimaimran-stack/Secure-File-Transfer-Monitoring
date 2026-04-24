import hashlib
import os
import time

def calculate_hash(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

file_path = input("Enter file path to monitor: ")

if not os.path.exists(file_path):
    print("File not found!")
    exit()

print("Monitoring file:", file_path)

baseline_hash = calculate_hash(file_path)

while True:
    time.sleep(5)  # check every 5 seconds
    current_hash = calculate_hash(file_path)

    if current_hash != baseline_hash:
        print("⚠️ ALERT: File has been modified!")
        print("Old Hash:", baseline_hash)
        print("New Hash:", current_hash)
        break
    else:
        print("No changes detected...")
