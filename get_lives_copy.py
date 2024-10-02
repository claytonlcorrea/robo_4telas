from googleapiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import datetime

#api_key = 'AIzaSyD2Rc0eouTq4xX6e5A_Rqu38s8BxzZWBBg' # you have exceeded your quota at 30/09/24

# api_key = 'AIzaSyD4Y-OVxAtBUrZxulGbuIvVVbjr0fMCiUw'
# channel_ids = ['UCvdwhh_fDyWccR42-rReZLw', 'UCWwZ0vM0qnr3vPHh2lgqH_w'] # Sequência - CNN - TCNews

# def get_last_youtube_lives(api_key, channel_ids):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     live_videos = []

#     for channel_id in channel_ids:
#         request = youtube.search().list(
#             part="snippet",
#             channelId=channel_id,
#             eventType="live",
#             type="video",
#             order="date"
#         )
#         response = request.execute()

#         if response['items']:
#             live_video_id = response['items'][-1]['id']['videoId']
#             live_video_link = f'https://www.youtube.com/embed/{live_video_id}?&autoplay=1&mute=1'
#             live_videos.append(live_video_link)
#         else:
#             live_video_id = response['items'][-1]['id']['videoId']
#             live_video_link = f'https://www.youtube.com/embed/{live_video_id}?&autoplay=1&mute=1'
#             live_videos.append(live_video_link)

#     return live_videos

# live_videos = get_last_youtube_lives(api_key, channel_ids)

# # Gerando o HTML 
# html_content = f"""
# <!DOCTYPE html>
# <html lang="pt-BR">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Telao Laatus</title>
#     <style>
#         * {{
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }}

#         html, body {{
#             height: 100%;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#         }}

#         .video-grid {{
#             display: grid;
#             grid-template-columns: repeat(2, 1fr); /* 2 colunas de tamanho igual */
#             grid-template-rows: repeat(2, 1fr);    /* 2 linhas de tamanho igual */
#             width: 100vw;
#             height: 100vh;
#         }}

#         .video-grid iframe {{
#             width: 100%;
#             height: 100%;
#         }}
#     </style>
# </head>
# <body>
#     <div class="video-grid">
#         <!-- Bloomberg -->
#         <iframe src="https://www.youtube.com/embed/iyOq8DhaMYw?&autoplay=1&mute=1" 
#                 title="YouTube live video 1" 
#                 frameborder="0" 
#                 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
#                 allowfullscreen></iframe>

#         <!-- CNN -->
#         <iframe src="{live_videos[0]}" 
#                 title="YouTube live video 2" 
#                 frameborder="0" 
#                 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
#                 allowfullscreen></iframe>

#         <!-- TC News -->
#         <iframe src="{live_videos[1]}" 
#                 title="YouTube live video 3" 
#                 frameborder="0" 
#                 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
#                 allowfullscreen></iframe>

#         <!-- trailer_laatus.mp4 -->
#         <video width="100%" height="100%" controls autoplay muted loop style="object-fit: cover;">
#             <source src="intro-INDICADORES.mp4" type="video/mp4">
#         </video>
#     </div>
# </body>
# </html>
# """

# # Escreve o conteúdo HTML em um arquivo
# html_file_path = os.path.abspath('telao_04.html')
# with open(html_file_path, 'w', encoding='utf-8') as file:
#     file.write(html_content)

# print("Arquivo HTML gerado com sucesso!")

while True:
    chrome_options = Options()
    #chrome_options.add_argument("--start-fullscreen")  # Para iniciar em fullscreen - estou usando F11 L-129
    chrome_options.add_argument("--disable-infobars")  # Para remover a infobar =]
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove mensagem de automação

    # Abrindo telao_04.html usando Selenium
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(f"file:///home/laatus/Clayton/testes/4_telao/telao_04.html")

    pyautogui.press('f11')

    print(f'executado em {datetime.datetime.now()}! aguardando uma hora para a próxima execução.')
    time.sleep(30)
    



