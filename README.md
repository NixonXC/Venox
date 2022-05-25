# Veno

Easy to use information gathering bot
Maintained by NixonXC

# Requirements

`python-whois`
`py-cord`
`phonenumbers`
`aiohttp`

# Commands

<h3>Slash Commands and Prefix Commands Supported </h3>

**DEFAULT PREFIX:** `v!`

`help` `ping` `whois <domain>` `ipwhois <ip>` `finder <user>` `phonewhois <phone-number>` `checkemail <email>`

# How to Use

First replace `AUTH`'s value with your token in <a href="https://github.com/NixonXC/Veno/blob/main/db/database.json">db/database.json<a>
You can also change the bot's `PREFIX` and `STREAM_URL` in <a href="https://github.com/NixonXC/Veno/blob/main/db/database.json">db/database.json<a> Changing the Prefix will also change the prefix information on commands, status etc.

```json
{
    "AUTH": "TOKEN",
    "PREFIX": "v!",
    "STREAM_URL": "https://github.com/NixonXC/Veno"
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
