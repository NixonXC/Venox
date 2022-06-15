# Venox

Easy to use information gathering bot
Maintained by NixonXC<br>
<h3><a href="https://venoxbot.tk/">venoxbot.tk</a></h3>

# Requirements

Install via `pip install -r requirements.txt`

`python-whois`
`py-cord`
`phonenumbers`
`aiohttp`

# Commands

<h3>Slash Commands and Prefix Commands Supported </h3>

**DEFAULT PREFIX:** `v!`

`help` `ping` `eval` `prefix <new-prefix>` `whois <domain>` `ipwhois <ip>` `finder <user>` `phonewhois <phone-number>` `checkemail <email>` `nameservers <domain>`

# How to Use

First replace `AUTH`'s value with your token in <a href="https://github.com/NixonXC/Veno/blob/main/db/database.json">db/database.json<a>
You can also change the bot's `PREFIX`,  `STREAM_URL` and the `AUTHOR` in <a href="https://github.com/NixonXC/Veno/blob/main/db/database.json">db/database.json<a> Changing the Prefix And Author will also change the information on commands, status etc.

```json
{
    "AUTH": "TOKEN",
    "PREFIX": "v!",
    "STREAM_URL": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "AUTHOR": "NixonXC"
}
```

then run the main file (main.py

<h3>Output:</h3>
```md
[INFO] SUCCESSFULLY LOADED info cog!
[INFO] SUCCESSFULLY LOADED admin cog!
[INFO] SUCCESSFULLY LOADED help cog!
------
Bot is ready!
Logged in as: BOT_NAME
With ID: BOT_ID
PREFIX: BOT_PREFIX
AUTHOR: AUTHOR
STREAM: STREAM_URL
------
```


# Example

![image](https://user-images.githubusercontent.com/81410474/173798814-093d0988-f793-4155-bc32-3632e5d4112b.png)

# Note

This project is made for educational purposes only, the contributors are not responsible for any damage.
