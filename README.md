## Setting up bot
First, you need to install the library to use your telegram's bot with python, with in this case is [python-telegram-bot](https://python-telegram-bot.org/).
You can install it using `pip install python-telegram-bot`.
<br>
After that, you need to create an bot in Telegram's Botfather and get your Token. You can find an tutorial for it [here](https://medium.com/shibinco/create-a-telegram-bot-using-botfather-and-get-the-api-token-900ba00e0f39).
<br>
Then, open the file `Tbot.py` in your text editor, and paste your bot token in the specified place (line no. 3).
<br>
## Configuring Cities
This bot is configured to use **OpenWeather's One Call API - excluding 'minutely', 'hourly' and 'alerts'**. So, it's necessary to have an OpenWeather account and an OpenWeather API key. It's not necessary to use an paid plan.
<br>
Each `MFCity.py` program ask for OpenWeather's API and store the data in an text file, in the same directory. This process will happen every 6 hours (counting as you started the program). The `Tbot.py` will use the data stored in those text files instead of keep asking for api calls every time.
<br>
You can use many cities you want, as long as you copy the same pattern used in the `MFCity1.py` and add the functions `wcity(message)` in `Tbot.py`.
