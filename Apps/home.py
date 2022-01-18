import streamlit as st 

def app():
    #Colocando as categorias de projetos
    st.subheader("Projetos")

    #Descrição
    st.markdown("Esse é o meu portfólio de projetos relacionados a Data Science, Data Analytics, Machine Learning e Inteligência Artificial")
    st.markdown("Caso esteja interessado de saber um pouco mais do meu trabalho, você pode visitar www.enderecodesite.com.br")
    st.markdown("Contato: Pedrocdellazzari@gmail.com | Site: pedrodellazzari.com.br")

    #Criando as colunas
    col1, col2 = st.columns(2)

    #Criando o expander de Data Science 
    data_science = col1.expander("Data Science")
    data_science.write("""- Em breve \n\n - Em breve""")

    #Criando o expander de Machine Learning
    machine_learning = col1.expander("Machine Learning")
    machine_learning.write("""- Reconhecimento de mãos (vídeo) \n\n - Reconhecimento de faces (imagem)""")

    #Criando expander de Data Anlytics 
    data_analyses = col2.expander("Data Analytics")
    data_analyses.write("- Em breve \n\n - Em breve")

    #Criando o expander de inteligencia artificial
    inteligencia = col2.expander("Inteligência Artificial")
    inteligencia.write("- Em breve \n\n - Em breve")

    #Criando o expander de inteligencia artificial
    miscellaneous = col1.expander("miscellaneous")
    miscellaneous.write("- Simulação investimento \n\n - Projeto 2")