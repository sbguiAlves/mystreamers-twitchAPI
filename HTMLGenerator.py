from items import Items


def gerador_html(items):
    lista = items.data_obj.data
    conteudo = ''

    inicio_html = '''
    <!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="utf-8">
    <title>Minha Twitch</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <header>
        <div class="caixa-principal">
            <h1>Programação atual - Streamers seguidos</h1>
        </div>
    </header>

    <main>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Título</th>
                    <th scope="col">Tempo</th>
                </tr>
            </thead>
    '''

    # Lógica -------------

    if lista:  # Se a lista não estiver vazia
        for item in lista:
            conteudo += '''
                <tbody>
                    <tr>       
                        <td>
                        <div class="live-info">    
                            <div class="live-streamer">
                                <h2>{0}</h2> <img src="Images/twitch-logo.png" alt="Logo Twitch"> <a href="https://twitch.tv/{3}">twitch.tv/{3}</a>
                            </div>
                            <h3 class="live-title">{1}</h3>
                            <div class="live-game">
                                <img src="Images/game-control.png" alt="Logo Twitch"><p class="game">{2}</p>
                            </div>
                        </div>
                        </td>
                         <td>
                            <div class="date">
                                <span>{4}</span>
                            </div>
                        </td>
                    </tr>    
                </tbody>
                '''.format(item.user_name, item.title, item.game_name, item.user_login,
                           items.tempo_transmissao(item.started_at))

    # -------------------
    # items.verificar_status(item.type)

    fim_html = '''
        </table>
    </main>

    <script type="text/javascript"></script>
    <footer>
        <p class="copyright">&copy; Guilherme A. Silva - 2022</p>   
    </footer>
</body>
</html>
    '''

    html_str = inicio_html + conteudo + fim_html

    # abre o arquivo HTML para escrita
    arq_html = open('index.html', 'w', encoding="utf-8")

    # escrevendo no arquivo HTML
    arq_html.write(html_str)

    # fechando os arquivos
    arq_html.close()


items = Items
gerador_html(items)
