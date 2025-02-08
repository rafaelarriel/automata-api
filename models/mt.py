from sqlalchemy import Column, Integer, String, JSON
from database import Base

class TuringMachine(Base):
    __tablename__ = "turing_machines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    states = Column(JSON)
    input_symbols = Column(JSON)
    tape_symbols = Column(JSON)
    transitions = Column(JSON)
    initial_state = Column(String)
    blank_symbol = Column(String)
    final_states = Column(JSON)