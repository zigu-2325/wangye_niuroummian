import streamlit as st
st.title("绝世美味")
st.header("You need to eat delicious foods")
st.subheader("eg, Lanzhou beef Noodles")
st.text("世界上最（✓）好吃的 ")

st.markdown("this is an image: \n \
            ![](https://ts1.cn.mm.bing.net/th/id/R-C.93d20ea20c49a1014985984a38e1b95f?rik=ndHmayshq%2bVd4A&riu=http%3a%2f%2fwww.jwdlm.com%2fHdAtt%2fimg%2f2020%2f07%2f20200731111923250.jpg&ehk=Vdcf0LKCWRVmuOYqyh5%2f0v%2bT1KAlvdSS9qSPEM%2bdAPI%3d&risl=&pid=ImgRaw&r=0)")

if st.checkbox("Show/Hide"):
    st.text("真好次")


status = st.radio("选择你目前的状态:" ,
                  ('好吃，天天吃！',
                   '现在吃不到以后吃'))
if status == '好吃，天天吃！':
    st.success("慕了慕了")
else:
    st.success("哈哈哈哈，绝对好吃")

hobbies = st.multiselect("你有多久没吃过牛肉面了:",
               ['一天',
                '一月',
                '半年',
                '一年'])
st.write("You selected: ", hobbies)

if st.button("解决方案"):
    st.text("没辙，回家库库吃（嘿嘿）")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    