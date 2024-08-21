import unittest
from unittest.mock import MagicMock, patch
import matplotlib.pyplot as plt
from mqtt_graph import Message, LineOption, Graph, MQTTClient, IMQTTClient, PayloadFilter
from dotenv import load_dotenv
import os, sys, json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'mqtt_graph'))

load_dotenv()

class TestMessage(unittest.TestCase):
    def test_message_creation(self):
        msg = Message(key="test_key", value=10.5)
        self.assertEqual(msg.key, "test_key")
        self.assertEqual(msg.value, 10.5)

class TestLineOption(unittest.TestCase):
    def test_line_option_creation_with_color(self):
        line_option = LineOption(label="Test Label", key="test_key", color="blue")
        self.assertEqual(line_option.label, "Test Label")
        self.assertEqual(line_option.key, "test_key")
        self.assertEqual(line_option.color, "blue")

    def test_line_option_creation_without_color(self):
        line_option = LineOption(label="Test Label", key="test_key")
        self.assertEqual(line_option.label, "Test Label")
        self.assertEqual(line_option.key, "test_key")
        self.assertIsNone(line_option.color)

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.messages = [Message('key1', 0.1), Message('key2', 0.2)]
        self.line_options = [LineOption('Line 1', 'key1', 'blue'), LineOption('Line 2', 'key2', 'red')]
        self.fig, self.ax = plt.subplots()  # Garantir que plt.subplots() retorne fig e ax
        self.plot_func = MagicMock()
        self.graph = Graph(self.messages, self.line_options, self.fig, self.ax, self.plot_func)

    def test_initialization(self):
        self.assertEqual(len(self.graph.lines), 2)
        self.assertEqual(self.graph.ax.get_xlabel(), 'Mensagem')
        self.assertEqual(self.graph.ax.get_ylabel(), 'Valor')
        self.assertEqual(self.graph.ax.get_title(), 'Valores dos estados ao longo do tempo')

    def test_init(self):
        lines = self.graph.init()
        self.assertEqual(len(lines), 2)
        self.assertEqual(self.graph.ax.get_xlim(), (0, 100))
        self.assertEqual(self.graph.ax.get_ylim(), (0, 1))

    def test_calculate_values(self):
        values = self.graph.calculate_values()
        self.assertEqual(values, [[0.1, 0.0], [0.0, 0.2]])

    def test_calculate_limits(self):
        messages = [Message('key1', 0.0), Message('key2', 0.2)]
        line_options = [LineOption('Label1', 'key1'), LineOption('Label2', 'key2')]
        fig, ax = plt.subplots()
        graph = Graph(messages, line_options, fig, ax, None)
        
        values = graph.calculate_values()
        limits = graph.calculate_limits(values)
        
        self.assertEqual(limits, (0.0, 0.2))  # Ajuste o valor esperado conforme necessário


    def test_update(self):
        self.graph.update(0)
        self.assertEqual(self.graph.ax.get_xlim(), (0, len(self.messages)))
        self.assertEqual(self.graph.ax.get_ylim(), (0.0, 0.2))

if __name__ == '__main__':
    unittest.main()