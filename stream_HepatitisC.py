import pickle
from turtle import color
import streamlit as st

# Membaca Model
HepatitisC_model = pickle.load(open('hepatitisC_model.sav', 'rb'))

# Judul Web
st.title('Data Mining Prediksi Hepatitis C')

col1, col2, col3 = st.columns(3)
with col1:
    Age = st.number_input('Input nilai Age')
with col2:
    Gender = st.number_input('Input nilai Gender')
with col3:
    st.caption('''
        Gender : \n
        male   = 0 \n
        female = 1 \n
        ''')
with col1:
    ALB = st.number_input('Input nilai ALB')
with col2:
    ALP = st.number_input('Input nilai ALP')
with col1:
    ALT = st.number_input('Input nilai ALT')
with col2:
    AST = st.number_input('Input nilai AST')
with col1:
    BIL = st.number_input('Input nilai BIL')
with col2:
    CHE = st.number_input('Input nilai CHE')
with col1:
    CHOL = st.number_input('Input nilai CHOL')
with col2:
    CREA = st.number_input('Input nilai CREA')
with col1:
    GGT = st.number_input('Input nilai GGT')
with col2:
    PROT = st.number_input('Input nilai PROT')

# Code untuk pediksi
hepa_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Hepatitis C'):
    hepa_prediction = HepatitisC_model.predict(
        [[Age, Gender, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT]])

    if (hepa_prediction[0] == 1):
        hepa_diagnosis = 'Pasien terdiagnosa Hepatitis C'
    else:
        hepa_diagnosis = 'Pasien tidak terdiagnosa Hepatitis C'

    st.success(hepa_diagnosis)
