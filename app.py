import streamlit as st
#
#st.markdown("# AI 챗봇 만들기")
#st.markdown("---")
#st.markdown("## 질문을 하시면 AI 친구가 응답합니다.")
#st.header("1. 기본 정보 입력")
#user_id = st.text_input("아이디(ID)를 입력하세요", placeholder="example_user")
#age = st.number_input("나이를 입력하세요", min_value=1, max_value=100, value=17)
#question = st.text_area("AI에게 보낼 질문을 입력하세요", placeholder="여기에 질문을 작성해 주세요.")
#
#st.header("2. 챗봇 설정")
#ai_model = st.radio("사용할 AI 모델을 선택하세요", ["GPT-4", "Claude 3", "Gemini Pro"], horizontal=True)
#tone = st.selectbox("답변의 말투를 골라주세요", ["친절하게", "냉철하게", "유머러스하게"])
#features = st.multiselect("추가 기능을 선택하세요", ["이미지 생성", "웹 검색", "코드 분석", "번역"])
#creativity = st.slider("AI의 창의성 수준을 설정하세요", 0, 100, 50)
#ai_speed = st.select_slider("응답 처리 속도를 선택하세요",options=["매우 느림", "느림", "보통", "빠름", "실시간"],value="보통")
#agree = st.checkbox("개인정보 수집 및 AI 학습 이용에 동의합니다.")
#st.markdown("---")
#
#if st.button("질문 전송하기"):
#    if agree:
#        st.success(f"성공적으로 전송되었습니다! ({user_id}님)")
#        st.markdown(f"""
#        * **질문 내용:** {question}
#        * **선택 모델:** `{ai_model}` | **말투:** `{tone}`
#        * **활성화 기능:** {', '.join(features) if features else '없음'}
#        * **창의성:** `{creativity}%` | **처리 속도:** `{ai_speed}`
#        """)
#        
#        if age < 14:
#            st.info("참고: 14세 미만 사용자이므로 보호자 모드가 활성화됩니다.")
#   else:
#        st.error("⚠️ 동의 항목에 체크해야 전송이 가능합니다.")

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
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

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#with st.sidebar:
#    st.header("프로필")
#    user_name = st.text_input("닉네임")
#    weather = st.selectbox("오늘 날씨", ["맑음", "흐림", "비/눈", "매우 추움"])
#    st.markdown("---")
#    st.info(f"반가워요, {user_name}님! 오늘 날씨는 '{weather}'이네요.")
#
#st.title("👗 AI 코디 메이커")
#st.write("사이드바에서 날씨를 먼저 선택하고 코디를 시작하세요!")
#
#st.header("👕 아이템 조합하기")
#col1, col2 = st.columns(2)
#with col1:
#    st.subheader("상의")
#    top_type = st.radio("종류", ["후드티", "셔츠", "맨투맨", "반팔 티셔츠"])
#    top_color = st.select_slider("색상 톤", options=["밝음", "무난함", "어두움"])
#with col2:
#    st.subheader("하의")
#    bottom_type = st.radio("종류", ["청바지", "슬랙스", "트레이닝 팬츠", "반바지"])
#    bottom_color = st.select_slider("핏(Fit)", options=["슬림", "레귤러", "오버핏"])
#
#st.header("디테일 추가")
#tab1, tab2 = st.tabs(["신발", "액세서리"])
#with tab1:
#    st.write("오늘의 발걸음을 책임질 신발:")
#    shoes = st.selectbox("신발 선택", ["스니커즈", "운동화", "구두", "슬리퍼"])
#    with st.expander("신발 선택 팁 보기"):
#        st.info("너무 튀는 신발은 지양하도록 해요!")
#with tab2:
#    st.write("포인트 아이템:")
#    acc = st.multiselect("액세서리 추가", ["모자", "안경", "목걸이", "가방"])
#   with st.expander("액세서리 스타일링 팁 보기"):
#        st.warning("너무 많은 액세서리는 투머치가 될 수 있어요.")
#
#st.markdown("---")
#if st.button("코디 완성하기"):
#    with st.container(border=True):
#        st.subheader(f"{user_name}님의 오늘의 룩북")
#        st.write(f"오늘 같은 **{weather}** 날씨에는 이렇게 입어보세요!")
#        st.markdown(f"""
#        * **상의:** {top_color} {top_type}
#       * **하의:** {bottom_color} {bottom_type}
#        * **매칭:** {shoes}와 {', '.join(acc) if acc else '악세서리 없이 깔끔하게!'}
#        """)
#        st.success("오늘의 스타일링이 완성되었습니다! 자신 있게 외출하세요!")
#        
#        with st.expander("코디 연출 팁 영상 보기"):
#            st.video("https://www.youtube.com/watch?v=lkMZ8ytly1k")
#            st.write("전문가가 제안하는 코디 연출법을 참고해 보세요.")

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#st.markdown("# 파이썬 퀴즈 프로그램")
#with st.sidebar:
#    st.header("힌트 보기")
#    q1 = st.button("1번 문제")
#    q2 = st.button("2번 문제")
#    if q1:
#        st.markdown("라는걸 명심하세요!")
#    if q2:
#        st.markdown("라는걸 명심하세요!")
#st.subheader("첫번째 문제")
# with st.container(border=True):
#        st.markdown("n = int(input())")
#        st.markdown("""if n < 4:
#                            print("A")""")
#        st.markdown("""____ n > 8:
#                            print("B")""")
#        st.markdown("""else:
#                            print("C")""")
#
#with st.container(border=True):
#        st.markdown("9를 입력 --> B")
#        st.markdown("6을 입력 --> C")
#        st.markdown("""3을 입력 --> A
#                                    C""")
#st.subheader("두번째 문제")
# with st.container(border=True):

st.title("카운터 앱")
count = 0
if st.button("증가"):
    count += 1
st.markdown(f"##현재 숫자: `{count}`")















        
        

