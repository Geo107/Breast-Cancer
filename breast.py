import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('cancer.pkl', 'rb'))


def run():
    st.title("Cancer Prediction using Machine Learning")

    account_num = st.text_input('Sample Code Number')

    fn = st.text_input('Full Name')

    clump= st.slider('Clump Thickness',0,10,1)
    cell_size= st.slider('Uniformity of Cell Shape',0,10,1)
    mar = st.slider('Marginal Adhesion',0,10,1)
    epi = st.slider('Single Epithelial Cell Size',0,10,1)
    bare= st.slider('Bare Nuclei',0,10,1)
    bland= st.slider('Bland Chromatin',0,10,1)
    nucleo= st.slider('Normal Nuceoli',0,10,1)
    mito = st.slider('Mitoses',0,10,1)
    class1 = st.slider('Class',0,10,1)



    if st.button("Submit"):
        features = [[clump,cell_size, mar, epi, bare, bland,nucleo,mito,class1]]
        print(features)
        for i in features[0]: print(type(i))
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 2:
            st.success(
                "Hello: " + fn + " || "
                                 "Sample Code Number: " + account_num + ' || '
                                                                   'Congrats its Benign Cancer!'
            )
        elif ans == 4:
            st.error(
                "Hello: " + fn + " || "
                                 "Sample Code Number: " + account_num + ' || '
                                                                   'Cancer Detected! Its Malignant!!!'
            )


run()
