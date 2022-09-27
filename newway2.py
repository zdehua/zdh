import requests
se=requests.session()
header1={
    "Host": "yqfk.bjut.edu.cn",
    "Connection": "keep-alive",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "XSRF-TOKEN=eyJpdiI6IitZMXpjSGVkV25kczJPN0RFcXdKcWc9PSIsInZhbHVlIjoiUDUzeWZPY1lSNXcweDJCUDlHT1RvWU1RVGVPSVU4aDk1WFl2cnhjdVlNK1VHOUJ4WHB0NXlTenhTSUxMZXdkUHN5ejJHa3d0ZHQ4MmJaRkhHZmUyNzVkUWVrZXJIcHNoa3RlWVAvR2ZzbUFhU2JFSU5TMzhuQy9BaExYYURwcWEiLCJtYWMiOiJmMzk0Y2YyNzU5ZmYzODIxZDZlNmM3NTNhNzBmYmI3MjU3ZThiN2E4ZGZkYzdlMjE2YjAxY2I0ZjBiZmYzZDgyIn0%3D; _session=eyJpdiI6ImtuL2pKZXBxYytMUXNxbXBPYkI4Q0E9PSIsInZhbHVlIjoiczB2MHkzdStaU203SnRLdjhNOURBNllkSFZEQy9SaGFmaUw2emJlWUw4VHM5bkxZdTZPbC9TVUNIeDFTdFJNdHk2V2g3Y0FwL0tmNFBBejJaZWZiZ2p2WUY5bUhWT2ZNeWxnZDBFZGE0Mk16K0tuWnBuSElkS1o1RGRCSXlZU2YiLCJtYWMiOiIxYmI1YmZhNTk5NmJmMzU2ZGE5NTNiYmI1YTljM2Y4MWI2YTU4YTU5NjQzMTY2NTgyNDE0MzA2ZjJjMGFlYmUxIn0%3D",
}
url1='https://yqfk.bjut.edu.cn/'
result=se.get(url=url1,headers=header1,verify=False,allow_redirects=False)
cooktext=result.headers['Set-Cookie']
XSRF=cooktext[cooktext.find('XSRF-TOKEN='):cooktext.find(' expires=Sat')]
print(XSRF)
tempcook=cooktext[cooktext.find(' expires=Sat')+10:]
print()
session=tempcook[tempcook.find('_session'):tempcook.find(' expires=')]
print(session)
print("###########")
print(result.status_code)

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
    'Cookie': XSRF+" "+session+" "+Gcook
}

url8='https://yqfk.bjut.edu.cn/ '
cook2=XSRF+" "+session+" "+Gcook
print(cook2)
header8={
    "Host": "yqfk.bjut.edu.cn",
    "Connection": "keep-alive",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "Authorization": "Bearer",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": "Windows",
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://yqfk.bjut.edu.cn/web/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    'Cookie':'XSRF-TOKEN=eyJpdiI6InpzdlVtTmJZZE1ra1c0aTlRQU00d2c9PSIsInZhbHVlIjoidEJmZ0NDeVNYVHljeTNFZnJaMG1rbmlPdlI3UG5jMGJzeUdzd01UbGFJZzVTay9oWXVSeFVHMXlCdVR0V0RjVVVUNnhqRkloSnZTN08ybkJ1V3pPbUpBTkE4ZFVmditHS0w4MDFmdHFtd2RLK2kzeUpleEExVmo2RHN5ZHJVek0iLCJtYWMiOiJjNTQ1Y2ZjNzRlNjQ5MzdlZGJkMjg5NTkwNjI0YjAwNmJmNDc2MjQwYTMxZTFhZTUyNGQ3MjVkZTU1YmIwOWJiIn0%3D; _session=eyJpdiI6InpDa3IrQ0tuT0lBeC9XcUtYbC9xbWc9PSIsInZhbHVlIjoiVkI5Syt2dGpFWWtLYkhsQVpLL3VHeEM0dDdTZ1NOSGJsZlZYVnlaWHJpYTVLVkcrVmlLOVB2ODh6T29QalFab2ZkY2tUcW1JRDFXaGpUcEJLVS9KMERPczlDTmRPQ3ZRMkxxcmJSa2FSejBhcTBtU2U1cVFMcTA5UmRkUEFyTVEiLCJtYWMiOiI4NzIwODQzNjZlODRlZWY4NzFjM2ZiZDdmNTk0M2E4NjBjZTY2ZjA4ODQ5MDRmMGE4ODFjZGFlOTkxYzZiZmJjIn0%3D; CASTGC=TGT-21568-uTPXrgdC5DT4T7oupRWePjhqLz-LTmYE9-xOinA4gmdp7Tv67Pm2vKKHHbBSqSJH-4sbc8e4494d89c'

}



re7=requests.get(url=url8,headers=header8,allow_redirects=False,verify=False)
print(re7.status_code)
print(re7.text)