import streamlit as st
import pandas


st.set_page_config("Welcome to TZO Foundation", layout="wide")

st.header("TZO Foundation")
website_description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(website_description)

st.subheader("Our Team")

content = pandas.read_csv("data.csv")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    for index, data in content[:4].iterrows():
        st.subheader(
            f"{data['first name'].title()} {data['last name'].title()} ")
        st.write(data["role"])
        st.image(f"assets/images/{data['image']}")

with col2:
    for index, data in content[4:8].iterrows():
        st.subheader(
            f"{data['first name'].title()} {data['last name'].title()} ")
        st.write(data["role"])
        st.image(f"assets/images/{data['image']}")

with col3:
    for index, data in content[8:].iterrows():
        st.subheader(
            f"{data['first name'].title()} {data['last name'].title()} ")
        st.write(data["role"])
        st.image(f"assets/images/{data['image']}")
