from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.afd import DeterministicFiniteAutomaton
from schemas.afd import DeterministicFiniteAutomatonSchema
from automata.fa.dfa import DFA
from fastapi.responses import StreamingResponse
import io

router = APIRouter(prefix="/deterministic-finite-automaton")

# Endpoint para criar um Autômato Finito Determinístico (AFD)
@router.post("")
def create_dfa(dfa: DeterministicFiniteAutomatonSchema, db: Session = Depends(get_db)):
    db_dfa = DeterministicFiniteAutomaton(
        name=dfa.name,
        states=dfa.states,
        input_symbols=dfa.input_symbols,
        transitions=dfa.transitions,
        initial_state=dfa.initial_state,
        final_states=dfa.final_states
    )
    db.add(db_dfa)
    db.commit()
    db.refresh(db_dfa)
    return {"message": "DFA criado com sucesso", "dfa": db_dfa}

@router.get("")
def list_all_dfa(db: Session = Depends(get_db)):
    dfas = db.query(DeterministicFiniteAutomaton).all()
    return dfas

# Endpoint para recuperar um Autômato Finito Determinístico (AFD) por ID
@router.get("/{dfa_id}")
def get_dfa(dfa_id: int, db: Session = Depends(get_db)):
    dfa = db.query(DeterministicFiniteAutomaton).filter(DeterministicFiniteAutomaton.id == dfa_id).first()
    if not dfa:
        raise HTTPException(status_code=404, detail="DFA não encontrado")
    return dfa

# Endpoint para testar a aceitação de uma string por um AFD
@router.post("/{dfa_id}/accept")
def test_dfa_acceptance(dfa_id: int, input_string: str, db: Session = Depends(get_db)):
    dfa = db.query(DeterministicFiniteAutomaton).filter(DeterministicFiniteAutomaton.id == dfa_id).first()
    if not dfa:
        raise HTTPException(status_code=404, detail="DFA não encontrado")
    
    # Cria um objeto DFA a partir dos dados do banco de dados
    dfa_model = DFA(
        states=set(dfa.states),
        input_symbols=set(dfa.input_symbols),
        transitions=dfa.transitions,
        initial_state=dfa.initial_state,
        final_states=set(dfa.final_states)
    )
    
    # Testa a aceitação da string
    accepts = dfa_model.accepts_input(input_string)
    return {"accepts": accepts}

@router.get("/{afd_id}/visualize")
def deterministic_finite_automaton_visualize(afd_id: int, db: Session = Depends(get_db)):
    afd = db.query(DeterministicFiniteAutomaton).filter(DeterministicFiniteAutomaton.id == afd_id).first()
    if not afd:
        raise HTTPException(status_code=404, detail="Autômato Finito Determinístico não encontrado")

    afd_model = DFA(
        states=set(afd.states),
        input_symbols=set(afd.input_symbols),
        transitions=afd.transitions,
        initial_state=afd.initial_state,
        final_states=set(afd.final_states)
    )

    # Gera o diagrama do autômato
    dot = afd_model.show_diagram()
    dot.format = "png"

    # Renderiza o diagrama em memória
    image_stream = io.BytesIO(dot.pipe(format="png"))

    # Retorna o arquivo como uma resposta HTTP
    return StreamingResponse(image_stream, media_type="image/png", headers={"Content-Disposition": "inline; filename=automaton.png"})