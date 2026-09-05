import pandas as pd
import streamlit as st

# 페이지 설정 (와이드 모드)
st.set_page_config(
    page_title="AFK Global Geo-Risk & Delay Radar", page_icon="🚨", layout="wide"
)

# 커스텀 스타일 (다크 모드 레이더 콘솔 스타일)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .main-header { background-color: #1e293b; padding: 20px; border-radius: 8px; border: 1px solid #334155; color: #38bdf8; font-weight: 900; font-size: 24px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; }
    .card { background-color: #1e293b; padding: 20px; border-radius: 8px; border: 1px solid #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); margin-bottom: 15px; }
    .sub-header { font-size: 16px; font-weight: 700; color: #38bdf8; margin-bottom: 10px; }
    .risk-card-red { background-color: #450a0a; border: 1px solid #991b1b; padding: 12px; border-radius: 6px; margin-bottom: 10px; }
    .risk-card-orange { background-color: #451a03; border: 1px solid #9a3412; padding: 12px; border-radius: 6px; margin-bottom: 10px; }
    .risk-card-green { background-color: #052e16; border: 1px solid #166534; padding: 12px; border-radius: 6px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 상단 배너
st.markdown("""
    <div class="main-header">
        <span>🚨 AFK GLOBAL SUPPLY CHAIN DELAY & RISK RADAR</span>
        <span style="font-size: 13px; background-color: #ef4444; color: #ffffff; padding: 4px 10px; border-radius: 4px; font-weight: 700;">LIVE CRISIS MONITOR v2.0</span>
    </div>
""", unsafe_allow_html=True)

# 전 세계 주요 항만 실무 지연 데이터 (지연 일수, 원인, 심각도 포함)
port_risk_data = pd.DataFrame({
    "port": [
        "상하이항 (중국)",
        "닝보-주산항 (중국)",
        "부산항 (한국)",
        "로스앤젤레스항 (미주)",
        "로테르담항 (유럽)",
        "파나마 운하 통항",
    ],
    "lat": [31.2304, 29.8683, 35.1796, 33.7420, 51.9244, 9.1000],
    "lon": [121.4737, 121.5440, 129.0756, -118.2437, 4.4777, -79.7000],
    "status": ["심각 지연", "지연 주의", "정상 운영", "정상 운영", "혼잡", "통항 제한"],
    "delay_days": ["+7 ~ 10일", "+3 ~ 5일", "지연 없음", "지연 없음", "+3일", "+14일 우회"],
    "reason": [
        "성수기 물동량 폭증 및 야드 적체율 90% 초과",
        "국지적 기상 악화(풍랑 경보)로 인한 선적 일시 중단",
        "부두 하역 및 야드 회전율 원활",
        "터미널 철도 연계 원활, 대기 시간 단축",
        "부두 인력 파업 여파 및 하역 장비 점검 지연",
        "가뭄으로 인한 흘수 제한 및 일일 통항 척수 감축",
    ],
    "risk_level": ["red", "orange", "green", "green", "orange", "red"],
})

col_map, col_info = st.columns([2, 1])

with col_map:
  st.markdown(
      '<div class="card"><div class="sub-header">🗺️ 글로벌 공급망 실시간 리스크'
      " 레이더 맵</div>",
      unsafe_allow_html=True,
  )

  # 스트림릿 맵 시각화
  st.map(
      port_risk_data,
      latitude="lat",
      longitude="lon",
      size=60,
      zoom=1,
  )

  st.markdown(
      '<p style="font-size: 12px; color: #94a3b8; margin-top: 10px;">💡 <b>지도'
      " 활용 가이드</b>: 붉은색 및 주황색 마커가 표기된 거점은 현재 선적 및"
      " 입고 일정에 차질이 발생하고 있는 구간입니다.</p>",
      unsafe_allow_html=True,
  )
  st.markdown("</div>", unsafe_allow_html=True)

with col_info:
  st.markdown(
      '<div class="card"><div class="sub-header">⚡ 긴급 지연 거점 브리핑</div>',
      unsafe_allow_html=True,
  )

  # 지연 상태인 곳들만 필터링해서 상단에 긴급 브리핑 카드 노출
  for _, row in port_risk_data.iterrows():
    if row["risk_level"] == "red":
      st.markdown(
          f"""
                <div class="risk-card-red">
                    <b>🔴 {row['port']}</b><br>
                    <span style="font-size: 13px; color: #fca5a5;">지연: <b>{row['delay_days']}</b></span><br>
                    <span style="font-size: 12px; color: #cbd5e1;">원인: {row['reason']}</span>
                </div>
            """,
          unsafe_allow_html=True,
      )
    elif row["risk_level"] == "orange":
      st.markdown(
          f"""
                <div class="risk-card-orange">
                    <b>🟠 {row['port']}</b><br>
                    <span style="font-size: 13px; color: #fdba74;">지연: <b>{row['delay_days']}</b></span><br>
                    <span style="font-size: 12px; color: #cbd5e1;">원인: {row['reason']}</span>
                </div>
            """,
          unsafe_allow_html=True,
      )

  st.markdown("</div>", unsafe_allow_html=True)

# 하단 전체 항만 인텔리전스 테이블
st.markdown(
    '<div class="card"><div class="sub-header">📋 전 세계 주요 항만/운하별 상세'
    " 지연 리포트</div>",
    unsafe_allow_html=True,
)
st.dataframe(
    port_risk_data[["port", "status", "delay_days", "reason"]],
    use_container_width=True,
    hide_index=True,
)
st.markdown("</div>", unsafe_allow_html=True)
