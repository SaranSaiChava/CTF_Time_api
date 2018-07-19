import json
import requests
import urllib.request

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


parameter = {"start":1422019499,"finish":1423029499}


response=requests.get("https://ctftime.org/api/v1/events/?limit=100",headers=header,params=parameter)
content_list = response.json()
for i in content_list:
	contest_duration=((i["duration"])['hours'])
	contest_name = (((i["organizers"])[0])["name"])
	contest_link = (i["url"])
	contest_start_time=(i["start"])[11:]
	cst1=int((i["start"])[11:13])
	cst2=int((i["start"])[14:16])
	cst3=int((i["start"])[17:19])
	ist1=int((i["start"])[20:22])
	ist2=int((i["start"])[23:25])
	print(cst1,cst2,cst3,ist1,ist2)

#contest_id = feed[0][0]
#contest_name = content_list[0].('name')
#contest_time = feed["finish"]
#contest_link = feed["ctftime_url"]

print(response.status_code)
print(contest_duration,contest_name,contest_link,contest_start_time)

