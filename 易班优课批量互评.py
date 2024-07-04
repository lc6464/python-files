import requests
from bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor
from typing import List

# 分数
SCORE = input("请输入分数：")

# 评语
CONTENT = input("请输入评语：")

# Cookies 字符串
COOKIES_STR = input("请粘贴 Cookies：")

# 解析 Cookies 字符串为字典
def parse_cookies(cookies_str):
    return dict(item.split("=") for item in cookies_str.split("; "))

# 存储解析后的 Cookies
COOKIES = parse_cookies(COOKIES_STR)

def review(entry: str) -> None:
    # 获取所有 table a 的 href
    response = requests.get(entry, cookies=COOKIES)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 获取作业标题
    title_elem = soup.select_one('.hw-title')
    title = title_elem.text.strip() if title_elem else "未知作业"
    title = re.sub(r'^作业标题：', '', title)
    
    links = [a['href'] for a in soup.select('table a')]

    # 获取 CSRF token
    csrf_token = COOKIES['csrftoken']

    def process_link(link):
        # 准备 POST 数据
        data = {
            'score': SCORE,
            'content': CONTENT,
            'csrfmiddlewaretoken': csrf_token
        }
        
        # 准备请求头
        headers = {
            'X-Csrftoken': csrf_token
        }
        
        # 发送 POST 请求
        full_url = f"https://www.yooc.me{link}"
        response = requests.post(full_url, data=data, cookies=COOKIES, headers=headers)
        
        # 从 URL 中提取 ID
        id_match = re.search(r'/hu/(\d+)$', link)
        id = id_match.group(1) if id_match else "未知ID"
        
        # 检查请求是否成功
        if response.status_code == 200:
            print(f"成功发送 POST 请求到 ID: {id}")
        else:
            print(f"发送 POST 请求到 ID: {id} 失败，状态码: {response.status_code}")

    print(f"开始评阅：{title}")

    # 使用线程池并发处理每个链接
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_link, links)

    print(f"完成评阅：{title}")

def get_review_entries(course_id: str) -> List[str]:
    url = f"https://www.yooc.me/group/{course_id}/homeworks"
    response = requests.get(url, cookies=COOKIES)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    review_links = soup.select('.board-handler a:nth-of-type(2)')
    if review_links:
        return [link['href'] for link in review_links]
    else:
        raise ValueError("无法找到评阅链接")

def main():
    # 通过用户输入获取课程 ID
    course_id = input("请输入课程 ID：")
    
    try:
        # 获取评阅入口 URL 列表
        entry_urls = get_review_entries(course_id)
        print(f"找到 {len(entry_urls)} 个评阅入口")
        
        # 执行评阅
        for i, entry_url in enumerate(entry_urls, 1):
            print(f"正在处理第 {i} 个评阅入口: {entry_url}")
            review(entry_url)
            
    except ValueError as e:
        print(f"错误: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")

if __name__ == "__main__":
    main()