import pickle
import streamlit as st

model = pickle.load(open('data_balita.sav', 'rb'))

st.title('Prediksi Status Gizi Balita')

umur_bulan = st.number_input('Input Umur (bulan)', min_value=0, max_value=120)
kelamin = st.selectbox('Jenis Kelamin', ['Laki-laki', 'Perempuan'])
tinggi = st.number_input('Input Tinggi Badan (cm)', min_value=0, max_value=300)

kelamin_encoded = 1 if kelamin == 'Laki-laki' else 0

input_data = [[umur_bulan, kelamin_encoded, tinggi]]

predict = ''

if st.button('Prediksi'):
    predict = model.predict(input_data)[0]
    st.write('Prediksi Status Gizi Balita :', predict)