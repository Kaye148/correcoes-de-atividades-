import streamlit as st

st.title ("atividade_nota_media_5")

nota1 = st.number_input ("informe a nota: ", min_value=0, max_value=10)
nota2 = st.number_input ("informe a nota: ", min_value=0, max_value=10)
nota3 = st.number_input ("informe a nota: ", min_value=0, max_value=10)


while True


media = (nota1 + nota2 + nota3) / 3

if st.button("calclular a média"):
    st.info(f"média:{media}")


 








