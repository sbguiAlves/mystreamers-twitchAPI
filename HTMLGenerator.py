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
                    <th scope="col">Streamer</th>
                    <th scope="col">Atividade atual</th>
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
                                <h2>{0}</h2> <img src="Images/twitch-logo.png" alt="Logo Twitch"> <a href="https://twitch.tv/{1}">twitch.tv/{1}</a>
                            </div>
                            <h3 class="live-title">{2}</h3>
                            <div class="time">
                                <p>{3}</p>
                                <p>{4}</p>
                            </div>
                        </div>
                        </td>
                         <td>
                            <div class="live-game">
                                <p class="game">{5}</p>
                            </div>
                        </td>
                    </tr>    
                </tbody>
                '''.format(item.user_name, item.user_login, item.title, items.data_hora_inicio(item.started_at), items.data_hora_transmitido(item.started_at),
                           item.game_name)

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

