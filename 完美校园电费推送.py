import requests
import json
import threading

# 获取电费数据，使用 POST 请求
def get_electricity_data(account):
    url = "https://xqh5.17wanxiao.com/smartWaterAndElectricityService/SWAEServlet"
    payload = {
        "param": json.dumps({"cmd": "getbindroom", "account": account}),
        "customercode": 973,
        "method": "getbindroom",
        "command": "JBSWaterElecService"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.json()

# 解析电费数据并获取 roomfullname 和 odd
def parse_electricity_data(data):
    if data["result_"] == "true":
        body = json.loads(data["body"])
        roomfullname = body["roomfullname"].split("_")
        odd = float(body["detaillist"][0]["odd"])
        return f"**{roomfullname[-1]}**", odd
    return None, None

# 根据电费余额选择合适的颜色
def get_color(odd):
    if odd < 30:
        return "warning"  # 橙红色
    elif odd < 60:
        return "comment"  # 灰色
    else:
        return "info"  # 绿色

# 生成微信通知内容
def generate_content(roomfullname, odd):
    if roomfullname and odd is not None:
        color = get_color(odd)
        return f"宿舍号：{roomfullname}\n剩余电量：<font color=\"{color}\">{odd} kWh</font>"
    else:
        return "宿舍号：<font color=\"warning\">**获取失败**</font>\n剩余电量：<font color=\"warning\">获取失败</font>"

# 推送数据到企业微信
def send_wechat_notification(content: str, key: str):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

# 电费数据线程类
class ElectricityDataThread(threading.Thread):
    def __init__(self, account, results, index):
        threading.Thread.__init__(self)
        self.account = account
        self.results = results
        self.index = index

    def run(self):
        data = get_electricity_data(self.account)
        roomfullname, odd = parse_electricity_data(data)
        content = generate_content(roomfullname, odd)
        self.results[self.index] = content

if __name__ == "__main__":
    with open("电费.json", encoding="utf-8") as f:
        groups = json.load(f)

    for group in groups:
        accounts = group['ids']
        all_content = "# 电费信息\n"
        results = [None] * len(accounts)

        threads = []
        for i, account in enumerate(accounts):
            thread = ElectricityDataThread(account, results, i)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        for content in results:
            all_content += content + "\n\n"

        # 去掉最后多余的空行
        all_content = all_content.strip()

        # 发送微信通知
        response = send_wechat_notification(all_content, group['key'])
        print("推送结果:", response)