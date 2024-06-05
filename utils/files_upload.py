# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         files_upload.py
**    @author           Echo
**    @EditTime         2024/2/21
"""
import os
from typing import *

import pyautogui
import pyperclip
import pywinauto
from pywinauto import Application
from pywinauto.keyboard import send_keys
import time


def upload_file(file_path, file_name):
    time.sleep(1)
    app = pywinauto.Desktop()
    dlg = app["打开"]
    dlg["Toolbar3"].click()
    send_keys(file_path)
    send_keys('{VK_RETURN}')
    time.sleep(0.5)
    dlg["文件名(&N):Edit"].type_keys(file_name)
    dlg["打开(&O)"].click()
    time.sleep(0.5)

