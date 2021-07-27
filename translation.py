import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hai {}!!</b>
<i>I'm Simple Auto file Forward Bot❤️
This Bot forward all files to One Public channel to Your Personal channel🔥
More details /help</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Follow These Steps!!</b>
<b>• Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>• Then give admin permission in your personal telegram channel</b>
<b>• Then send any message In your personal telegram channel</b>
<b>• Then use /run command in your bot</b>

<b><u>Available Command</b></u>

* /start - <b>Bot Alive</b>
* /help - <b>more help</b>
* /run - <b>start forward</b>
* /about - <b>About Me</b>"""
  ABOUT_TXT = """Hy Man🐙

<b>Name 🔰 :Auto Forward Bot
<b>Credit 🐙 :@Perfect_Vazha 🔥
<b>Language 📝 :</b> <code>Python3</code>
<b>Lybrary 🌀 :</b> <code>Pyrogram v1.2.9</code>"""

