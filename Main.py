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
#remove the hamburger & footer of streamlit
st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4
{
    visibility: hidden;            
}
.st-emotion-cache-1wbqy5l.e17vllj40
{
    visibility: hidden;            
}
            
</style>
""", unsafe_allow_html=True)
def change():
    print(st.session_state.checker)
state=st.checkbox("checkbox",value=True,on_change=change,key="checker")#value=False by default but if it is True, there will be  a tick mark 
#session_state : true or false of the checkbox if it's checked or not
#radio_btn=st.radio('In which country do you live?',options=("US","Uk","canada","TN"))
#print(radio_btn)
def btn_click():
    print('button clicked')
btn=st.button("Click Me!",on_click=btn_click)
st.link_button(":coffee:","https://www.linkedin.com/in/mohamed-bechir-yassine-ouardani/")
select=st.selectbox("what is your favourite car ?",options=("audi","bmw","polo"))
multi_select=st.multiselect("what is your favourite brand",options=('gucci',"bmx",'afro'))
st.write(multi_select)
