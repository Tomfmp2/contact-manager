import json # Importando herramientas 
import os
from typing import Dict, List, Optional, Any, Union, Callable


JSON_CUENTAS = "data/JsonCuentas.json"
JSON_USUARIO = "data/JsonUsuario.json"

# Creacion de archivo json
def ReadJson(file_path: str)-> Dict:
    try:
        with open(file_path, "r", encoding="utf-8") as ArchivoJson:
            return json.load(ArchivoJson)
    except FileNotFoundError:
        return {}
    
def WriteJson(file_path: str, data: Dict) -> None:
    with open(file_path, "w", encoding="utf-8") as ArchivoJson:
        json.dump(data, ArchivoJson, indent=4)

def UpdateJson(file_path: str, data: Dict, path: Optional[list[str]] = None) -> None:
    CurrentData = ReadJson(file_path)
    if not path:
        CurrentData.update(data)
    else:
        current = CurrentData
        for key in path[:-1]:
            current = current.setdefault(key, {})
        current.setdefault(path[-1], {}).update(data)
    WriteJson(file_path, CurrentData)

def InitJson(file_path: str, initial_structure: Dict) -> None:
    if not os.path.isfile(file_path):
        WriteJson(file_path, initial_structure)
    else:
        current_data = ReadJson(file_path)
        for key, value in initial_structure.items():
            if key not in current_data:
                current_data[key] = value
        WriteJson(file_path, current_data)
        
