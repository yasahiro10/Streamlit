import streamlit as st
import pandas as pd
table=pd.DataFrame({"column1":[1,2,3,4,5,6,7],"column2":[11,12,13,14,15,16,17]})
st.title("Hi i am streamlit web app")
st.subheader("Hi I am your subheader")
st.header("I am header")
st.text("Hi i am text function and programmers uses")
st.markdown("**HELLO** *world*")
st.markdown(" ---")
st.caption("hi i am caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
print("hello world")
def funct():
    return 0;
"""
st.code(code,language="python")
st.write("## H2")
st.metric(label="Wind speed", value='120ms⁻¹',delta="-1.4ms⁻¹ ")
st.table(table)
st.dataframe(table)#for dataframe we can stor the numbers
st.image("image.jpg",caption="this is an image", width=400)
#st.audio()
#st.video()