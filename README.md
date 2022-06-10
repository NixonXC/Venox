# Venox

Easy to use information gathering bot
Maintained by NixonXC<br>
<h3><a href="https://venoxbot.tk/">venoxbot.tk</a></h3>

# Requirements

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
    "STREAM_URL": "https://github.com/NixonXC/Veno",
    "AUTHOR": "NixonXC"
}
```

then run the main file (main.py

And it should print:
```py
Bot is ready!
Logged in as: Bot_Name
With ID: Bot_ID
------
```

# Note

This project is made for educational purposes only, the contributors are not responsible for any damage.
