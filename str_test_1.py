import streamlit as st

st.title('Hello Streamlit')

st.title('박소훈 바보')
st.header('김태혁 바보')
st.subheader('박민이 바보')

col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
  # column 1 에 담을 내용
  st.title('강민성은 컬럼')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  #st.checkbox('this is checkbox1 in col2 ')


# with 구문 말고 다르게 사용 가능 
col1.subheader(' i am column1  subheader !! ')
col2.checkbox('this is checkbox2 in col2 ') 
#=>위에 with col2: 안의 내용과 같은 기능을합니다

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

with tab1:
  #tab A 를 누르면 표시될 내용
  st.write('hello')
    
with tab2:
  #tab B를 누르면 표시될 내용 
  st.write('hi')

  #st.sidebar는 

st.sidebar.title('this is sidebar')
st.sidebar.checkbox('체크박스에 표시될 문구')
# 사이드바에 체크박스, 버튼등 추가할 수 있습니다! 


from PIL import Image

#PIL 패키지에 이미지 모듈을 통해 이미지 열기 
# Image.open('이미지 경로')
zarathu_img = Image.open('다운로드.jfif')

col1,col2 = st.columns([2,3])

with col1 :
  # column 1 에 담을 내용
  st.title('here is column1')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')


# 컬럼2에 불러온 사진 표시하기
col2.image(zarathu_img)

import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
import streamlit as st


iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 


species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

def mapp_species(x):
  return species_dict[x]


df['species'] = df['species'].apply(mapp_species)
print(df)




# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title('Iris Species🌸')

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_species = st.sidebar.selectbox(
    '확인하고 싶은 종을 선택하세요',
    ['setosa','versicolor','virginica']
)
# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
tmp_df = df[df['species']== select_species]
# 선택한 종의 맨 처음 5행을 보여줍니다 
st.table(tmp_df.head())


# 여러개 선택할 수 있을 때는 multiselect를 이용하실 수 있습니다 
# return : list
select_multi_species = st.sidebar.multiselect(
    '확인하고자 하는 종을 선택해 주세요. 복수선택가능',
    ['setosa','versicolor','virginica']

)

# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
tmp_df = df[df['species'].isin(select_multi_species)]
# 선택한 종들의 결과표를 나타냅니다.  
st.table(tmp_df)



#지도 위에 표시될 점 좌표 값을 위도경도에 담습니다 .
base_position =  [37.5073423, 127.0572734]
#중심점의 위도, 경도 좌표를 리스트에 담습니다.

# base_position에, 랜덤으로 생성한 값을 더하여 5개의 좌표를 데이터 프레임으로 생성하였고,
# 컬럼명은 위도 :lat  경도 lon으로 지정하였습니다. 


map_data = pd.DataFrame(
    np.random.randn(5, 1) / [20, 20] + base_position , 
    columns=['lat', 'lon'])
# map data 생성 : 위치와 경도 

print(map_data)

st.code('st.map(map_data)')
# 웹사이트에 어떤 코드인지 표시해주기 
st.subheader('Map of Data ')
# 제목 생성 
st.map(map_data)
# 지도 생성 


import time 

# 방법 1 progress bar 
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.05)
  # 0.05 초 마다 1씩증가

st.balloons()
# 시간 다 되면 풍선 이펙트 보여주기 