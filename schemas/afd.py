from pydantic import BaseModel
from typing import Dict, List

class DeterministicFiniteAutomatonSchema(BaseModel):
    name: str
    states: List[str]
    input_symbols: List[str]
    transitions: Dict[str, Dict[str, str]]
    initial_state: str
    final_states: List[str]
