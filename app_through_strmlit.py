import streamlit as st
st.title("streamlit app of vgu")
st.text("welcome to our dashboard")
st.header("i am a header")
st.write("u can write",10+5)

name = st.text_input("Enter your name")
age = st.number_input("Enter your age:")
st.write("your name Is :",name,"your age is :",age)
st.selectbox("Enter your cource :",["BCA","Btech","MCA"])
if st.button("click me"):
  st.success("clicked button")
file = st.file_uploader("Upload your file")


