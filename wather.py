import urllib3
from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
import schedule


    
url = "https://tenki.jp/forecast/1/2/1400/1103/3hours.html"
#HTML取得
res = requests.get(url)
#HTMLのツリー化
soup = BeautifulSoup(res.text, 'html.parser')
#天気気表まで取る
forecast = []    
forecast = soup.select_one("#forecast-point-3h-today")
print(forecast)

def temperature():
    #temperatureクラスまで取得
    temp_class = forecast.find(class_="temperature")
    
    #print(temp_class)
    #９時から１８時までの気温を取得    
    first_temp = temp_class.find("td")
    second_temp = first_temp.find_next_sibling("td")
    third_temp = second_temp.find_next_sibling("td")
    forth_temp = third_temp.find_next_sibling("td")
    fifth_temp = forth_temp.find_next_sibling("td")
    sixth_temp = fifth_temp.find_next_sibling("td")

    three_temp_str = [third_temp.text, fifth_temp.text, sixth_temp.text]
    three_temp_num = list(map(float, three_temp_str))#浮動小数点型に変更


    #平均算出
    temp_avelage = sum(three_temp_num) / 3
    
    #上着の判断
    if temp_avelage < 20.0:
        wear = "上着推奨"
    else:
        wear = "半袖OK"
        
    print(three_temp_num)
    print(temp_avelage)
    print(wear)

def amount_of_rain():
    #precipitationクラスまで取得
    rain_class = forecast.find(class_="precipitation")
    #print(rain_class)
    #９時から１８時の降水量を取得
    first_rain = rain_class.find("td")
    second_rain = first_rain.find_next_sibling("td")
    third_rain = second_rain.find_next_sibling("td")
    forth_rain = third_rain.find_next_sibling("td")
    fifth_rain = forth_rain.find_next_sibling("td")
    sixth_rain = fifth_rain.find_next_sibling("td")
    

    three_rain_str = [third_rain.text, fifth_rain.text, sixth_rain.text]
    three_rain_num = list(map(int, three_rain_str))#整数型に変更

    third_rain = three_rain_num[0]
    fifth_rain = three_rain_num[1]
    sixth_rain = three_rain_num[2]
    
    #最大降水量
    max_rain = max(three_rain_num)
    #print(max_rain)
    
    #判断 
    if max_rain < 1:
        rain_gear = "晴れ"
    elif max_rain <= 2:
        rain_gear = "濡れてもいいならそのまま行け"
    elif 2 < max_rain < 5 :
        rain_gear = "雨具必須"
    elif 5 <= max_rain < 10:
        rain_gear = "レインコート上下必須　普通の人はバス乗る"
    elif 10 <= max_rain < 20:
        rain_gear = "超降ってる。これでのったら強者"
    elif 20 <= max_rain < 30:
        rain_gear = "大雨注意報レベル。こんな日に自転車乗るのは君くらいだ。"
    else:
        rain_gear = "大雨警報レベル。自転車どこらか外に出るのが危ない。STAY HOME!!"

    print(three_rain_num)
    print(rain_gear)

def wind_vector():
    wind_vector_class = forecast.find(class_="wind-direction")
    #print(wind_vector_class)



    first_wind_vector = wind_vector_class.find("td")
    second_wind_vector = first_wind_vector.find_next_sibling("td")
    third_wind_vector = second_wind_vector.find_next_sibling("td")
    forth_wind_vector = third_wind_vector.find_next_sibling("td")
    fifth_wind_vector = forth_wind_vector.find_next_sibling("td")
    sixth_wind_vector = fifth_wind_vector.find_next_sibling("td")

    three_wind_vector = [first_wind_vector.text, fifth_wind_vector.text, sixth_wind_vector.text]

    n = 0
    while n <= 2:
        three_wind_vector[n].replace("\n"," ")
        n = n + 1

    first_wind_vector_str = three_wind_vector[0]
    second_wind_vector_str = three_wind_vector[1]
    third_wind_vector_str = three_wind_vector[2]
    
    print(" " + first_wind_vector_str, second_wind_vector_str, third_wind_vector_str)

def wind_power():
    wind_power_class = forecast.find(class_="wind-speed")
    #print(wind_power_class)

    
    first_wind_power = wind_power_class.find("td")
    second_wind_power = first_wind_power.find_next_sibling("td")
    third_wind_power = second_wind_power.find_next_sibling("td")
    forth_wind_power = third_wind_power.find_next_sibling("td")
    fifth_wind_power = forth_wind_power.find_next_sibling("td")
    sixth_wind_power = fifth_wind_power.find_next_sibling("td")
    
    three_wind_power_str = [first_wind_power.text, fifth_wind_power.text, sixth_wind_power.text]
    three_wind_power_num = list(map(int, three_wind_power_str))#整数型に変更
    print(three_wind_power_num)

    speed = three_wind_power_num[0]

    if speed < 2:
        coment = "ほぼ無風"
    elif speed == 2 or speed == 3:
        coment = "ほぼ快適。マンション周りは強いかも"
    elif speed == 4:
        coment = "家をちょっと早めに出よう"
    elif speed == 5:
        coment = "しんどい。速度が出なくてイライラし始める"
    elif speed == 6:
        coment = "超しんどい。ハンドルをしっかり握って油断は禁物。縦長の筆箱が倒れれる"
    elif speed < 9:
        coment = "全然進まない。止まる時突風で倒れないように注意"
    elif speed <19:
        coment = "自転車をあきらめを視野に入れる＜注意報レベル＞"
    elif speed < 24:
        coment = "＜台風レベル＞＜暴風警報レベル＞徒歩でも厳しい"
    else:
        coment = "＜外出危険＞物がプロ野球並で飛んでくる"

    print(coment)
    
    

    
temperature()
amount_of_rain()
wind_vector()
wind_power()

    



#schedule.every().day.at("6:00").do(job)



    

    
