from sqlalchemy import Column, Integer, String, JSON
from database import Base

class PushdownAutomaton(Base):
    __tablename__ = "pushdown_automata"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    states = Column(JSON)
    input_symbols = Column(JSON)
    stack_symbols = Column(JSON)
    transitions = Column(JSON)
    initial_state = Column(String)
    initial_stack_symbol = Column(String)
    final_states = Column(JSON)