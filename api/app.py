from flask import Flask, render_template, request

app = Flask(__name__)

app.config["FREEZER_DESTINATION"] = "build"
app.config["FREEZER_RELATIVE_URLS"] = True

@app.route("/")
def home():
    return render_template("home.html")




@app.route("/servicos/")
def servicos():

    cards_beneficios_site = [{"beneficio": "Protótipo Navegável", "descricao": "Sujeito a sua aprovação antes da construção do site real", "imagem": "/static/img/icone_prototipo.png", "cor": ""}, 
    {"beneficio": "Controle de Versão", "descricao": "Via Git, em um repositório privado no Github. Você decide quem tem acesso", "imagem": "/static/img/icone_versao.png", "cor": "azul_2"}, 
    {"beneficio": "Design Responsivo", "descricao": "O design de seu site se adaptará a qualquer resolução", "imagem": "/static/img/icone_responsivo.png", "cor": "azul_3"},
    {"beneficio": "Organização", "descricao": "Código limpo, organizado e com comentários para fácil entendimento", "imagem": "/static/img/icone_organizacao.png", "cor": "azul_2"},
    {"beneficio": "UX/UI Aplicado", "descricao": "Aplicação de princípios de UX/UI, como Layout, Gestalt, 60/30/10 rule etc.", "imagem": "/static/img/icone_ux_ui.png", "cor": "azul_3"},
    {"beneficio": "Transparência 100%", "descricao": "Log diário do que foi feito, se tive facilidade ou não", "imagem": "/static/img/icone_transparencia.png", "cor": "azul_4"}
    ]

    cards_beneficios_branding = [{"beneficio": "Logo Criativo", "descricao": "Para que sua marca possa se destacar e passar sua mensagem", "imagem": "/static/img/icone_logo.png", "cor": "laranja_1"},
    {"beneficio": "Cores e Tipografia", "descricao": "Para que sua marca possa se comunicar melhor do que nunca", "imagem": "/static/img/icone_cores.png", "cor": "laranja_2"},
    {"beneficio": "Cartão de Visita", "descricao": "Arquivo de um cartão de visita personalizado frente e verso pronto para impressão", "imagem": "/static/img/icone_cartao.png", "cor": "laranja_3"},
    {"beneficio": "Mockups", "descricao": "De camisetas, canecas e bottons para você se inspirar", "imagem": "/static/img/icone_mockups.png", "cor": "laranja_3"},
    ]

    cards_avaliacoes = [{"foto": "/static/img/foto_geovana.png", "nome": "Geovana Vieira", "empresa": "Fundadora de Arerê Eventos", "texto": "O primeiro passo de um negócio que sempre sonhei foi criado: sua identidade. A Arerê tomará proporções gigantescas e seu branding a acompanhará em todo esse processo! Agradeço por todo o trabalho feito e o suporte recebido!", "data": "03/01/2024"},
    {"foto": "/static/img/foto_perfil.png", "nome": "Seu nome aqui", "empresa": "Nome do seu negócio", "texto": "Se você ficar satisfeito com sua comissão, você pode optar em escrever uma avaliação positiva curta aqui!", "data": "05/01/2022"},
    {"foto": "/static/img/foto_perfil.png", "nome": "Seu nome aqui", "empresa": "Nome do seu negócio", "texto": "Se você ficar satisfeito com sua comissão, você pode optar em escrever uma avaliação positiva curta aqui!", "data": "05/01/2022"}
    ]

    return render_template("servicos.html", cards_beneficios_site = cards_beneficios_site, 
    cards_beneficios_branding = cards_beneficios_branding, cards_avaliacoes = cards_avaliacoes)




@app.route("/sobre_mim/")
def sobre():
    return render_template("sobre_mim.html")




@app.route("/formacao/")
def formacao():

    formacao = [{"nome": "FATEC São José dos Campos - Prof. Jessen Vidal", "curso": "Tecnólogo em Desenvolvimento de Software Multiplataforma", "data": "ago 2023 - ago 2026", "texto_pequeno": "Grade do curso:",
    "lista_1": "Algoritmo e Lógica de Programação", "lista_2": "Desenvolvimento Web", "lista_3": "Engenharia de Software", "lista_4": "Modelagem de Banco de Dados", "lista_5": "Sistemas e Redes Operacionais", "lista_6": "Design Digital"},

    {"nome": "EBAC - Escola Britânica de Artes Criativas", "curso": "Profissão: UX/UI Design", "data": "mar 2023 - set 2024", "texto_pequeno": "Habilidades sendo desenvolvidas:",
    "lista_1": "Experiência e Interface do Usuário", "lista_2": "UX Research, UX Writing, Desk Research", "lista_3": "Jornada do Usuário, Storytelling, Benchmark", "lista_4": "Protótipos de baixa, média e alta fidelidade", "lista_5": "Cores, Tipografia, Gestalt, Layout e Composição", "lista_6": "Figma, Prototipagem e Microinterações", "lista_7": "Design Responsivo, Pixel Perfect Design", "lista_8": "Design Thinking, Testes de Usabilidade"},

    {"nome": "Mapa Educação", "curso": "Curso de liderança política", "data": "jan 2022 - dez 2022", "texto_pequeno": "Conclui o curso Jornada do Líder, que é o processo de formação e preparação de jovens de todo Brasil para atuarem na transformação da realidade educacional de seus municípios. Habilidades desenvolvidas:",
    "lista_1": "Responsabilidade", "lista_2": "Cooperação", "lista_3": "Comunicação", "lista_4": "Pensamento Crítico", "lista_5": "Poder de ação", "lista_6": "Liderança", "lista_7": "Valorização da Diversidade"},

    {"nome": "Colégios Univap Aquarius", "curso": "Ensino Médio regular", "data": "fev 2019 - dez 2022", "texto_pequeno": "Entrei no 9º ano em 2019, realizei o Ensino Médio de 2020 a 2022"},

    {"nome": "Saga - School of Arts, Games and Animation", "curso": "Curso START", "data": "2016 - 2020", "texto_pequeno": "Habilidades desenvolvidas:",
    "lista_1": "Arte Vetorial (Adobe Illustrator)", "lista_2": "Edição de Imagens (Adobe Photoshop)", "lista_3": "Desenho e Pintura Digital (Adobe Photoshop)", "lista_4": "Modelagem 3D (Autodesk Maya, Blender, Zbrush, Substance Painter)", "lista_5": "Animação (Autodesk Maya)", "lista_6": "Edição de Vídeo (Adobe Premiere)", "lista_7": "Composição e Efeito de Vídeo (Adobe After Effects)"},

    {"nome": "Super Geeks", "curso": "Curso de Programação", "data": "2016 - 2017", "texto_pequeno": "Habilidades desenvolvidas:",
    "lista_1": "Lógica de Programação (Python)", "lista_2": "Programação de Jogos (Unity, Unreal Engine, GameMaker, Roblox)"},

    {"nome": "FISK", "curso": "Escola de Inglês", "data": "2014 - 2020", "texto_pequeno": "Notas importantes:",
    "lista_1": "Teste de proficiência internacional MET (Michigan English Test): 69", "lista_2": "Nível CEFR (Common European Framework of Reference): C1"}
    ]

    return render_template("formacao.html", formacao = formacao)




@app.route("/projetos/")
def projetos():
    
    projetos = [{"nome": "Criança Renal", "descricao": "(FATEC API - 1° SEM) Site destinado a conscientizar a população sobre crianças que sofrem de Insuficiência Renal Crônica (IRC), com uma página de blog", "imagem": "/static/img/card_nefro.png", "link": "https://github.com/TeamHiveAPI/API-2023.2", "botao_escrito": "Repositório", "modal": "1"},
    {"nome": "Woodpecker", "descricao": "(FATEC API - 2° SEM) Site de gerenciamento de chamada de serviço (Help Desk) de uma loja de eletrodomésticos", "imagem": "/static/img/card_woodpecker.png", "link": "https://github.com/TeamHiveAPI/API-2024.01", "botao_escrito": "Repositório", "modal": "9"},
    {"nome": "Portal FAPG", "descricao": "(FATEC API - 3° SEM) Portal de transparência da instituição FAPG (Fundação de Apoio à Pesquisa de Pós-Graduandos)", "imagem": "/static/img/card_fapg.png", "link": "https://github.com/A-Sync-Fatec/api-fatec-3sem-24", "botao_escrito": "Repositório", "modal": "10"},  
    {"nome": "Tecsus", "descricao": "(FATEC API - 4° SEM) Sistema IoT de monitoramento climático, focada na coleta e transmissão de dados de estações meteorológicas", "imagem": "/static/img/placeholder.png", "link": "https://github.com/TeamHiveAPI/API-2025.01", "botao_escrito": "Github", "modal": "11"},
    {"nome": "Sistema Almox", "descricao": "(FATEC API - 5° SEM) Aplicativo de gestão de almoxarifado militar com previsão de IA integrada", "imagem": "/static/img/placeholder.png", "link": "https://github.com/TeamHiveAPI/API-2025.02", "botao_escrito": "Github", "modal": "12"},
    {"nome": "Site UNES", "descricao": "Site de uma universidade fictícia integrado com Flask e um banco de dados (MySQL)", "imagem": "/static/img/card_unes.png", "link": "https://github.com/maarantes/Desenvolvimento_Web", "botao_escrito": "Repositório", "modal": "2"},
    {"nome": "Portfólio", "descricao": "Portfólio pessoal (este site!) que reúne as principais informações acadêmicas sobre mim", "imagem": "/static/img/card_portfolio.png", "link": "/", "botao_escrito": "Estamos aqui!", "modal": "3"},
    {"nome": "Projeto Educatech", "descricao": "Projeto de Letramento Digital que desenvolvi ao longo do curso Jornada do Líder no Mapa Educação", "imagem": "/static/img/card_educatech.png", "link": "https://docs.google.com/presentation/d/1QoyCDg5e0w7mHqd7Z8F7pxUwl0SPssPuGIhCnkKW5XY/edit?usp=sharing", "botao_escrito": "Acessar Site", "modal": "4"},
    {"nome": "Estudamat", "descricao": "Projeto da EBAC de um Protótipo Navegável para um aplicativo gamificado de incentivo à aprendizagem de Matemática", "imagem": "/static/img/card_estudamat.png", "link": "https://www.behance.net/gallery/193553035/UXUI-Study-Case-Estudamat", "botao_escrito": "Behance", "modal": "5"},
    {"nome": "Itaú Store", "descricao": "Projeto Final da EBAC de um Protótipo Navegável para um aplicativo de gerenciamento de pontos, milhas e cashback do Banco Itaú", "imagem": "/static/img/card_itau.png", "link": "https://www.behance.net/gallery/194386719/UXUI-Study-Case-Itau-Store", "botao_escrito": "Behance", "modal": "6"},
    ]

    projetos_prof = [{"nome": "Advocacia Thaís", "descricao": "Landing page completa de um escritório de advocacia", "imagem": "/static/img/card_thais.png", "link": "https://thaisadvocacia.vercel.app", "botao_escrito": "Acessar Site", "modal": "7"},
    {"nome": "Arerê Eventos", "descricao": "Branding completo de uma marca que trabalha com eventos", "imagem": "/static/img/card_arere.png", "link": "https://www.behance.net/gallery/193918609/Branding-Arere-Eventos", "botao_escrito": "Behance", "modal": "8"}
    ]
    
    return render_template("projetos.html", projetos = projetos, projetos_prof = projetos_prof)

if __name__ == "__main__":
    app.run(debug=True)