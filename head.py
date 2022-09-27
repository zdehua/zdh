import requests
url8='https://yqfk.bjut.edu.cn/ '


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

ccok={'XSRF-TOKEN':'eyJpdiI6InpzdlVtTmJZZE1ra1c0aTlRQU00d2c9PSIsInZhbHVlIjoidEJmZ0NDeVNYVHljeTNFZnJaMG1rbmlPdlI3UG5jMGJzeUdzd01UbGFJZzVTay9oWXVSeFVHMXlCdVR0V0RjVVVUNnhqRkloSnZTN08ybkJ1V3pPbUpBTkE4ZFVmditHS0w4MDFmdHFtd2RLK2kzeUpleEExVmo2RHN5ZHJVek0iLCJtYWMiOiJjNTQ1Y2ZjNzRlNjQ5MzdlZGJkMjg5NTkwNjI0YjAwNmJmNDc2MjQwYTMxZTFhZTUyNGQ3MjVkZTU1YmIwOWJiIn0%3D',
      '_session':'eyJpdiI6InpDa3IrQ0tuT0lBeC9XcUtYbC9xbWc9PSIsInZhbHVlIjoiVkI5Syt2dGpFWWtLYkhsQVpLL3VHeEM0dDdTZ1NOSGJsZlZYVnlaWHJpYTVLVkcrVmlLOVB2ODh6T29QalFab2ZkY2tUcW1JRDFXaGpUcEJLVS9KMERPczlDTmRPQ3ZRMkxxcmJSa2FSejBhcTBtU2U1cVFMcTA5UmRkUEFyTVEiLCJtYWMiOiI4NzIwODQzNjZlODRlZWY4NzFjM2ZiZDdmNTk0M2E4NjBjZTY2ZjA4ODQ5MDRmMGE4ODFjZGFlOTkxYzZiZmJjIn0%3D',
      'CASTGC':'TGT-21568-uTPXrgdC5DT4T7oupRWePjhqLz-LTmYE9-xOinA4gmdp7Tv67Pm2vKKHHbBSqSJH-4sbc8e4494d89c'
      }
re7=requests.get(url=url8,cookies=ccok,verify=False)
print(re7.status_code)
print(re7.text)