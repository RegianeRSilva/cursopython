from plyer import notification
from datetime import datetime
from notifypy import notify

def alerta(nivel, base, etapa):

    nivel_titulo = {
        1: "Alerta Baixo",
        2: "Alerta Médio",
        3: "Alerta Alto"
    }

    titulo = nivel_titulo.get(nivel, "Alerta Desconhecido")

    mensagem = f"Falha no carregamento da base {base} na etapa {etapa}"

    notification.notify(title=titulo, message=mensagem, timeout=10)


alerta(nivel=int(input("Digite o nível (1 para Baixo, 2 para Médio, 3 para Alto): ")), base='Minhabase', etapa='carregamento')