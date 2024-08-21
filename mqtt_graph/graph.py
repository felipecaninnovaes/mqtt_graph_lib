import matplotlib.pyplot as plt
from typing import Optional
from dataclasses import dataclass

@dataclass
class Message:
    """
    Representa uma mensagem com uma chave e um valor.

    Atributos:
        key: A chave da mensagem.
        value: O valor da mensagem.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get(self, attribute):
        """
        Retorna o valor do atributo especificado.

        Parâmetros:
            attribute: O nome do atributo ('key' ou 'value').

        Retorna:
            O valor do atributo especificado.

        Levanta:
            AttributeError: Se o atributo não for 'key' ou 'value'.
        """
        if attribute == 'key':
            return self.key
        elif attribute == 'value':
            return self.value
        else:
            raise AttributeError(f"'Message' object has no attribute '{attribute}'")

class LineOption:
    """
    Representa as opções de uma linha no gráfico.

    Atributos:
        label: O rótulo da linha.
        key: A chave associada à linha.
        color: A cor da linha (opcional).
    """
    def __init__(self, label: str, key: str, color: Optional[str] = None):
        self.label = label
        self.key = key
        self.color = color

class Graph:
    """
    Representa um gráfico que exibe valores de mensagens ao longo do tempo.

    Atributos:
        messages: Uma lista de mensagens a serem exibidas.
        line_options: As opções de configuração das linhas do gráfico.
        fig: A figura do matplotlib.
        ax: O eixo do matplotlib.
        plot_func: A função de plotagem do matplotlib.
        lines: As linhas do gráfico inicializadas.
    """
    def __init__(self, messages, line_options, fig, ax, plot_func):
        self.messages = messages
        self.line_options = line_options
        self.fig = fig
        self.ax = ax
        self.plot_func = plot_func
        self.lines = self.init()

    def init(self):
        """
        Inicializa as linhas do gráfico com base nas opções de linha.

        Retorna:
            Uma lista de linhas do matplotlib.
        """
        lines = []
        for line_option in self.line_options:
            # Encontra a mensagem correspondente à chave da linha
            message = next((msg for msg in self.messages if msg.get('key') == line_option.key), None)
            if message:
                # Cria uma linha no gráfico
                line, = self.ax.plot([], [], label=line_option.label, color=line_option.color)
                lines.append(line)
        # Configurações iniciais do gráfico
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 1)
        self.ax.set_xlabel('Mensagem')
        self.ax.set_ylabel('Valor')
        self.ax.set_title('Valores dos estados ao longo do tempo')
        return lines

    def calculate_values(self):
        """
        Calcula os valores das mensagens para cada linha do gráfico.

        Retorna:
            Uma lista de listas de valores.
        """
        values = [[msg.get('value') if msg.get('key') == line_option.key else 0 for line_option in self.line_options] for msg in self.messages]
        return values

    def calculate_limits(self, values):
        """
        Calcula os limites mínimo e máximo dos valores.

        Parâmetros:
            values: Uma lista de listas de valores.

        Retorna:
            Uma tupla contendo o valor mínimo e o valor máximo.
        """
        min_value = min(min(value) for value in values)
        max_value = max(max(value) for value in values)
        return min_value, max_value

    def update(self, frame):
        """
        Atualiza o gráfico com novos valores.

        Parâmetros:
            frame: O quadro atual da animação.
        """
        values = self.calculate_values()
        for line, value in zip(self.lines, values):
            # Atualiza os dados da linha
            line.set_data(range(len(value)), value)
        # Atualiza os limites do gráfico
        self.ax.set_xlim(0, len(self.messages))
        self.ax.set_ylim(min(value for sublist in values for value in sublist), max(value for sublist in values for value in sublist))
        self.fig.canvas.draw()