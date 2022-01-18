#Importando as bibliotecas
import streamlit as st
import cv2
import mediapipe as mp



#Criando o app
def app():
    # Criando classe
    mp_hands = mp.solutions.hands

    # Config find video
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

    # Inicializando a classe de desenho de landmark
    mp_drawing = mp.solutions.drawing_utils

    def detect_hands(image, output_image):

        # Pegando os resultados
        results = hands.process(image)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image=output_image, landmark_list=hand_landmarks,
                                          connections=mp_hands.HAND_CONNECTIONS,
                                          landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255),
                                                                                       thickness=3, circle_radius=2),
                                          connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0),
                                                                                         thickness=2, circle_radius=2))

    # Título
    st.title("Identificação de mãos")

    # Descrição do projeto
    st.write("Esse projeto foi criado utilizando o algoritmo do MediaPipe/Google para identificar mãos humanas.\n"
             "Nenhuma imagem ficará guardada após o uso desse projeto.")

    expander_1 = st.expander("Bibliotecas usadas")
    expander_1.write("Streamlit\n\nOpenCV\n\nMediaPipe")

    expander_2 = st.expander("Contato")
    expander_2.write("Criador - Pedro Dellazzari\n\n"
                     "LinkedIn: Pedro Dellazzari\n\n"
                     "Github: Link do Git")

    expander_3 = st.expander("Como usar?")
    expander_3.write("Certifique-se que você esteja conectado com uma Webcam\n\n"
                     "Certifique-se que o navegador que esteja utilizando tenha a permissão de usar a sua webcam\n\n"
                     "Basta apertar o botão 'Run' para começar. "
                     "Mostre as mãos para o algoritmo reconhecer")

    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    except:
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    # Para começar o aplicativo
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])

    while run:

        while cap.isOpened():
            _, frame_real = cap.read()
            frame = cv2.cvtColor(frame_real, cv2.COLOR_BGR2RGB)
            frame_2 = cv2.cvtColor(frame_real, cv2.COLOR_BGR2RGB)

            detect_hands(frame, frame_2)

            FRAME_WINDOW.image(frame_2)


    else:
        st.write('Clique no botão para inicializar a aplicação')