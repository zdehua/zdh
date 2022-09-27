import requests
se=requests.session()
url1='https://cas.bjut.edu.cn/login?service=https%3A%2F%2Fitsapp.bjut.edu.cn%2Fa_bjut%2Fapi%2Fsso%2Findex%3Fredirect%3Dhttps%253A%252F%252Fitsapp.bjut.edu.cn%252Fuc%252Fapi%252Foauth%252Findex%253Fredirect%253Dhttp%253A%252F%252Fyqfk.bjut.edu.cn%252Fapi%252Flogin%252Fpages-index-index%253Flogin%253D1%2526appid%253D200220501233430304%2526state%253DSTATE%26from%3Dwap'
header1={
    "Host": "cas.bjut.edu.cn",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "document",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Referer": "https://yqfk.bjut.edu.cn/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}
re1=se.get(url=url1,headers=header1,verify=False)
print(re1.status_code)
print(re1.headers['Set-Cookie'])
print(re1.cookies)
cook=re1.cookies
re_text=re1.text
re_text=re_text[re_text.find("execution")+18:re_text.find("_eventId")-16]
print(re_text)

durl='https://cas.bjut.edu.cn/login'
# print(re_text)
data2={
    'username':'17074516',
    'password':'Aa123456789.',
    'submit':'LOGIN',
    'type':'username_password',
    'execution':re_text,
    '_eventId':'submit'
}

header2={
    "Host": "cas.bjut.edu.cn",
    "Connection": "keep-alive",
    "Content-Length": "5908",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://cas.bjut.edu.cn",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://cas.bjut.edu.cn/login?service=https%3A%2F%2Fitsapp.bjut.edu.cn%2Fa_bjut%2Fapi%2Fsso%2Findex%3Fredirect%3Dhttps%253A%252F%252Fitsapp.bjut.edu.cn%252Fuc%252Fapi%252Foauth%252Findex%253Fredirect%253Dhttp%253A%252F%252Fyqfk.bjut.edu.cn%252Fapi%252Flogin%252Fpages-index-index%253Flogin%253D1%2526appid%253D200220501233430304%2526state%253DSTATE%26from%3Dwap",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}

# re3=se.post(url=url1,cookies=cook,data=data2,verify=False)
# re3=requests.post(url=durl,cookies=cook,data=data2,allow_redirects=False,verify=False)
re3=se.post(url=durl,data=data2,verify=False,allow_redirects=False)
print(re3.status_code)
print(re3.headers)
Gcook=re3.headers['Set-Cookie']
Gcook=Gcook[:Gcook.find(' Domain=')]
print(Gcook)
url4=re3.headers['Location']
print(se.cookies)
header4={
    "Host": "itsapp.bjut.edu.cn",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Referer": "https://cas.bjut.edu.cn/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

re4=se.get(url=url4,headers=header4,verify=False,allow_redirects=False)
# print(re4.headers)
url5=re4.headers['Location']
print(se.cookies)
header5 = {
    "Host": "itsapp.bjut.edu.cn",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Referer": "https://cas.bjut.edu.cn/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

re5=se.get(url=url5,headers=header5,verify=False,allow_redirects=False)
print(se.cookies)
# print(re5.headers)
url6=re5.headers['Location']

re6=se.get(url=url6,headers=header5,verify=False,allow_redirects=False)
print(re6.headers)
print("###########################")
print(se.cookies)
url7=re6.headers['Location']
print(url7)

cook2={
    'XSRF-TOKEN':'eyJpdiI6IjZEQWJCVmdsMHNNeW9DT3NPMDBxTGc9PSIsInZhbHVlIjoibUZKOHB5TGxEWitzazRBR3RXNU9veTZCdW10dkc5V1k5Mm8vZXF4cmpzektDZTd4Q2dYeGRTL1FOTlpxc2lYOG53bzZ1RGdvL1ZwMHRZTE5wU09jSHZDNlBFNGNNcnBVQjVaT0EvTERQVmZIS0RrZzk2N0l6Y29DWS9sbUlDMWkiLCJtYWMiOiIwODk4YzJmNDdiOGEyMjA3NmQ4YzEzMjhlN2RjYTYyZGI2NzM0ZDUzZTUzMGI1Nzg3MDE1MzQwNDVmODc3NWI2In0%3D',
    '_session':'eyJpdiI6ImF1LzBQZGFucWJiWC9qWHhITEVjbWc9PSIsInZhbHVlIjoiREV5YVVPdXNJWlNUUFhUd1ZNM0dlUFVlT1diSXZUekpMQTJ3OE5STXFsMnVvbjJtVzJoSjBNNWVWeSs4NmYxWUFYUDBUa0hiaWxrY0VHWTRLQ0VpOVlvcWFBR3lMTk1ST1RNM1JGaExIb29RbWNsc1h2eUxMMkd3R3hza3dOTzYiLCJtYWMiOiIwYzJhZmE2ZjExZDdlOWQxZTc0NWI0NTkxNjIyYzYwZTBjMGY5MjY2YzJhMWFlYTAyY2U0N2NkOGNlMThhYTYzIn0%3D',
    'CASTGC':'TGT-376278-l9jlwl-sSqC4VftoiguGWcuelsINlxnlu4osMWXwTvyXx-MnalyBC-B8f2QN9s-Ocss46b4b91a66cb'
}
coo1='XSRF-TOKEN=eyJpdiI6IjZEQWJCVmdsMHNNeW9DT3NPMDBxTGc9PSIsInZhbHVlIjoibUZKOHB5TGxEWitzazRBR3RXNU9veTZCdW10dkc5V1k5Mm8vZXF4cmpzektDZTd4Q2dYeGRTL1FOTlpxc2lYOG53bzZ1RGdvL1ZwMHRZTE5wU09jSHZDNlBFNGNNcnBVQjVaT0EvTERQVmZIS0RrZzk2N0l6Y29DWS9sbUlDMWkiLCJtYWMiOiIwODk4YzJmNDdiOGEyMjA3NmQ4YzEzMjhlN2RjYTYyZGI2NzM0ZDUzZTUzMGI1Nzg3MDE1MzQwNDVmODc3NWI2In0%3D; _session=eyJpdiI6ImF1LzBQZGFucWJiWC9qWHhITEVjbWc9PSIsInZhbHVlIjoiREV5YVVPdXNJWlNUUFhUd1ZNM0dlUFVlT1diSXZUekpMQTJ3OE5STXFsMnVvbjJtVzJoSjBNNWVWeSs4NmYxWUFYUDBUa0hiaWxrY0VHWTRLQ0VpOVlvcWFBR3lMTk1ST1RNM1JGaExIb29RbWNsc1h2eUxMMkd3R3hza3dOTzYiLCJtYWMiOiIwYzJhZmE2ZjExZDdlOWQxZTc0NWI0NTkxNjIyYzYwZTBjMGY5MjY2YzJhMWFlYTAyY2U0N2NkOGNlMThhYTYzIn0%3D; CASTGC=TGT-376278-l9jlwl-sSqC4VftoiguGWcuelsINlxnlu4osMWXwTvyXx-MnalyBC-B8f2QN9s-Ocss46b4b91a66cb'
header7={
    "Host": "yqfk.bjut.edu.cn",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    'Cookie': 'XSRF-TOKEN=eyJpdiI6IjZEQWJCVmdsMHNNeW9DT3NPMDBxTGc9PSIsInZhbHVlIjoibUZKOHB5TGxEWitzazRBR3RXNU9veTZCdW10dkc5V1k5Mm8vZXF4cmpzektDZTd4Q2dYeGRTL1FOTlpxc2lYOG53bzZ1RGdvL1ZwMHRZTE5wU09jSHZDNlBFNGNNcnBVQjVaT0EvTERQVmZIS0RrZzk2N0l6Y29DWS9sbUlDMWkiLCJtYWMiOiIwODk4YzJmNDdiOGEyMjA3NmQ4YzEzMjhlN2RjYTYyZGI2NzM0ZDUzZTUzMGI1Nzg3MDE1MzQwNDVmODc3NWI2In0%3D; _session=eyJpdiI6ImF1LzBQZGFucWJiWC9qWHhITEVjbWc9PSIsInZhbHVlIjoiREV5YVVPdXNJWlNUUFhUd1ZNM0dlUFVlT1diSXZUekpMQTJ3OE5STXFsMnVvbjJtVzJoSjBNNWVWeSs4NmYxWUFYUDBUa0hiaWxrY0VHWTRLQ0VpOVlvcWFBR3lMTk1ST1RNM1JGaExIb29RbWNsc1h2eUxMMkd3R3hza3dOTzYiLCJtYWMiOiIwYzJhZmE2ZjExZDdlOWQxZTc0NWI0NTkxNjIyYzYwZTBjMGY5MjY2YzJhMWFlYTAyY2U0N2NkOGNlMThhYTYzIn0%3D; CASTGC=TGT-376278-l9jlwl-sSqC4VftoiguGWcuelsINlxnlu4osMWXwTvyXx-MnalyBC-B8f2QN9s-Ocss46b4b91a66cb',
}

# re7=requests.get(url=url7,headers=header7,allow_redirects=False)
# print(re7.cookies)
# print(re7.status_code)
# header3={
#     "Host": "yqfk.bjut.edu.cn",
#     "Connection": "keep-alive",
#     "Cache-Control": "max-age=0",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-User": "?1",
#     "Sec-Fetch-Dest": "document",
#     "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "Windows",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Cookie": "XSRF-TOKEN=eyJpdiI6IjZEQWJCVmdsMHNNeW9DT3NPMDBxTGc9PSIsInZhbHVlIjoibUZKOHB5TGxEWitzazRBR3RXNU9veTZCdW10dkc5V1k5Mm8vZXF4cmpzektDZTd4Q2dYeGRTL1FOTlpxc2lYOG53bzZ1RGdvL1ZwMHRZTE5wU09jSHZDNlBFNGNNcnBVQjVaT0EvTERQVmZIS0RrZzk2N0l6Y29DWS9sbUlDMWkiLCJtYWMiOiIwODk4YzJmNDdiOGEyMjA3NmQ4YzEzMjhlN2RjYTYyZGI2NzM0ZDUzZTUzMGI1Nzg3MDE1MzQwNDVmODc3NWI2In0"
# }
# print("###########################")
# url3='https://yqfk.bjut.edu.cn/api/login/pages-index-index?login=1&code=e452781416d4624ee23e0cf7d6404edb&state=STATE'
# result3=requests.get(url=url3,headers=header3,verify=False)
# print(result3.status_code)
# print(result3.headers)
