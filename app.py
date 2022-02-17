import streamlit as st
from PIL import Image

#####################
# Custom function for printing text
def txt(a):
    _, col, _ = st.columns((1,3,1))
    with col:
        st.markdown(a)

def txt1(a, b):
  _, col1, col2, _ = st.columns([1,2,1,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  _, col1, col2, _ = st.columns([1,1,2,1])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  _, col1, col2, _ = st.columns([1,1,2,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  _, col1, col2, _, col3, _ = st.columns([1,0.65,1.5, 0.1,0.75,1])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

st.set_page_config(page_title='Le Nguyen Gia Bao - Portfolio',page_icon="☀", layout="wide")
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
# bg = Image.open('./image/background.jpg')
# st.image(bg, width=1920)

image = Image.open('./image/lenguyengiabao-circle.png')
_, img_column, _ = st.columns((2,1,2))
img_column.image(image, use_column_width  = True)

st.write('''
# Le Nguyen Gia Bao
##### A Developer from Vietnam 🇻🇳  
''')
txt('## Summary')
# col.markdown('## Summary')
_, col, _ = st.columns((1,3,1))
col.success('''
- I'm interested in AI, Machine Learning, Computer Vision, NLP, Data Processing, Data Visualization.
- I love nature. I love trees 🌲 , lakes, mountains, ... I love sunny, and if I have a window, I always want it to open!
- I like running, cycling, ... And during the time I run, I like listening to Podcast. My favorite author is [The Present Writter](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy8zMjZkNjc2Yy9wb2RjYXN0L3Jzcw) (Ms. Chi Nguyen)
''')

#####################
txt('''
## Contact Infomation
''')
txt2('Phone', '0798725333')
txt2('Zalo', '0798725333')
txt2('Address', 'Thu Duc City, Ho Chi Minh City, Vietnam')
txt2('Email', '[lenguyengiabao46@gmail.com](mailto:lenguyengiabao46@gmail.com)')
txt2('LinkedIn', 'https://www.linkedin.com/in/lenguyengiabao/')
txt2('GitHub', 'https://github.com/LeNguyenGiaBao/')
txt2('Leetcode', 'https://leetcode.com/LeNguyenGiaBao/')
txt2('Facebook', 'https://www.facebook.com/baorua.98/')

#####################
txt('## Education')
# col.markdown('## Education')
txt1('**Final Year Student**,  *[Ho Chi Minh University of Technology and Education](https://hcmute.edu.vn/)*, Vietnam',
'09/2018 - Present')
txt('''
- Software Technology
- GPA: `3.38`
- Student with 5 Merits - University Level - 01/2022
''')

txt1('**AI Developer Course**,  *ISC Quang Trung*, Vietnam',
'11/2021 - 01/2022')
txt('''
- Final Project: [Fashion Recognition](https://share.streamlit.io/lenguyengiabao/fashion_recognition/app.py)
''')

#####################
txt('''
## Work Experience
''')
txt1('**Member of Developer Team**, *[Google Developer Student Club HCMUTE](https://www.facebook.com/gdsc.hcmute)*',
'08/2021 - Present')
txt1('**Internship**, *Anonymous company*, Vietnam',
'10/2021 - 01/2022')

#####################
txt('''
## Project
''')
txt4('Vehicle Detection', 'The website is used to identify vehicles, assess and visualize traffic conditions in Ho Chi Minh City, Vietnam. Using `SSD Object Detection` and real camera data from Ho Chi Minh', 'https://share.streamlit.io/lenguyengiabao/vehicle_detection/app.py')
txt4('Face Recognition Research', 'Research about SOTA model of Face Recognition. Current research: `InsightFace`','https://github.com/LeNguyenGiaBao/face_detection')
txt4('Fashion Recognition', 'A website where you can find all fashion styles in world with only a picture', 'https://share.streamlit.io/lenguyengiabao/fashion_recognition/app.py')
txt4('Leetcode Java', 'A repo to learn, solve and store answers to questions on Leetcode. Submission: `68` easy and `11` medium', 'https://github.com/LeNguyenGiaBao/leetcode_java')
txt4('Face Recognition', 'Timekeeping system with face recognition build in Python. Technology: `MTCNN`, `Inception Resnet`, `SVM`', 'https://github.com/LeNguyenGiaBao/Face_Recognition')
txt4('ParkingLot_CNN', 'Using CNN to read license plates and replicate a parking application. Technology: `MobileNetV2`, `Wpod Net`, `MySQL Database`','https://github.com/LeNguyenGiaBao/ParkingLot_CNN')


#####################
txt('''
## Skills
''')
txt3('Programming', '`Python`, `Java`, `C#`, `SQL`, `JS`')
txt3('Python Library', '`numpy`, `opencv`, `pandas`, `matplotlib`, `glob`, `requests`, ...')
txt3('Machine Learning', 'Supervised Learning, Unsupervised Learning, `scikit learn`')
txt3('Deep Learning', 'CNN, Object Detection, Transformer, BERT, `TensorFlow`, `Keras`, `PyTorch`')
txt3('Web development', '`Flask`, `HTML`, `CSS`, `Streamlit`')

