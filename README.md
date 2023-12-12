## Instalace knihoven
pip3 install requests
## Vytvoření CRONu
crontab -e
### Do CRONu uložíme toto:
11 11 * * * /usr/bin/python3 /var/py_cron/daily_post_iris/main.py
