# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2024, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: July 9th, 2024
# | Last update..: July 9th, 2024
# | WhatIs.......: InstagramBot_dataBase - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Python – How to Check if a file or directory exists:
#     https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
# Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# Pandas read csv() Tutorial: https://www.datacamp.com/tutorial/pandas-read-csv
# How do I read and write tabular data?:
#     https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html

# ------------------------- Libraries -------------------------
import datetime  # datetime.datetime.now()
import os  # os.path.exists(path)
import pandas as pd

# ------------------------- Variables -------------------------
# Time
now = datetime.datetime.now()
todayDate = now.strftime("%d/%m/%Y")
nowTime = now.strftime("%H:%M")
nowDateTime = now.strftime("%d/%m/%Y %H:%M:%S")

instagramPost_path = './instagrampost.csv'


# --------------------------- Code ----------------------------
class InstagramPost:

    def __init__(self):
        self.path = instagramPost_path
        self.dataBase = None

    def get_data_base(self):
        if os.path.exists(self.path):
            print("File exists")
            self.dataBase = pd.read_csv(self.path, index_col="idinstagrampost")
            self.dataBase.head()
        else:
            print("404")
