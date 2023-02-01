import requests,json
import urllib.parse
import schedule
import time

url = "https://api.apilayer.com/exchangerates_data/convert?to=THB&from=USD&amount=1"
url2 = "https://api.apilayer.com/exchangerates_data/convert?to=THB&from=TWD&amount=1"
payload = {}
headers= {
  "apikey": "RRR3BYHZ5pPvdJ2Ocl0rWqyTzxHTk4pO"
}
response = requests.request("GET", url, headers=headers, data = payload)
response2 = requests.request("GET", url2, headers=headers, data = payload)

status_code = response.status_code
result = response.text
result2 = response2.text
response_info = json.loads(result)
response_info2 = json.loads(result2)
usdtothb = response_info["info"]["rate"]    
twdtothb = response_info2["info"]["rate"]    
date = response_info["date"]

print(usdtothb)

LINE_ACCESS_TOKEN="3CxeDEtvfhcJDvzO447J3ufLZuJnI8HYzWJhbw3Q962"
url_line = "https://notify-api.line.me/api/notify"



message ="ค่าเงิน USD -> THB : %f \n ค่าเงิน TWD -> THB : %f \n วันที่ : %s"%(usdtothb,twdtothb,date) # ข้อความที่ต้องการส่ง
# ข้อความที่ต้องการส่ง
msg = urllib.parse.urlencode({"message":message})

LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
def job():
  session = requests.Session()
  a=session.post(url_line, headers=LINE_HEADERS, data=msg)
  print(a.text)
schedule.every().day.at("7:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)