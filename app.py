from flask import Flask, jsonify, render_template
import pandas as pd
import pythonping

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/servidores')
def get_servidores():
    # Define os endereços IP dos servidores
    facebook_ip = '31.13.74.35'
    hotmail_ip = '204.79.197.212'
    microsoft_ip = '8.8.4.4'
    open_DNS_ip = '1.1.1.1'
    google_ip = '8.8.8.8'

    # Realiza o ping nos servidores e armazena as informações
    facebook_ping = pythonping.ping(facebook_ip)
    hotmail_ping = pythonping.ping(hotmail_ip)
    microsoft_ping = pythonping.ping(microsoft_ip)
    opendns_ping = pythonping.ping(open_DNS_ip)
    google_ping = pythonping.ping(google_ip)

    # Cria um dataframe com as informações dos servidores
    data = {'Servidor': ['facebook', 'hotmail', 'Microsoft', 'Open DNS', 'Google'],
            'Endereço IP': [facebook_ip, hotmail_ip, microsoft_ip, open_DNS_ip, google_ip],
            'Latência (ms)': [facebook_ping.rtt_avg_ms, hotmail_ping.rtt_avg_ms, microsoft_ping.rtt_avg_ms, opendns_ping.rtt_avg_ms, google_ping.rtt_avg_ms],
            'Status': ['Online' if facebook_ping.success() else 'Offline',
                       'Online' if hotmail_ping.success() else 'Offline',
                       'Online' if microsoft_ping.success() else 'Offline',
                       'Online' if opendns_ping.success() else 'Offline',
                       'Online' if google_ping.success() else 'Offline']}

    df = pd.DataFrame(data)

    # Converte o dataframe em um dicionário e retorna os resultados em JSON
    return jsonify(df.to_dict(orient='records'))


if __name__ == '__main__':
    app.run()

