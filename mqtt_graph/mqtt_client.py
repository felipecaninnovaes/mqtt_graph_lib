import json
import os
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import paho.mqtt.client as mqtt
from .utils import PayloadFilter

class IMQTTClient:
    def connect(self, broker_address: str, port: int = 1883, keepalive: int = 60):
        pass

    def subscribe(self, topic: str):
        pass

    def loop_start(self):
        pass

    def username_pw_set(self, username: str, password: str):
        pass

class PahoMQTTClient(IMQTTClient):
    def __init__(self):
        self.client = mqtt.Client()

    def connect(self, broker_address: str, port: int = 1883, keepalive: int = 60):
        self.client.connect(broker_address, port, keepalive)

    def subscribe(self, topic: str):
        self.client.subscribe(topic)

    def loop_start(self):
        self.client.loop_start()

    def username_pw_set(self, username: str, password: str):
        self.client.username_pw_set(username, password)

@dataclass
class MQTTClient:
    broker_address: str
    username: str
    password: str
    topic: str
    filters: List[str]
    client: IMQTTClient = field(default_factory=PahoMQTTClient)
    messages: List[Dict[str, Any]] = field(default_factory=list, init=False)

    def __post_init__(self):
        self.client.username_pw_set(self.username, self.password)
        try:
            self.client.connect(self.broker_address)
        except Exception as e:
            print(f"Erro ao conectar ao broker: {e}")
            return
        result = self.client.subscribe(self.topic)
        if result is not None and result != mqtt.MQTT_ERR_SUCCESS:
            print(f"Falha ao assinar o tópico: {self.topic}")
            return

    def on_connect(self, client: mqtt.Client, userdata: Any, flags: Dict[str, Any], rc: int):
        if rc == 0:
            print("Conectado ao broker com sucesso.")
        else:
            print(f"Falha na conexão com o broker. Código de retorno: {rc}")

    def on_message(self, client: mqtt.Client, userdata: Any, msg: mqtt.MQTTMessage, filters: List[str]) -> Any:
        payload = PayloadFilter(msg.payload, filters)
        if payload:
            self.messages.append(payload)
        return payload

    def connect_and_subscribe(self):
        self.client.connect(self.broker_address, 1883, 60)
        self.client.subscribe(self.topic)
        self.client.loop_start()