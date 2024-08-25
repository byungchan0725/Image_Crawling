import requests
from bs4 import BeautifulSoup


def set_base_url(search_word, pages):
    # search_word: str 
    # pages: int 
    base_url = f"https://www.google.com/search?tbm=isch&q={search_word}&start={pages}"
    return base_url


def search_images(search_word, pages): 
    base_url = set_base_url(search_word, pages)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # 이미지 저장 리스트 
    images = [] 

    for page in range(pages):
        url = base_url.format(start=page*20)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        result = soup.find_all("img")
        for img in result:
            img_url = img.get("src")
            if img_url:
                images.append(img_url)

    return images
