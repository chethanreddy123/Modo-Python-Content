import streamlit as st
import time


st.title("Welcome to the Streamlit Count-Down Timer!!")
st.subheader("Do Enter the below values...")
time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=25)
time_in_seconds = st.number_input('Enter the time in secs', min_value=0, max_value=60)
time_in_seconds = time_minutes * 60 + time_in_seconds

if st.button("START"):
        ts = time_in_seconds
        with st.empty():
            while ts:
                mins, secs = divmod(ts, 60)
                time_now = '{:02d}:{:02d}'.format(mins, secs)
                st.header(f"{time_now}")
                time.sleep(1)
                ts -= 1

