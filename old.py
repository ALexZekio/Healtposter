# Copyright <c> 2018 NeTFoX.
# Powered by ALex Zerkio
#

import os
import requests
import json
import time

# 请求地址
url = "http://health.laotingedu.cn/api/services/app/organUser/SubmitUserHealth"

# 消息头
headers = {
        "Connection": "keep-alive",
        "Content-Length": "283",
        "Cache-Control": "max-age=0",
        "Origin":"http://health.laotingedu.cn",
        "Upgrade-Insecure-Requests":"1",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1901A Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/3390 MicroMessenger/8.0.1.1841(0x28000157) Process/tools WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
        "Accept": "*/*",
        "X-requested-With": "com.tencent.mm",
        "Referer": "http://health.laotingedu.cn/index.html?v=2.1",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "Abp.Localization.CultureName=en-US; ASP.NET_SessionId=j54jt4uh4gjqgeewzcluyfyp; webToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoi5YiY5a6H6L2pIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiNmNhZWFiOWNhZTUxNDc2OWJlNWJmNTMyODZhZTg5ZTYiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL2FjY2Vzc2NvbnRyb2xzZXJ2aWNlLzIwMTAvMDcvY2xhaW1zL2lkZW50aXR5cHJvdmlkZXIiOiJBU1AuTkVUIElkZW50aXR5IiwiaHR0cDovL3d3dy5hc3BuZXRib2lsZXJwbGF0ZS5jb20vaWRlbnRpdHkvY2xhaW1zL3RlbmFudElkIjoiMSIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiODQ0NjIwOCIsInN1YiI6Ijg0NDYyMDgiLCJqdGkiOiI4MWQ0YmY0OS02YzE2LTQzYzMtODdiOC1lOWY3MzFiMzhlMjMiLCJpYXQiOjE2MTIxMDg3MDYsIm5iZiI6MTYxMjEwODcwNiwiZXhwIjoxNjQzNjQ0NzA2LCJpc3MiOiJIRjEwNDY3ODhMaSIsImF1ZCI6IkhGQ1l4MTA3ODkifQ.IHNjkO4bZQfpAe_yGggScU0HWTprym_MJaoZP3TYdvA",
        }

# 消息体
payload = {
        "id": 0,
        "userId": 8446208,              # 用户id    xxxxxxx
        "reportTime": "2021-02-13",     # 上报日期  yyyy-mm-dd
        "temperature": "36.5",          # 体温      xx.x
        "DoNucleicAcidTest": "否",
        "FirstResult": "",
        "SecondResult": "",
        "SelfCurrentArea": "否",
        "DoNucleicAcidTestReason": "",
        "selfHealthy": "无",            # 是否出现下列四种情况？                  1.确诊  2.疑似  3.密切接触者  4.发热人员  5.无
        "familyHealthy": "无",          # 你的家人朋友是否出现下列四种情况？      1.确诊  2.疑似  3.密切接触者  4.发热人员  5.无
        "helpMethed": "无",             # 救助及防护措施                          1.住院治疗  2.定点隔离  3.无
        "testPerson": "",               # 检测人姓名
        "status": 0,
        }

rp = requests.post(url, json=payload, headers=headers,verify=False)
print(rp.json())

localtime = time.localtime(time.time())
time = time.strftime('%m-%d',time.localtime(time.time()))

# 用于日志保存 (date.json.log)
jf = open(str(time) + '.json.log', 'w')
print(str(rp.json()), file=jf)
jf.close()

#os.system("figlet complete")
print("[!] upload complete")









