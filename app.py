#import streamlit as st
#st.markdown("# 앱 UI 만들기")
#user_id = st.text_input("이름", placeholder="이름")
#cla = st.number_input("반", min_value=1, max_value=10, value=1)
#grade = st.radio("학년", ["1", "2", "3"], horizontal=True)
#level = st.select_slider("난이도",options=["매우 쉬움", "쉬움", "보통", "어려움", "매우 어려움"],value="보통")
#score = st.slider("점수", 0, 100, 50)
#text1 = st.text_area("소감", placeholder = "소감입니다")
#
#if st.button("확인"):
#    st.success(f"{user_id}/{grade}학년/{cla}반/{level}")
#    st.markdown(f"점수: {score}")
#    st.info(f"소감:{text1}")


import treamlit as st
with st.sidebar:
    st.header("프로필")
    user_name = st.text_input("닉네임")
    weather = st.selectbox("오늘 날씨", ["맑음", "흐림", "비/눈", "매우 추움"])
    st.markdown("---")
    st.info(f"반가워요, {user_name}님! 오늘 날씨는 '{weather}'이네요.")

st.title("👗 AI 코디 메이커")
st.write("사이드바에서 날씨를 먼저 선택하고 코디를 시작하세요!")






