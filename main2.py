import requests
from bs4 import BeautifulSoup
import re

def get_signkai_urls(page_url):
    try:
        # ページのHTMLを取得
        response = requests.get(page_url)
        response.raise_for_status()

        # BeautifulSoupを使ってHTMLを解析
        soup = BeautifulSoup(response.content, 'html.parser')

        # URLを抽出
        signkai_urls = []
        for link in soup.find_all('a', href=True):
            url = link['href']
            pattern = r"\d{4}/\d{4}_[\w\d\s\W]+\.html"
            if re.match(pattern, url):
                signkai_url = f"http://www.kaitorimax.com/signkai/{url}"
                signkai_urls.append(signkai_url)

        return signkai_urls

    except Exception as e:
        print(f"エラー: {e}")
        return []
    
def get_pic_urls(page_url):
    try:
        # ページのHTMLを取得
        response = requests.get(page_url)
        response.raise_for_status()

        # BeautifulSoupを使ってHTMLを解析
        soup = BeautifulSoup(response.content, 'html.parser')

        parts = page_url.rsplit("/", 1)
        modified_url = parts[0]

        pic_urls = []
        for link in soup.find_all('a', href=True):
            url = link['href']
            pattern = r"img/\d+\.jpg"
            if re.match(pattern, url):
                pic_url = f"{modified_url}/{url}"
                pic_urls.append(pic_url)

        return pic_urls

    except Exception as e:
        print(f"エラー: {e}")
        return []

if __name__ == "__main__":
    target_page_url = "http://www.kaitorimax.com/signkai/signkai.html"
    signkai_urls = get_signkai_urls(target_page_url)

    if signkai_urls:
        print("過去のサイン会のURL:")
        for url in signkai_urls:
            pics = get_pic_urls(url)
            result = {
              'sign_kai_url': url,
              'images': pics
            }
            print(result)
    else:
        print("過去のサイン会のURLは見つかりませんでした。")