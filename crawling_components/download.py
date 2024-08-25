import requests
import os 


def download_images(search_word, images) -> int:
    base_path = os.path.expanduser(f"~/crawling_data_storage/{search_word}")
    
    # 폴더가 없을 시 생성 
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    image_number = 0

    for image in images: 
        try: 
            response = requests.get(image) 
            if response.status_code == 200:
                # 이미지 파일 저장 경로 생성
                file_path = os.path.join(base_path, f"{search_word}_{image_number}.jpg")
                with open(file_path, "wb") as file:
                    file.write(response.content)
                image_number += 1
            else:
                print(f"이미지 다운로드에 실패하였습니다. Status code: {response.status_code}")
        except: 
            pass 
    
    return image_number
