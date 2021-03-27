## Initial requirements
1. Install [python-telegram-bot](https://python-telegram-bot.org/) - `python -m pip install python-telegram-bot`.
2. Install [python-requests](https://2.python-requests.org/en/master/user/install/#install) - `python -m pip install requests`.

## Setting up bot
1. Create an bot in Telegram's Botfather and get your Token. You can find an tutorial for it [here](https://medium.com/shibinco/create-a-telegram-bot-using-botfather-and-get-the-api-token-900ba00e0f39).
2. Open the file `Tbot.py` in your text editor, and paste your bot token in the line no. 3.

## Configuring cities
This bot is configured to use **OpenWeather's One Call API - excluding 'minutely', 'hourly' and 'alerts'**. So, it's necessary to have an OpenWeather account and an OpenWeather API key. There is no need to use a paid plan.

To set up your api link on each city program, [get your api link](https://openweathermap.org/api/one-call-api), open an `MFCity.py` file and insert your api link in the line no. 2.

Each `MFCity.py` program ask for OpenWeather's API and store the data in an text file, in the same directory. This process will happen every 6 hours (counting as you started the program). The `Tbot.py` will use the data stored in those text files instead of keep asking for api calls every time.

You can use many cities you want, as long as you copy the same pattern used in the `MFCity1.py` and add the functions `wcity(message)` in `Tbot.py`.
