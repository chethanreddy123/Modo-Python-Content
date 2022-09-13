import string
import random
import streamlit as st


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

random.shuffle(characters)

st.title("Random Password Generator 💻")
st.subheader("Works Like Google Password Generator")

length = st.number_input('Enter the lenght of the passord ', min_value=5, value=15)


password = []
for i in range(length):
	password.append(random.choice(characters))

random.shuffle(password)

final_pass = "".join(password)

st.text_area("Your Randomly Generated Password", value=final_pass)



