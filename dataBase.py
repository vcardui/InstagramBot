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
# | Last update..: July 20th, 2024
# | WhatIs.......: InstagramBot_dataBase - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Python – How to Check if a file or directory exists:
#     https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
# Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# Pandas read csv() Tutorial: https://www.datacamp.com/tutorial/pandas-read-csv
# How do I read and write tabular data?:
#     https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html
# NEVER grow a DataFrame row-wise!
#   https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-and-then-filling-it

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
        self.DataFrame = None

    def get_data_base(self):
        if os.path.exists(self.path):
            print("File exists")
            self.DataFrame = pd.read_csv(self.path, index_col="idinstagrampost")
            self.DataFrame.head()
        else:
            print("Creating new DataFrame...")
            self.DataFrame = pd.DataFrame(
                columns=['idinstagrampost', 'caption', 'pathtoimage', 'dateadded', 'dateposted'])
            self.DataFrame.to_csv(path_or_buf="instagrampost.csv", index=False)
            print("👍New DataFrame successfully created")

    def new_row(self, postCaption, pathtoimage):
        instagram_post_dic = []
        row = {
            "idinstagrampost": 1,
            "caption": postCaption,
            "pathtoimage": pathtoimage,
            "dateadded": nowDateTime,
            "dateposted": ""
        }
        instagram_post_dic.append(row)
        dic = pd.DataFrame(instagram_post_dic)
        self.DataFrame = pd.concat([self.DataFrame, dic])
        print("👍New row successfully added")
