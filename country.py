# coding = utf-8
# country = input('나라 입력:')
import requests
import json
url = 'http://apis.data.go.kr/1262000/TravelAlarmService2/getTravelAlarmList2'
params = {'serviceKey': 'VVPaC0RDxkfKH+odRoIcjKFKhgFujjCi1x3IQaR1EZwcvxrdNmti4rNng1BB8uPg2D5HLu03NzAdGEDTJ0t8Mg==',
          'returnType': 'JSON',
          'numOfRows': '197',
          # 'cond[country_nm::EQ]': country,
          'pageNo': '1'}
response = requests.get(url, params=params)
contents = response.text
obj = json.loads(contents)
print(obj)

asia = []
asia_lvl = []
europe = []
europe_lvl = []
america = []
america_lvl = []
africa = []
africa_lvl = []
ME = []
ME_lvl = []

for i in range(0, 197):
    print(obj["data"][i]["continent_nm"])
    if obj["data"][i]["continent_nm"] == '아프리카':
        if obj["data"][i]["alarm_lvl"] != None:
            africa.append(obj["data"][i]["country_nm"])
            africa_lvl.append(obj["data"][i]["alarm_lvl"])
    if obj["data"][i]["continent_nm"] == '유럽':
        if obj["data"][i]["alarm_lvl"] != None:
            europe.append(obj["data"][i]["country_nm"])
            europe_lvl.append(obj["data"][i]["alarm_lvl"])
    if obj["data"][i]["continent_nm"] == '미주':
        if obj["data"][i]["alarm_lvl"] != None:
            america.append(obj["data"][i]["country_nm"])
            america_lvl.append(obj["data"][i]["alarm_lvl"])
    if obj["data"][i]["continent_nm"] == '아주':
        if obj["data"][i]["alarm_lvl"] != None:
            asia.append(obj["data"][i]["country_nm"])
            asia_lvl.append(obj["data"][i]["alarm_lvl"])
    if obj["data"][i]["continent_nm"] == '중동':
        if obj["data"][i]["alarm_lvl"] != None:
            ME.append(obj["data"][i]["country_nm"])
            ME_lvl.append(obj["data"][i]["alarm_lvl"])



continent = ['아시아', '유럽', '아메리카', '아프리카', '중동']
alarm_lvl = [sum(asia_lvl)/len(asia_lvl), sum(europe_lvl)/len(europe_lvl), sum(america_lvl)/len(america_lvl),
             sum(africa_lvl)/len(africa_lvl), sum(ME_lvl)/len(ME_lvl)]
import matplotlib.pyplot as plt
print('선 그래프')
plt.plot(continent, alarm_lvl)
plt.show()
