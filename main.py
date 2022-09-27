import requests
import re
se=requests.session()
result=requests.get(url='https://xgxt.bjut.edu.cn/',verify=False,allow_redirects=False)
print(result.headers)
url1=result.headers['Location']
print(url1)
re2=se.get(url=url1,verify=False)
cook=re2.cookies
re_text=re2.text[1945:7392]

re_text=re_text[1:-1]
# re_text=re.sub(r'/',' ',re_text)
# re_text=re.sub(r'>',' ',re_text)
# re_text=re.sub(r'<',' ',re_text)
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

    "Origin": "https://cas.bjut.edu.cn",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",

    "Referer": "https://cas.bjut.edu.cn/login?service=https%3A%2F%2Fxgxt.bjut.edu.cn%2FwiseduIndex.jsp",

}
# re3=se.post(url=url1,cookies=cook,data=data2,verify=False)
re3=requests.post(url=url1,cookies=cook,data=data2,verify=False,allow_redirects=False)
print(re3.status_code)
print(re3.headers)





# print(re.headers['Location'])
