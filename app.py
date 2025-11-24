import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

st.title("streamlit app of vgu")
st.text("welcome to our dashboard")
st.header("i am a header")
st.write("u can write",10+5)

name = st.text_input("Enter your name")
age = st.number_input("Enter your age:")
st.write("your anem Is :",name,"your age is :",age)
st.selectbox("Enter your cource :",["BCA","Btech","MCA"])
if st.button("click me"):
  st.success("clicked button")
file = st.file_uploader("Upload your file")
if file:
  content = file.read()
  st.write("File upload successfully !!!")

data = {"Name":["TOM", "jack","pop","harry"], "Marks":[10,20,30,40]}
df = pd.DataFrame(data)

st.dataframe(df)

data = pd.DataFrame({
  "Marks":[10,20,10,30]
})

st.line_chart(data)
st.bar_chart(data)

subject = ["python",["c++"],["java"]]
marks = [20,10,5]

fig , ax = plt.subplots()
ax.pie(marks, labels = marks)
st.pyplot(fig)



bar = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    bar.progress(i+1)

st.metric(label="Profit", value="₹10,000", delta="+12%")

agree = st.checkbox("i agree terms and conditions")
if agree: 
   st.text("thank you for agreeing t and c")


date = st.date_input("Select a date")
st.write("Your selected date:", date)

time = st.time_input("Select time")
st.write("Selected time:", time)


age = st.slider("Select age", 1, 100, 25)
st.write("Age:", age)

values = st.slider("Select range", 0, 100, (20, 60))
st.write("Range:", values)

name = st.text_input("Enter your name")
st.write("Name:", name)

num = st.number_input("Enter a number", min_value=0, max_value=100)
st.write("Number:", num)

if st.button("Click me"):
    st.write("Button clicked!")


