from fastapi import FastAPI
from controllers.dfa import router as dfa_router
from controllers.pda import router as pda_router
from controllers.tm import router as tm_router

app = FastAPI()

app.include_router(dfa_router, tags=["Deterministic Finite Automaton"])
app.include_router(pda_router, tags=["Pushdown Automaton"])
app.include_router(tm_router, tags=["Turing Machine"])
