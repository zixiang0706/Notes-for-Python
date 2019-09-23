# get
import requests
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
kw = {
    "wd": "python"
}
proxies = {
    "https":"125.25.45.167:56628"
}
url = "http://www.baidu.com/s"
response = requests.get(url, headers=headers, params=kw, proxies=proxies)
print(response)
print(response.request.url)