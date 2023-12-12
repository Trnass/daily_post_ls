import requests

username = "Trnass"
password = "Aa123456"
db_id = "6969"
obsah = "emotikona dle nabídky"

session = requests.Session()

login_url = "https://leosight.cz/prihlaseni"
credentials = {
    "username": username,
    "password": password
}

response = session.post(login_url, data=credentials)

if response.ok:
    print("Přihlášení bylo úspěšné.")

    char_url = f'https://artic.leosight.cz/chars/{db_id}'
    response = session.get(char_url)
    iris_url = 'https://artic.leosight.cz/www/iris.ic/'
    response = session.get(iris_url)

    form_data = {'content': f'{obsah}'}
    post_response = session.post(iris_url + 'index.php', data=form_data)
    if post_response.ok:
        print("Formulář byl úspěšně odeslán.")
    else:
        print("Nepodařilo se odeslat formulář.")
else:
    print("Přihlášení selhalo.")
