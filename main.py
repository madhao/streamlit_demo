import streamlit as st
from streamlit_gsheets import GSheetsConnection


st.write("**SPY Open and Close Data**")
# url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"
url = "https://docs.google.com/spreadsheets/d/1CT3p-Bu5W1Bnet8EfjWQbEaCKSLXjF0mfi7VyqlkXk8/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)
st.dataframe(data)
