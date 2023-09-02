import random
import streamlit as st


presentacion = '''

***************JUEGO DE JAVIER 👨‍💻********************
*********Piedra Papel Tijeras***********
         🧻  🪨   ✂️

'''

st.write(presentacion)
#user_option = input('Por favor elija Piedra, papel o tijeras : ')

st.write("Mi primera app de python")
options = ['piedra','papel','tijeras']
user_option = st.selectbox("Seleccione uno de los siguientes", options)

random_options = (random.randint(0,2))
computer_option = options[random_options]
# st.write(computer_option)

st.write(f"Eleccion usuario 👨‍🦰: {user_option}")
st.write(f"Eleccion computador 🤖: {computer_option}")


if user_option.lower() == computer_option:
    st.write("!!Empate!! ")

elif user_option == "piedra":
    if computer_option=="tijeras":
        st.write("Usuario Gana Piedra rompe tijeras")
    else :
        st.write("Computador Gana papel tapa a piedra ☹️")

elif user_option == "papel":
    if computer_option == "tijeras":
        st.write("Computador gana tijeras corta a papel☹️")
    else :
        st.write("Usuario Gana papel tapa a piedra") 

elif user_option == "tijeras":
    if computer_option == "piedra":
        st.write("Computador gana piedra rompe tijeras ☹️")
    else :
        st.write("Usuario Gana tijeras corta papel")


