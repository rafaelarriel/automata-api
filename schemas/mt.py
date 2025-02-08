from pydantic import BaseModel
from typing import Dict, List

class TuringMachineSchema(BaseModel):
    name: str
    states: List[str]
    input_symbols: List[str]
    tape_symbols: List[str]
    transitions: Dict[str, Dict[str, List[str]]]
    initial_state: str
    blank_symbol: str
    final_states: List[str]
