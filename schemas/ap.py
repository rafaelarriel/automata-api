from pydantic import BaseModel
from typing import Dict, List

class PushdownAutomatonSchema(BaseModel):
    name: str
    states: List[str]
    input_symbols: List[str]
    stack_symbols: List[str]
    transitions: Dict[str, Dict[str, Dict[str, List]]]  # Sem tuplas
    initial_state: str
    initial_stack_symbol: str
    final_states: List[str]
