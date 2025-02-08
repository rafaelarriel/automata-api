from sqlalchemy import Column, Integer, String, JSON
from database import Base

class DeterministicFiniteAutomaton(Base):
    __tablename__ = "deterministic_finite_automata"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    states = Column(JSON)
    input_symbols = Column(JSON)
    transitions = Column(JSON)
    initial_state = Column(String)
    final_states = Column(JSON)