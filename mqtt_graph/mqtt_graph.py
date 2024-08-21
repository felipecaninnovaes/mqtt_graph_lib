import json
from typing import List
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mqtt_graph import LineOption, MQTTClient, Graph
from dataclasses import dataclass

@dataclass
class Message:
    """
    Representa uma mensagem com uma chave e um valor.

    Atributos:
        key (str): A chave da mensagem.
        value (float): O valor associado à chave.
    """
    key: str
    value: float

class MQTTGraph:
    def __init__(self, broker_address: str, username: str, password: str, topic: str, line_options: List[LineOption], filter_keys: List[str]):
        """
        Inicializa a classe MQTTGraph.

        Parâmetros:
            broker_address (str): Endereço do broker MQTT.
            username (str): Nome de usuário para autenticação no broker.
            password (str): Senha para autenticação no broker.
            topic (str): Tópico MQTT para subscrever.
            line_options (List[LineOption]): Configurações das linhas do gráfico.
            filter_keys (List[str]): Chaves para filtrar as mensagens recebidas.
        """
        self.broker_address = broker_address
        self.username = username
        self.password = password
        self.topic = topic
        self.line_options = line_options
        self.filter_keys = filter_keys
        self.messages: List[Message] = []
        self.graph_generator = Graph(self.messages, self.line_options)
        self.client = MQTTClient(self.broker_address, self.username, self.password, self.topic, self.filter_keys).client
        self.client.on_message = self.on_message

    def on_message(self, client, userdata, msg):
        """
        Callback executado quando uma mensagem é recebida.

        Parâmetros:
            client: Instância do cliente MQTT.
            userdata: Dados definidos pelo usuário.
            msg: Mensagem recebida.
        """
        payload = msg.payload.decode('utf-8')
        data = json.loads(payload)
        self.messages.append(data)
        if len(self.messages) > 100:  # Limitar o número de mensagens armazenadas
            self.messages.pop(0)

    def start(self):
        """
        Inicia o cliente MQTT e a animação do gráfico.
        """
        self.client.loop_start()
        ani = FuncAnimation(self.graph_generator.fig, self.graph_generator.update, init_func=self.graph_generator.init, blit=True)
        plt.show()
        self.stop()

    def stop(self):
        """
        Para o cliente MQTT e desconecta.
        """
        self.client.loop_stop()
        self.client.disconnect()
        print("Conexão encerrada com sucesso!")