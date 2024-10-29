# Robo utilizado para varrer alguns canais do youtube e pegar a live ativa, tratar o click como embed e gerar um HTML de 8 quadros com os videos embedado. Foi utilizado 8 vídeos pois foi para um telão de 1024px x 1024px mas fácilmente pode ser customizado para atender diferentes necessidades.

O **Telao Laatus** é uma aplicação Python desenvolvida para capturar transmissões ao vivo de canais do YouTube e exibi-las em um layout organizado em HTML. Essa ferramenta permite que você acompanhe múltiplas lives em uma única tela, com suporte a vídeos embutidos e conteúdo em vídeo personalizado.

## Funcionalidades

- **Busca de Transmissões ao Vivo**: Conecta-se à API do YouTube para obter a live mais recente de canais específicos.
- **Renderização Dinâmica de HTML**: Gera um arquivo HTML com um layout de exibição personalizado, onde cada vídeo é ajustado automaticamente.
- **Exibição Automática em Tela Cheia**: Utiliza o Selenium para abrir o HTML gerado e maximizar a visualização em tela cheia na segunda tela configurada.
- **Atualizações Periódicas**: Atualiza a exibição automaticamente a cada 60 minutos, permitindo que novas lives sejam exibidas conforme disponíveis.

## Tecnologias Utilizadas

- **Python**: Principal linguagem de desenvolvimento para controle de lógica e API.
- **Google API Client**: Para integrar com a API do YouTube e buscar as transmissões ao vivo.
- **Selenium e PyAutoGUI**: Para automação do navegador e controle de tela cheia.
- **HTML e CSS**: Estrutura e estilo da página de exibição.
- **WebDriver Manager**: Facilita o gerenciamento do driver do Chrome para o Selenium.

## Configuração e Execução

### Pré-requisitos

- **Python 3.x**
- **Google API Key**: Configure sua chave de API no código para acessar a API do YouTube.
- **Chrome** e **ChromeDriver**: O navegador e o driver para execução do Selenium.

### Instalação

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install google-api-python-client selenium webdriver-manager pyautogui screeninfo
