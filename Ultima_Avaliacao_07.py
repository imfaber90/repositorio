import streamlit as st
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as pyplot
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
import pypdf
import streamlit as st
from googleapiclient.discovery import build
import requests


def text_img_main(curso):
    if curso == 'Medicina':
        return textinho_med, imagem_med
    elif curso == 'Medicina Veterinária':
        return textinho_med_vet, imagem_med_vet
    elif curso == 'Engenharia':
        return textinho_eng, imagem_eng
    elif curso == 'Advocacia':
        return textinho_adv, imagem_adv

if 'text_img_info' not in st.session_state:
    st.session_state.text_img_info = {'texto': '', 'img': ''}
if 'curso' not in st.session_state:
    st.session_state.curso = "Medicina"  # Valor padrão

textinho_med = """
<h2><strong>Notas de corte de Medicina no Sisu</strong></h2>
<p>+ <em><a href="https://www.guiadacarreira.com.br/blog/como-se-inscrever-no-sisu">Como se inscrever no Sisu? Garanta sua vaga na universidade pública</a></em></p>
<p><span>A nota de corte média para o curso de Medicina, considerando o Brasil todo, foi de cerca de </span><b><strong>811,428</strong></b> <b>pontos na última edição do Sisu de 2023.</b></p>
<p>Em 2023,<span> menor nota foi registrada na </span>Universidade Federal do Maranhão (UFMA) &#8211; São Luís (MA), sendo <strong>682,76</strong><span>. A maior</span> na Universidade Federal do Amapá (UNIFAP), <strong>918,34</strong>.</p>
<p><span>Veja quais foram as notas de corte em algumas outras universidades brasileiras que participam do Sisu, na modalidade Ampla Concorrência (A0):</span></p>
"""

textinho_med_vet = """
<h2><strong>Notas de corte de Medicina Veterinária no Sisu</strong></h2>
<p><span>As notas de corte para o curso variam de acordo com a faculdade e a localização da instituição. Nas últimas edições do exame, as notas variaram entre 636 e 817 pontos, sendo a menor pontuação foi da Universidade Federal de Tocantins e a mais alta da Universidade Federal do Pará.</span></p>
<p><span>Algumas faculdades e universidades bem conceituadas, como a Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM), Universidade Federal da Paraíba (UFPB) e a Universidade Federal do Rio Grande do Sul (UFRGS) tiveram notas de corte abaixo de 700 pontos.</span></p>
<p><span>Já instituições como a Universidade Federal do Paraná (UFPR), Universidade Federal de Minas Gerais (UFMG) e a Universidade Federal do Rio de Janeiro (UFRJ) pediram um pouco mais de empenho dos candidatos. As notas de corte nessas instituições foram superiores a 700 pontos, e a UFPR chegou próximo a 800.</span></p>
"""

textinho_eng = """
<h2><strong>Engenharia</strong></h2>
<p><strong>Engenharia </strong>é a capacidade de aplicar os conhecimentos científicos de forma prática a fim de produzir novas utilidades. Para obter tais resultados, o engenheiro estuda o problema, planeja uma solução, verifica a viabilidade econômica e técnica e por fim coordena o desenvolvimento ou produção.</p>
<p>A Engenharia tem uma forte relação com as <strong><a href="http://www.guiadacarreira.com.br/artigos/guia-das-profissoes/ciencias-exatas/">Ciências Exatas.</a></strong>No entanto, ao contrário do que muita gente pensa, nem toda Engenharia está relacionada apenas com matemática e objetos concretos. Hoje em dia temos a Engenharia Genética, por exemplo, que está relacionada à Biologia.</p>
"""

textinho_adv = """
<h2><strong>Advocacia</strong></h2>
<p>O primeiro passo para atuar na advocacia e ser um advogado, é necessário fazer uma graduação em Direito. Após a formação, que dura em torno de 5 anos, o profissional precisa realizar o <a href="https://www.guiadacarreira.com.br/blog/prova-da-oab" target="_blank" rel="noreferrer noopener"><b>Exame da OAB</b> (Ordem dos Advogados do Brasil)</a>. Somente após ser aprovado nesta prova é que recebe o registro e pode exercer a a carreira.</p>
<p>A principal atividade de um advogado é representar e <b>defender os interesses</b> de seus clientes com base nas <b>leis vigentes</b> do país. Ele pode representar pessoas físicas e jurídicas.</p>
<p>Um <b>advogado</b> pode se <b>especializar</b> em diferentes vertentes do Direito, tais como:</p>
<ul>
<li>Civil</li>
<li>Trabalhista e Previdenciário</li>
<li>Penal</li>
<li>Ambiental</li>
<li>Eleitoral</li>
<li>Tributário</li>
<li>Empresarial</li>
</ul>
<p>Além disso, outro ponto que vale destacar é que este profissional pode atuar como:</p>
<ul>
<li><b>Advogado de acusação</b>: representando os interesses de alguém que se sente lesado ou prejudicado e deseja acusar outra pessoa.</li>
<li><b>Advogado de defesa</b>: neste caso seu cliente está sendo acusado de algum crime ou infração e precisa se defender perante a Lei.</li>
</ul>
"""

if 'dicionario' not in st.session_state:
    
    url = "https://vestibulares.estrategia.com/portal/enem-e-vestibulares/enem/assuntos-que-mais-caem-no-enem/"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    uls = soup.find_all('ul')
    h3s = soup.find_all('h3')

    categoria = []

    dicionario = {}

    uls = uls[13:26]
    h3s = h3s[1:]

    for i, h3 in enumerate(h3s):
        if i in [1]:
            continue
        categoria.append(h3.text.strip())

    for i, ul in enumerate(uls):
        dicionario[categoria[i]] = []
        for li in ul:
            materia, porcentagem = li.text.strip().split('–')
            materia = materia.strip()
            porcentagem = float(porcentagem.replace("%","").replace(",",".").strip())
            dicionario[categoria[i]].append({materia:porcentagem})  
    
    st.session_state.dicionario = dicionario 
    

imagem_med = "imagens/Medicina-Enem-2.jpg"
imagem_med_vet = "imagens/medicina-veterinaria.jpeg"
imagem_eng = "imagens/qual-engenharia-ganha-mais-2.jpg"
imagem_adv = "imagens/vista-de-escalas-3d-de-justica-para-o-dia-do-advogado-1-scaled.jpg"


def gerar_pdf(dicionario):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)

    y = 750
    for categoria, materias in dicionario.items():
        c.drawString(30, y, f"{categoria}")
        y -= 30  # Espaço adicional após o título da categoria
        for materia_dict in materias:
            for materia, porcentagem in materia_dict.items():
                c.drawString(50, y, f"{materia} - {porcentagem}%")
                y -= 20
                if y < 50:
                    c.showPage()
                    y = 750
                    c.setFont("Helvetica", 12)

        y -= 20 
    
    c.save()
    buffer.seek(0)
    return buffer


def download_pdf(buffer):
    st.download_button(
        label="Download PDF",
        data=buffer,
        file_name="dados.pdf",
        mime="application/pdf"
    )


def grafico(dicionario, topic):
    materia = []
    porcent = []
    for descricao, lista in dicionario.items():
        if topic in descricao:
            for l in lista:
                for k in l:
                    materia.append(k)
                    porcent.append(l[k])
    
    num_colors = len(materia)
    cmap = pyplot.get_cmap("tab20", num_colors)
    colors = [cmap(i) for i in range(num_colors)]
    
    explode = [0.1 if i == 1 else 0 for i in range(len(materia))]

    pyplot.figure(figsize=(11, 8))
    pyplot.pie(porcent, labels=materia, colors=colors, startangle=90,
               shadow=True, explode=explode, autopct='%1.1f%%')
    pyplot.title(f'Principais tópicos de {topic}')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(pyplot.gcf())
    
api_key = "AIzaSyDZFNSxQLJMPVrD47AlE780I1_Y6r0DOpA"
    
def buscar_videos(api_key, pesquisa):
    if 'videos' not in st.session_state:
        st.session_state.videos = {}

    if pesquisa in st.session_state.videos:
        return st.session_state.videos[pesquisa]

    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=pesquisa,
        type="video"
    )
    response = request.execute()
    
    videos = []
    
    for item in response['items']:
        video_info = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'videoId': item['id']['videoId'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            'thumbnail': item['snippet']['thumbnails']['default']['url']
        }
        videos.append(video_info)
    
    st.session_state.videos[pesquisa] = videos
    return videos


def pesquisa_video(dicio):
    for descricao, lista in dicio.items():
        st.markdown(f'<strong>{descricao}<strong>', unsafe_allow_html=True)
        for i, l in enumerate(lista):
            if i == 3:
                break
            for k in l:
                st.write(k, l[k], "% de peso")
                pesquisa = k
                videos = buscar_videos(api_key, pesquisa)
                for idx, video in enumerate(videos):
                    st.subheader(f"Vídeo {idx+1}: {video['title']}")
                    st.image(video['thumbnail'])
                    st.write(f"Description: {video['description']}")
                    st.write(f"[Link para o vídeo]({video['url']})")
                    st.write("---")
    
    
st.title("Matérias recorrentes no Enem")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Cursos", "Linguagens", "Humanas", "Naturezas", "Matemática","Features"])

with tab1:
    col1, col2 = st.columns(2)
    cursos = ["Medicina", "Medicina Veterinária", "Engenharia", "Advocacia"]
    
    with col1:
        st.session_state.curso = st.selectbox("Selecione um curso:", cursos, index=cursos.index(st.session_state.curso))
        texto, img = text_img_main(st.session_state.curso)
        st.session_state.text_img_info['texto'] = texto
        st.session_state.text_img_info['img'] = img
                
    with col2:
        ingresso = st.selectbox("Forma de ingresso:", options=["ENEM/Sisu"])
            
    st.markdown('---')
                
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(st.session_state.text_img_info['texto'], unsafe_allow_html=True)
            
    with col4:
        st.image(st.session_state.text_img_info['img'], width=330)

with tab2:
    grafico(st.session_state.dicionario, "Português")

with tab3:
    grafico(st.session_state.dicionario, "Geografia")
    grafico(st.session_state.dicionario, "História")
    grafico(st.session_state.dicionario, "Filosofia")
    grafico(st.session_state.dicionario, "Sociologia")
    
with tab4:
    grafico(st.session_state.dicionario, "Biologia")
    grafico(st.session_state.dicionario, "Física")
    grafico(st.session_state.dicionario, "Química")
    
with tab5:
    grafico(st.session_state.dicionario, "Matemática")

with tab6:    
    gerar = st.button("Gerar PDF dos principais tópicos")
    if gerar:
        pdf_buffer = gerar_pdf(st.session_state.dicionario)
        download_pdf(pdf_buffer)
    try:  
        pass  
        pesquisa_video(st.session_state.dicionario)
    except:
        st.write("Excedeu o uso da API Key pro Youtube (trocar Key)")


