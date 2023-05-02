import streamlit as st

# 현재 페이지 번호를 저장할 session_state 변수 초기화
if 'page_num' not in st.session_state:
    st.session_state.page_num = 1

# 페이지 1 표시
if st.session_state.page_num == 1:
    st.write('This is Page 1.')

if st.session_state.page_num == 1:   
    st.subheader("어디에서 사고가 나셨나요?")
    # 클릭박스를 생성할 항목 리스트
    items = ['주차장', '횡단보도', '인도', '어린이 보호구역', '터널', '일방통행', '하이패스', '고속도로']

    # 클릭 여부를 저장할 리스트, 초기값은 False로 설정
    clicked_items = [False] * len(items)

    # 클릭박스 생성
    for i, item in enumerate(items):
        clicked_items[i] = st.button(item, key=i, help=f'{i}번째 항목')

    if st.button('기타'):
        # 텍스트 입력
        text_input = st.text_input('기타 위치를 알려주세요')
        # 입력된 텍스트 출력
        st.write('입력된 텍스트:', text_input)

    # 클릭된 항목 출력
    clicked_item_names = [item for i, item in enumerate(items) if clicked_items[i]]
    st.write(f'클릭된 항목: {", ".join(clicked_item_names)}')


    # 페이지 이동 버튼 생성
    if st.button('Go to Page 2'):
        # 현재 페이지 번호를 2로 업데이트하고, 페이지를 재로드
        st.session_state.page_num = 2
        st.experimental_rerun()





# 페이지 2 표시
if st.session_state.page_num == 2:
    st.write('This is Page 2.')

# 현재 페이지 번호를 저장할 session_state 변수 초기화
if 'page_num' not in st.session_state:
    st.session_state.page_num = 2

if st.session_state.page_num == 2:   
    st.subheader("무엇과 사고가 났나요?")
    # 클릭박스를 생성할 항목 리스트
    items = ['사람', '자전거', '오토바이', '킥보드', '킥보드', '동물을', '버스', '택시','트럭','가로수','화물차']

    # 클릭 여부를 저장할 리스트, 초기값은 False로 설정
    clicked_items = [False] * len(items)

    # 클릭박스 생성
    for i, item in enumerate(items):
        clicked_items[i] = st.button(item, key=i, help=f'{i}번째 항목')

    if st.button('기타'):
        # 텍스트 입력
        text_input = st.text_input('기타 대상을 알려주세요')
        # 입력된 텍스트 출력
        st.write('입력된 텍스트:', text_input)

    # 클릭된 항목 출력
    clicked_item_names = [item for i, item in enumerate(items) if clicked_items[i]]
    st.write(f'클릭된 항목: {", ".join(clicked_item_names)}')


    # 페이지 이동 버튼 생성
    if st.button('Go to Page 3'):
        # 현재 페이지 번호를 2로 업데이트하고, 페이지를 재로드
        st.session_state.page_num = 3
        st.experimental_rerun()

    # 페이지 이동 버튼 생성
    if st.button('back to Page 1'):
        # 현재 페이지 번호를 2로 업데이트하고, 페이지를 재로드
        st.session_state.page_num = 1
        st.experimental_rerun()









# 페이지 3 표시
if st.session_state.page_num == 3:
    st.write('This is Page 3.')

if st.session_state.page_num == 3:   
    st.subheader("어떻게 사고가 난 건가요?")
    items = ['직진', '끼어들다가', '과속하다가', '차선변경하다가', '보복운전', '전방주시태만', '음주운전', '운전미숙','졸다가','급발진','급제동']

    # 체크 여부를 저장할 리스트, 초기값은 False로 설정
    checked_items = [False] * len(items)

    # 체크박스 생성
    for i, item in enumerate(items):
        checked_items[i] = st.checkbox(item, value=checked_items[i])

    # 체크된 항목 출력
    checked_item_names = [item for i, item in enumerate(items) if checked_items[i]]
    st.write(f'체크된 항목: {", ".join(checked_item_names)}')

    if st.button('기타'):
        # 텍스트 입력
        text_input = st.text_input('기타 상황을 알려주세요')
        # 입력된 텍스트 출력
        st.write('입력된 텍스트:', text_input)

    # 페이지 이동 버튼 생성
    if st.button('Go to Page 4'):
        st.session_state.page_num = 4
        st.experimental_rerun()

    # 페이지 이동 버튼 생성
    if st.button('back to Page 2'):
        st.session_state.page_num = 2
        st.experimental_rerun()





# 페이지 4 표시
if st.session_state.page_num == 4:
    st.write('This is Page 4.')

if st.session_state.page_num == 4:   
    st.subheader("날씨는 어땠어요?")
    items = ['비내렸어요', '눈내렸어요', '낮', '밤', '어슴푸레']

    # 체크 여부를 저장할 리스트, 초기값은 False로 설정
    checked_items = [False] * len(items)

    # 체크박스 생성
    for i, item in enumerate(items):
        checked_items[i] = st.checkbox(item, value=checked_items[i])

    # 체크된 항목 출력
    checked_item_names = [item for i, item in enumerate(items) if checked_items[i]]
    st.write(f'체크된 항목: {", ".join(checked_item_names)}')

    if st.button('기타'):
        # 텍스트 입력
        text_input = st.text_input('기타 날씨를 알려주세요')
        # 입력된 텍스트 출력
        st.write('입력된 텍스트:', text_input)

    # 페이지 이동 버튼 생성
    if st.button('Go to Page 5'):
        st.session_state.page_num = 5 
        st.experimental_rerun()

    # 페이지 이동 버튼 생성
    if st.button('back to Page 3'):
        st.session_state.page_num = 3
        st.experimental_rerun()






# 페이지 5 표시
if st.session_state.page_num == 5:
    st.write('This is Page 5.')

if st.session_state.page_num == 5:   
    st.subheader("상황을 설명해주세요")
    items = ['무단횡단', '우회전', '좌회전', '문콕', '주차', '안전거리 미확보', '중앙선 침범', '실선', '이중실선', '빨간불', '주황불', '초록불']

    # 체크 여부를 저장할 리스트, 초기값은 False로 설정
    checked_items = [False] * len(items)

    # 체크박스 생성
    for i, item in enumerate(items):
        checked_items[i] = st.checkbox(item, value=checked_items[i])

    # 체크된 항목 출력
    checked_item_names = [item for i, item in enumerate(items) if checked_items[i]]
    st.write(f'체크된 항목: {", ".join(checked_item_names)}')

    if st.button('기타'):
        # 텍스트 입력
        text_input = st.text_input('기타 상황을 알려주세요')
        # 입력된 텍스트 출력
        st.write('입력된 텍스트:', text_input)

    # 페이지 이동 버튼 생성
    if st.button('Go to Page 6'):
        st.session_state.page_num = 6 
        st.experimental_rerun()

    # 페이지 이동 버튼 생성
    if st.button('back to Page 4'):
        st.session_state.page_num = 4
        st.experimental_rerun()



# 페이지 6 표시
if st.session_state.page_num == 6:
    st.write('This is Page 6.')

if st.session_state.page_num == 6:   
    st.subheader("기타는 무엇이 있었을까요?")
    items = ['혼자', '뒤에서', '옆에서', '사각지대', '적재물', '파편', '렌터카']

    # 체크 여부를 저장할 리스트, 초기값은 False로 설정
    checked_items = [False] * len(items)

    # 체크박스 생성
    for i, item in enumerate(items):
        checked_items[i] = st.checkbox(item, value=checked_items[i])

    # 체크된 항목 출력
    checked_item_names = [item for i, item in enumerate(items) if checked_items[i]]
    st.write(f'체크된 항목: {", ".join(checked_item_names)}')


    # 페이지 이동 버튼 생성
    if st.button(' 다음 '):
        st.session_state.page_num = 7 
        st.experimental_rerun()

    # 페이지 이동 버튼 생성
    if st.button('back to Page 5'):
        st.session_state.page_num = 5
        st.experimental_rerun()




# 페이지 7 표시
if st.session_state.page_num == 7:
    st.write('This is Page 7.')
    st.subheader("사진을 업로드해주세요.")


    # 파일 업로드
    image_file = st.file_uploader("이미지 업로드", type=["jpg", "jpeg", "png"])

    # 이미지 보여주기
    if image_file is not None:
        st.image(image_file, caption='Uploaded Image.', use_column_width=True)


    # 페이지 이동 버튼 생성
    if st.button(' 다음 없음 누르지 마셈'):
        st.session_state.page_num = 7 
        st.experimental_rerun()

    # 페이지 이동 버튼 생성
    if st.button('이전'):
        st.session_state.page_num = 5
        st.experimental_rerun()