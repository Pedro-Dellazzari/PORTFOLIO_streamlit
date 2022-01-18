import streamlit as st 
from multiapp import MultiApp
from Apps import home
from Apps.Streamlit_reconhecimento_rostos import reconhecimento
from Apps.Investimentos_simulacao import simulation
from Apps.finger_count import finger_count



app = MultiApp()

#st.set_page_config(layout = 'wide')

st.title("Pedro Dellazzari - Portfólio")

app.add_app("Home", home.app)
app.add_app("Reconhecimento de faces em imagens", reconhecimento.app)
app.add_app("Reconhecimento de dedos em vídeo", finger_count.app)
app.add_app("Simulação de investimentos", simulation.app)


app.run()