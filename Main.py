import streamlit as st
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