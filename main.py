# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2024, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: June 3rd, 2024
# | Last update..: July 3rd, 2024
# | WhatIs.......: InstagramBot - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# instagrapi GitHub: https://github.com/subzeroid/instagrapi?tab=readme-ov-file
# instagrapi Upload media documentation: https://subzeroid.github.io/instagrapi/usage-guide/media.html

# ------------------------- Libraries -------------------------
# CarduiBot
from carduiBot import InstagramBot
from dataBase import InstagramPost  # dataBase Object

# ------------------------- Variables -------------------------


# --------------------------- Code ----------------------------
carduiBot = InstagramBot()
instagramPost = InstagramPost()

instagramPost.get_data_base()

# carduiBot.new_post()
