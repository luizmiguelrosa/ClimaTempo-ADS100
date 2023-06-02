from flask import Flask, render_template, abort, url_for
from datetime import datetime
from constants import ESTADOS
from utils import converter_temperatura, pegarClima, pegarPeriodo, pegarImagens
import sys, asyncio, os

app = Flask(__name__)

@app.route("/<cidade>")
def clima(cidade):
    cidade = cidade.title()
    if not "." in cidade:
        clima = asyncio.run(pegarClima(cidade))
        condicao = str(clima.current.kind).upper()
        temperatura = converter_temperatura(clima.current.temperature)
        
        clima_seguinte = [forecast for forecast in clima.forecasts][1]
        temperatura_seguinte = converter_temperatura(clima_seguinte.temperature)

        horario = datetime.now().strftime("%H:%M")
        periodo = pegarPeriodo(horario)
        
        icone, fundo = pegarImagens(ESTADOS[condicao], periodo)
        
        icone_condicao = url_for('static', filename=f'img/{icone}')
        fundo_horario = url_for('static', filename=f'img/{fundo}')

        return render_template("index.html", cidade=cidade, condicao=ESTADOS[condicao], temperatura=temperatura, temperatura_seg=temperatura_seguinte, horario=horario, icone_condicao=icone_condicao, fundo=fundo_horario)
    return abort(404)

if __name__ == "__main__":
    app.run(debug=True, host=sys.argv[1], port=sys.argv[2])
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())