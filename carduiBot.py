# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2024, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: July 3rd, 2024
# | Last update..: July 3rd, 2024
# | WhatIs.......: InstagramBot_carduiBot - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# instagrapi GitHub: https://github.com/subzeroid/instagrapi?tab=readme-ov-file
# instagrapi Upload media documentation: https://subzeroid.github.io/instagrapi/usage-guide/media.html

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

# Instagram credentials
carduiBotUser = ""
carduiBotPassword = ""

# --------------------------- Code ----------------------------
class InstagramBot:

    def __init__(self):
        self.user = carduiBotUser
        self.password = carduiBotPassword

    def new_post(self):
        pass
