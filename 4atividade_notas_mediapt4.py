import streamlit as st

st.title("atividade_4_pt4")

login_salvo = "zezinho69"
senha_salva  = "123456"
tentativas = 0

st.session_state.setdefault()
st.session_state.setdefault()

for i in range (3):
    print(f"tentativa:{tentativas + 1}")

    login st.text_input("informe seu login: ",disabled=st.session_state.desabilitar)
    senha st.text_input("informe sua senha:", type="password")

    if st.button ("verificar"):
        login == login_salvo and senha == senha_salva: # type: ignore
        st.write("bem vindo!")
    else:
        st.Warning ("login ou senha invalidas")
        tentativas += 1
    if tentativas >= 3:
        st.warning("numero de tentativas excedido!")
        break

        