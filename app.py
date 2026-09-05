import pandas as pd
import streamlit as st

# 페이지 설정 (와이드 모드)
st.set_page_config(
    page_title="AFK Global Risk & Weather Radar", page_icon="🌍", layout="wide"
)

# 커스텀 스타일
st.markdown("""
    <style>
    .stApp { background-color: #f4f4f5; color: #18181b; }
    .main-header { background-color: #0f172a; padding: 20px; border-radius: 6px; color: #38bdf8; font-weight: 900; font-size: 24px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; }
    .card { background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #e4e4e7; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-bottom: 15px; }
    .sub-header { font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 상단 배너
st.markdown("""
    <div class="main-header">
        <span>🌍 AFK GLOBAL WEATHER & GEO-RISK RADAR</span>
        <span style="font-size: 13px; background-color: #38bdf8; color: #0f172a; padding: 4px 10px; border-radius: 4px; font-weight: 700;">LIVE RADAR v1.0</span>
    </div>
""", unsafe_allow_html=True)

# 주요 글로벌 항만 및 물류 거점 좌표 데이터 (위도, 경도, 리스크 상태)
port_data = pd.DataFrame({
    "port": [
        "상하이항 (중국)",
        "닝보항 (중국)",
        "부산항 (한국)",
        "로스앤젤레스 (미주)",
        "로테르담 (유럽)",
        "싱가포르항 (동남아)",
    ],
    "lat": [31.2304, 29.8683, 35.1796, 33.7420, 51.9244, 1.3521],
    "lon": [121.4737, 121.5440, 129.0756, -118.2437, 4.4777, 103.8198],
    "status": ["혼잡 (주의)", "지연", "정상", "정상", "혼잡 (주의)", "정상"],
    "risk_level": [2, 3, 1, 1, 2, 1],  # 1: 안정, 2: 주의, 3: 위험
    "weather": [
        "태풍 주의보",
        "풍랑 경보",
        "맑음",
        "맑음",
        "강풍 주의",
        "스콜",
    ],
})

col1, col2 = st.columns([2, 1])

with col1:
  st.markdown(
      '<div class="card"><div class="sub-header">🗺️ 전 세계 주요 항만 기상 및'
      " 리스크 레이더 맵</div>",
      unsafe_allow_html=True,
  )

  # 스트림릿 내장 맵 기능으로 세계지도 위에 항만 위치 핀포인트 표시
  # lat, lon 데이터를 기반으로 자동으로 세계지도를 렌더링합니다.
  st.map(
      port_data,
      latitude="lat",
      longitude="lon",
      size=50,
      color="#0f172a",
      zoom=1,
  )

  st.markdown(
      '<p style="font-size: 12px; color: #71717a; margin-top: 10px;">* 핀을'
      " 클릭하거나 확대하여 전 세계 주요 물류 거점의 위치를 확인할 수"
      " 있습니다.</p>",
      unsafe_allow_html=True,
  )
  st.markdown("</div>", unsafe_allow_html=True)

with col2:
  st.markdown(
      '<div class="card"><div class="sub-header">🚨 거점별 실시간 리스크'
      " 현황판</div>",
      unsafe_allow_html=True,
  )

  for index, row in port_data.iterrows():
    badge_color = (
        "#166534"
        if row["risk_level"] == 1
        else ("#b45309" if row["risk_level"] == 2 else "#991b1b")
    )
    st.markdown(
        f"""
            <div style="background-color: #fafafa; padding: 10px; border-radius: 6px; margin-bottom: 8px; border-left: 4px solid {badge_color};">
                <b>{row['port']}</b><br>
                <span style="font-size: 12px; color: #52525b;">날씨: <b>{row['weather']}</b> | 상태: <b>{row['status']}</b></span>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown("</div>", unsafe_allow_html=True)

# 하단 상세 데이터 테이블
st.markdown(
    '<div class="card"><div class="sub-header">📋 항만별 상세 인텔리전스 데이터'
    " 리포트</div>",
    unsafe_allow_html=True,
)
st.dataframe(
    port_data[["port", "status", "weather", "lat", "lon"]],
    use_container_width=True,
    hide_index=True,
)
st.markdown("</div>", unsafe_allow_html=True)
