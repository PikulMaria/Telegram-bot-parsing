from ast import If
from email import message
import requests
from datetime import datetime
from telegram import send_telegram

def get_game(result):
    for game in result["Value"]:
        game_id = game["I"]
        liga_name = game["L"]
        first_name = game["O1"]
        second_name = game["O2"]
        sc_pack = game["SC"]
        cps = sc_pack["CPS"]
        if '1-й Сет' in cps:
            ps_pack = sc_pack["PS"]
            #print(ps_pack)
            for key in ps_pack:
    #Тут мы нашли сет
                key_id = key["Key"]
                if key_id == 1:
                    for value in ps_pack:
                        value_name = value["Value"]
                        try:
                            s_one = value_name["S1"]
                        except:
                            s_one = "0"
                        try:
                            s_two = value_name["S2"]
                        except:
                            s_two = "0"
                        if s_one == s_two:
                            message = f'Лига: {liga_name} \n'\
                                      f'{cps} \n'\
                                      f'{first_name} : {s_one} \n'\
                                      f'{second_name} : {s_two} \n'
                            send_telegram(message)
                            print(message)
                            print("____________________________________________________________________")
                             
      

def main():
    url = 'https://1xstavka.ru/live/Tennis/' 
    params = {
        'sports': '4',
        'count': '50',
        'antisports': '188',
        'mode': '4',
        'country': '1',
        'partner': '51',
        'getEmpty': 'true',
        'noFilterBlockEvent': 'true',
    }
    response = requests.get('https://1xstavka.ru/LiveFeed/Get1x2_VZip',  params=params)
    result = response.json()
    get_game(result)

if __name__ == '__main__':
    main()