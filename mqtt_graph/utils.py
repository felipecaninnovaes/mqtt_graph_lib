from typing import List, Dict, Any
import json
import os

class PayloadFilter:
    def __init__(self, payload: str, arguments: List[str]):
        self.payload = payload
        self.arguments = arguments
        self.payload_dict = self._load_payload()

    def _load_payload(self) -> Dict[str, Any]:
        try:
            return json.loads(self.payload)
        except json.JSONDecodeError:
            print("Erro: Payload JSON inválido.")
            return {}

    def filter(self) -> Dict[str, Any]:
        result = {}
        for argument in self.arguments:
            result[argument] = self.payload_dict.get(argument, os.getenv(argument, "Argumento não encontrado na carga útil e variável de ambiente não definida"))
        return result