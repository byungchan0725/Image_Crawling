import streamlit as st 
from PIL import Image

# Crawling components 
from crawling_components.search import search_images as search
from crawling_components.download import download_images as download


# session_state
if 'start' not in st.session_state:
    st.session_state.start = None

if 'total_images' not in st.session_state:
    st.session_state.total_images = None


# Sidebar 
with st.sidebar:
    # pages의 허용 범위를 1 ~ 20으로 제한 *(API가 막힐 가능성)
    search_word = st.text_input("검색어")
    pages = st.number_input("페이지 수 설정", min_value=1, max_value=20) # int type 

    st.write("")

    # 경고 메시지 출력  
    if not search_word:
            st.error("""
                    아래 리스트를 확인해주세요.  
                    - 검색어를 지정하였나요? 
                    - Page 수를 지정하였나요?
                    """, icon="🚨")
    else: 
        # 모든 조건이 충족하면 st.session_state = True  
        # st.session_state가 True일 시 이미지 검색 
        st.session_state.start = True     


if st.session_state.start:
    images_list = search(search_word, pages)
    images_list = images_list[1:] # 처음 이미지의 형식이 .gif라서 제외  
    total_images = int(len(images_list)) # int 
    
    # 검색한 이미지가 맞는지 3개 정도만 출력 
    col1, col2, col3 = st.columns(3) 

    with col1:
        st.image(images_list[1])

    with col2:
        st.image(images_list[2])

    with col3:
        st.image(images_list[3])

    st.write("")
    st.write("")

    # 검색한 이미지의 결과를 보여줌 
    st.markdown(f"""
                검색어: :blue-background[{search_word}]에 해당하는 이미지를 :blue-background[{total_images}]개 찾았습니다.  

                - 이미지를 다운로드 하실려면 아래 버튼을 눌러주세요.  
                """)
    
    if st.button("다운로드"): 
        print(len(search_word))
        
        successful_downloads = download(search_word, images_list) # 다운로드 성공 이미지 
        failed_downloads = total_images - successful_downloads # 다운로드 실패 이미지 

        st.success(f"""
                이미지 다운로드에 성공하였습니다.  
                ( 실패: {abs(failed_downloads)}, 성공: {successful_downloads})
                """, icon="✅")
        
