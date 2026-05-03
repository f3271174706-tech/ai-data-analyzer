import requests
import csv

# 请求URL
url = "https://www.jxau.edu.cn/aop_component//webber/search/search/search/queryPage?r=0.8078282714063022"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

# 请求参数
data = {
    "keyWord": "计信院",
    "owner": "2043148059",  # 这个是从你提供的信息中得到的
    "size": 10,
    "total": 16
}

# 发起POST请求
response = requests.post(url, json=data, headers=headers)

# 输出查看返回的原始数据
print(response.text)

# 假设返回的JSON数据格式是 {"data": [...]}, 你可以修改以符合返回格式
json_data = response.json()

# 假设我们需要抓取的字段包括标题、链接、时间等
records = json_data.get("data", [])

# 保存为CSV文件
with open("result.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["标题", "链接", "时间"])  # 这里根据返回的字段调整

    for item in records:
        title = item.get("title")  # 假设字段是title
        link = item.get("url")     # 假设字段是url
        time = item.get("publishTime")  # 假设字段是publishTime

        writer.writerow([title, link, time])

print("爬取完成！")