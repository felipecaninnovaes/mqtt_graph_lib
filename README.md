**Título:** Biblioteca de Processamento e Visualização de Dados IoT em Tempo Real com Python e MQTT

**Resumo:**
Este trabalho de extensão visa desenvolver uma biblioteca em Python que facilite a visualização das mensagens do protocolo MQTT em tempo real, utilizando gráficos para facilitar o processamento dos dados. A biblioteca será projetada para agilizar a análise e compreensão dos dados de sensores IoT sem a necessidade de armazenamento em bancos de dados.

**Objetivos:**

1. Desenvolver uma biblioteca que lida com mensagens MQTT em tempo real.
2. Criar gráficos personalizáveis para visualizar os dados de sensores ou outros dispositivos que se comunica por MQTT.

**Tecnologias Utilizadas:**

* Python como linguagem de programação principal.
* Biblioteca paho-mqtt para lidar com MQTT.
* Bibliotecas gráficas como Matplotlib para criação de gráficos.
* Conhecimento de conceitos de IoT e Big Data.

**Biblioteca Proposta:**

A biblioteca será projetada para ser facilmente integrável em qualquer ambiente Python. Ela fornecerá as seguintes funcionalidades:

1. **Leitura de Mensagens MQTT:** A biblioteca se conectará ao broker MQTT e lerá mensagens de sensores IoT.
2. **Armazenamento em Memória:** Dados serão armazenados em memória para permitir a visualização imediata.
3. **Visualização de Gráficos:** Utilizando bibliotecas gráficas, a biblioteca gerará gráficos personalizáveis para representar os dados dos sensores em tempo real.

**Arquitetura da Biblioteca:**

A arquitetura da biblioteca seguirá as seguintes etapas:

1. Conexão ao Broker MQTT.
2. Leitura e tratamento das mensagens.
3. Armazenamento em memória.
4. Visualização gráfica dos dados.

**Timeline Proposta:**

O projeto é estimado para ser concluído em 1 meses, com as seguintes etapas:

* Mês 1: Definição das funcionalidades e revisão da literatura.
* Mês 2-3: Desenvolvimento incremental da biblioteca e implementação de funcionalidades.

**Cronograma:**

| Semana | Atividade |
| --- | --- |
| 1 | Revisão e planejamento |
| 2 | Implementação da conexão ao broker MQTT e armazenamento em memória |
| 3 | Desenvolvimento das funcionalidades de visualização gráfica |
| 4 | Desenvolvimento da documentação |

A biblioteca será submetida a testes para garantir sua estabilidade e eficiência.

**Conclusão:**

Este trabalho de extensão visa criar uma ferramenta útil para os desenvolvedores

**Implementação**
- **Instalação**
``` sh
git clone https://github.com/felipecaninnovaes/mqtt_graph_lib
python -m pip install .
```
- **Usando MQTT**

Criar ou adicionar as Variaveis de Ambiente.

``` env
BROKER_ADDRESS = "Endereço do broker MQTT"
USERNAME = "Usuario"
PASSWORD = "Senha"
```
Adicionar o seguinte codigo para utilizar a biblioteca.
``` python
from mqtt_graph import LineOption, MQTTGraph
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do cliente MQTT
broker_address = os.getenv("BROKER_ADDRESS")  # Endereço do broker MQTT
username = os.getenv("USERNAME")  # Nome de usuário para autenticação no broker
password = os.getenv("PASSWORD")  # Senha para autenticação no broker
topic = "zigbee2mqtt/Interruptor quarto"  # Tópico MQTT
filters = ["state_l1", "state_l2"]  # Filtros

# Configurações das linhas do gráfico
line_options = [
    LineOption(label='Botão 1', key='state_l1', color='blue'),  # Configuração da linha para o estado do botão 1
    LineOption(label='Botão 2', key='state_l2', color='orange'),  # Configuração da linha para o estado do botão 2
]

# Inicializa e inicia o gráfico MQTT
# MQTTGraph é responsável por conectar ao broker MQTT, escutar o tópico especificado,
# filtrar as mensagens recebidas e atualizar o gráfico com base nas opções de linha fornecidas.
MQTTGraph(broker_address, username, password, topic, line_options, filter_keys=filters).start()
```


**Integrantes** 

Felipe Canin Novaes: **Documentação/Desenvolvimento**
