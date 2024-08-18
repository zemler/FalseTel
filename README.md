# FalseTel

<img src=./img/FalseTel.webp width=600px>

### author: Jan zemler Zemla

**`Description`**

FalseTel is a python-written honeypot that pretends to be a telnet service responsible for the admin console for the backups server

I wrote this program for educational purposes and to improve enhance my python skills. It's not likely to be useful to anyone in a production environment because it doesn't offer much functionality but feel free

**`How it works?`**

The program runs a telnet honeypot service on port 23. Every attempt to connect to the service is written to the FalseTell.log file, as well as the sended login data and commands typed in the fake shell.

Each log has the following structure:

```
{Date} - Recived {info} from address: {address}
```

#

**`Installation & Usage:`**

Git Clone to your local computer:

```
git clone https://github.com/zemler/FalseTel.git
```

Run with python3:

```
python3 falsetel.py
```

# License

This project is licensed under the MIT License
