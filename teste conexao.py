
from flask import Flask, jsonify
import pandas as pd
import ping3

app = Flask(__name__, static_folder='static')

@app.route('/servidores')
def get_servidores():
    # Define os endereços IP dos servidores
    active_directory_ip = '192.168.1.143'
    whaticket_ip = '192.168.1.204'
    cativo_vpn_ip = '192.168.2.200'
    rio_lider_vpn_ip = '192.168.9.1'
    internet_ip = '8.8.8.8'

    # Realiza o ping nos servidores e armazena as informações
    active_directory_ping = ping3.ping(active_directory_ip)
    whaticket_ping = ping3.ping(whaticket_ip)
    cativo_vpn_ping = ping3.ping(cativo_vpn_ip)
    rio_lider_vpn_ping = ping3.ping(rio_lider_vpn_ip)
    internet_ping = ping3.ping(internet_ip)

    # Cria um dataframe com as informações dos servidores
    data = {'Servidor': ['Active Directory', 'WhaTicket', 'VPN da Cativo', 'VPN da Rio Lider', 'Internet'],
            'Endereço IP': [active_directory_ip, whaticket_ip, cativo_vpn_ip, rio_lider_vpn_ip, internet_ip],
            'Latência (ms)': [active_directory_ping, whaticket_ping, cativo_vpn_ping, rio_lider_vpn_ping, internet_ping]}
    df = pd.DataFrame(data)

    # Converte o dataframe em um dicionário e retorna os resultados em JSON
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run()


