from googleapiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import datetime
from screeninfo import get_monitors

# Nova API Key gerada
api_key = 'AIzaSyDSAhr_GOV1ok0d1zf4J-ddTKyXqT-rEgk'

# Sequência - CNN - TCNews
channel_ids = ['UCvdwhh_fDyWccR42-rReZLw', 'UCWwZ0vM0qnr3vPHh2lgqH_w']

def get_last_youtube_lives(api_key, channel_ids):
    youtube = build('youtube', 'v3', developerKey=api_key)
    live_videos = []

    for channel_id in channel_ids:
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            eventType="live",
            type="video",
            order="date"
        )
        response = request.execute()

        if response['items']:
            live_video_id = response['items'][-1]['id']['videoId']
            live_video_link = f'https://www.youtube.com/embed/{live_video_id}?&autoplay=1&mute=1'
            live_videos.append(live_video_link)
        else:
            live_videos.append("Nenhuma live ativa")
    
    return live_videos

while True:
    # Obter os links das lives
    live_videos = get_last_youtube_lives(api_key, channel_ids)

    # Gerando o HTML com vídeos dimensionados para 512px por 256px
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Telao Laatus</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            html, body {{
                height: 100%;
                width: 100%;
                overflow: hidden;  /* Desabilitar barras de rolagem */
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .video-grid {{
                display: grid;
                grid-template-columns: repeat(2, 512px); /* 2 colunas com largura de 512px */
                grid-template-rows: repeat(4, 256px);    /* 4 linhas com altura de 256px */
                gap: 1px; /* Espaço entre os vídeos */
            }}

            .video-grid iframe,
            .video-grid video {{
                width: 512px;   /* Largura fixa de 512px */
                height: 256px;  /* Altura fixa de 256px */
            }}
        </style>
    </head>
    <body>
        <div class="video-grid">
            <!-- Bloomberg -->
            <iframe src="https://www.youtube.com/embed/iyOq8DhaMYw?&autoplay=1&mute=1" 
                    title="YouTube live video 1" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen></iframe>

            <!-- CNN -->
            <iframe src="{live_videos[0]}" 
                    title="YouTube live video 2" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen></iframe>

            <!-- TC News -->
            <iframe src="{live_videos[1]}" 
                    title="YouTube live video 3" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen></iframe>

            <!-- trailer_laatus.mp4 -->
            <video controls autoplay muted loop style="object-fit: cover;">
                <source src="intro-INDICADORES.mp4" type="video/mp4">
            </video>
            
            <!-- Bloomberg (repetido) -->
            <iframe src="https://www.youtube.com/embed/iyOq8DhaMYw?&autoplay=1&mute=1" 
                    title="YouTube live video 1" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen></iframe>

            <!-- CNN (repetido) -->
            <iframe src="{live_videos[0]}" 
                    title="YouTube live video 2" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen></iframe>

            <!-- TC News (repetido) -->
            <iframe src="{live_videos[1]}" 
                    title="YouTube live video 3" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen></iframe>

            <!-- trailer_laatus.mp4 (repetido) -->
            <video controls autoplay muted loop style="object-fit: cover;">
                <source src="intro-INDICADORES.mp4" type="video/mp4">
            </video>
        </div>
    </body>
    </html>
    """

    # Escreve o conteúdo HTML em um arquivo
    html_file_path = os.path.abspath('telao_04.html')
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("Arquivo HTML gerado com sucesso!")

    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")  # Remover a infobar
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remover a mensagem de automação

    # Abrindo o arquivo HTML local
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Definir as coordenadas da segunda tela (assumindo que a segunda tela está à direita da primeira)
    # Ajuste o valor de monitor_x conforme necessário, geralmente a segunda tela começa após a largura do monitor principal.
    monitor_x = 1920  # Exemplo para um monitor principal de 1920px de largura. Ajuste conforme necessário.
    monitor_y = 0     # Manter a janela no topo do segundo monitor

    # Mover o navegador para a segunda tela
    driver.set_window_position(monitor_x, monitor_y)
    driver.maximize_window()
    driver.get("file:///C:/Clayton/telao04/telao_04.html")
    #driver.get(f"file:///home/laatus/Clayton/testes/4_telao/telao_04.html")

    pyautogui.press('f11')  # Fullscreen via pyautogui

    print(f'Executado em {datetime.datetime.now()}! Próxima execução em 60 minutos.')
    time.sleep(60 * 60)





