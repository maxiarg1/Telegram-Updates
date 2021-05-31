from bs4 import BeautifulSoup
import requests
import schedule


def bot_send_text(bot_message):
    
    bot_token = 'TOKEN'
    bot_chatID = 'chatID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def btc_scraping():
    url = requests.get('https://www.meteored.com.ar/tiempo-en_Neuquen-America+Sur-Argentina-Neuquen--1-16888.html')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'dato-temperatura changeUnitT'})
    format_result = result.text

    return format_result

def btc_scraping1():
    url = requests.get('https://www.meteored.com.ar/tiempo-en_Neuquen-America+Sur-Argentina-Neuquen--1-16888.html')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'maxima changeUnitT'})
    format_result = result.text

    return format_result

def btc_scraping2():
    url = requests.get('https://www.meteored.com.ar/tiempo-en_Neuquen-America+Sur-Argentina-Neuquen--1-16888.html')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'minima changeUnitT'})
    format_result = result.text

    return format_result


def report():
    btc_price = f'Temperatura actual {btc_scraping()} \nTemperatura máxima {btc_scraping1()}\nTemperatura minima {btc_scraping2()}'
    bot_send_text(btc_price)

def initia():
    welcomeMessage = f'Estoy funcionando!'
    bot_send_text(welcomeMessage)


if __name__ == '__main__':
    print("I'm working...")
    initia()
    schedule.every().day.at("07:00").do(report)
    schedule.every().day.at("12:00").do(report)
    schedule.every().day.at("13:15").do(report)    
    schedule.every().day.at("17:00").do(report)

    while True:
        schedule.run_pending()
