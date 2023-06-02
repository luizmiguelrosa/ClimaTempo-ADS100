from python_weather import Client, IMPERIAL
from constants import ESTILOS

converter_temperatura = lambda f: round((f -32) * 5/9)

async def pegarClima(cidade):
    async with Client(unit=IMPERIAL) as cliet:
        clima = await cliet.get(cidade)
        return clima

def pegarImagens(condicao, periodo):
    for estilo in ESTILOS:
        if periodo in estilo["periodos"] and condicao in estilo["condicoes"]:
            break
    return list(estilo["condicoes"][condicao].values())

def pegarPeriodo(horario):
    horas = int(horario[:2])

    if 0 <= horas <= 5:
        periodo = "Madrugada"
    elif 6 <= horas <= 11:
        periodo = "Manhã"
    elif 12 <= horas <= 17:
        periodo = "Tarde"
    elif 18 <= horas <= 23:
        periodo = "Noite"
    
    return periodo