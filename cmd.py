from Funchin import *

commands = ['Приветик',
            'открой гитхаб',
            'открой файл',
            'down comp',
            'выруби компьютер',
            'Спасибо',
            'покажи файл',
            'покажи список команд',
            'open vk',
            'открой браузер', 'открой интернет',
            'открой youtube',
            'включи музон',
            'вруби музыку',
            'сколько время',
            'очисти файл',
            'открой стату',
            'покажи cтатистику',
            'покажи красивую девушку',
            'открой музыку',
            'переведи',
            'планы',
            'на будущее',
            'что планируется',
            'play lil pump',
            'загугли',
            'апдейт', 'апгрейт',
            'как тебя зовут', 'кто ты',
            'Прогноз погоды',
            'накинь малины',
            'сделай смарт',
            'сделай французкскую атмосферу',
            'сделай по красоте',
            'кто твой создатель']

cmds = {
    'Приветик' : hello,                         'выруби компьютер' : shut,                   'down comp' : shut,
    'Спасибо' : quit,                            'покажи  cтатистику' : pri_com,           'загугли':web_search,
    'открой браузер' : brows,                  'включи vk' : ovk,                            'открой интернет' : brows,
    'открой youtube' : youtube,                   'вруби музыку' : musik,                      'open vk' : ovk,
    'открой  стату' : pri_com,                   'включи музон' : musik,                      'очисти файл' : clear_analis,
    'покажи файл' : pri_com,                  'открой файл' : pri_com,                  'открой музыку' : musik,
    'планы' : plans,                           'на будущее' : plans,                      'что планируется' : plans,
    'открой гитхаб' : github,                     'pump' : playLILPump,                    'сколько время' : time,
    'переведи' : check_translate,                'play lil pump': playLILPump ,               'апдейт':update,
    'как тебя зовут' :alexa,
    'кто ты': alexa,
    'апгрейт': upgrade,
    'Прогноз погоды' :weather, 'накинь малины': playYoloTAgMAlina, 'сделай смарт': playPharaohSmart,  'сделай французкскую атмосферу': playZazJuVew,
    'сделай по красоте': playKatyaNovemvber, 'кто твой создатель': obiitoOne
}
