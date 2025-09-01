import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# 구글시트 연결
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file"]


creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)


# 시트 열기
SHEET_URL = "https://docs.google.com/spreadsheets/d/1OscAAla05H4mrkIGoT81_O0V0B4N_oyU80MzZDnOlcE/edit#gid=0"
sheet = client.open_by_url(SHEET_URL).sheet1


# ------------------ Streamlit UI ------------------
st.title("📋 구글 시트 연동 연습")


# 1. 이름 입력 및 기록
name = st.text_input("이름을 입력하세요")


if st.button("기록"):
    if name.strip() != "":
        sheet.append_row([name])
        st.success(f"{name}님이 기록되었습니다!")
    else:
        st.warning("이름을 입력해주세요.")


# 2. 기록 초기화
if st.button("초기화"):
    sheet.clear()
    st.success("모든 기록이 초기화되었습니다!")


# 3. 기록된 데이터 표시
st.subheader("기록된 데이터")
data = sheet.get_all_records()
df = pd.DataFrame(data)
st.dataframe(df)
