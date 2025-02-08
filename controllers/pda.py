from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.ap import PushdownAutomaton
from schemas.ap import PushdownAutomatonSchema
from automata.pda.dpda import DPDA
from fastapi.responses import StreamingResponse
import io

router = APIRouter(prefix="/pushdown-automata")

# Endpoint para criar um Autômato com Pilha (AP)
@router.post("")
def create_pda(pda: PushdownAutomatonSchema, db: Session = Depends(get_db)):
    db_pda = PushdownAutomaton(
        name=pda.name,
        states=pda.states,
        input_symbols=pda.input_symbols,
        stack_symbols=pda.stack_symbols,
        transitions=pda.transitions,
        initial_state=pda.initial_state,
        initial_stack_symbol=pda.initial_stack_symbol,
        final_states=pda.final_states
    )
    db.add(db_pda)
    db.commit()
    db.refresh(db_pda)
    return {"message": "PDA criado com sucesso", "pda": db_pda}

@router.get("")
def list_all_pda(db: Session = Depends(get_db)):
    pdas = db.query(PushdownAutomaton).all()
    return pdas

# Endpoint para recuperar um Autômato com Pilha (AP) por ID
@router.get("/{pda_id}")
def get_pda(pda_id: int, db: Session = Depends(get_db)):
    pda = db.query(PushdownAutomaton).filter(PushdownAutomaton.id == pda_id).first()
    if not pda:
        raise HTTPException(status_code=404, detail="PDA não encontrado")
    return pda

# Endpoint para testar a aceitação de uma string por um AP
@router.post("/{pda_id}/accept")
def test_pda_acceptance(pda_id: int, input_string: str, db: Session = Depends(get_db)):
    pda = db.query(PushdownAutomaton).filter(PushdownAutomaton.id == pda_id).first()
    if not pda:
        raise HTTPException(status_code=404, detail="PDA não encontrado")
    
    # Cria um objeto DPDA a partir dos dados do banco de dados
    pda_model = DPDA(
        states=set(pda.states),
        input_symbols=set(pda.input_symbols),
        stack_symbols=set(pda.stack_symbols),
        transitions=pda.transitions,
        initial_state=pda.initial_state,
        initial_stack_symbol=pda.initial_stack_symbol,
        final_states=set(pda.final_states)
    )
    
    # Testa a aceitação da string
    accepts = pda_model.accepts_input(input_string)
    return {"accepts": accepts}

@router.get("/{ap_id}/visualize")
def pushdown_automaton_visualize(ap_id: int, db: Session = Depends(get_db)):
    ap = db.query(PushdownAutomaton).filter(PushdownAutomaton.id == ap_id).first()
    if not ap:
        raise HTTPException(status_code=404, detail="Autômato com Pilha não encontrado")

    ap_model = DPDA(
        states=set(ap.states),
        input_symbols=set(ap.input_symbols),
        stack_symbols=set(ap.stack_symbols),
        transitions=ap.transitions,
        initial_state=ap.initial_state,
        initial_stack_symbol=ap.initial_stack_symbol,
        final_states=set(ap.final_states)
    )

    dot = ap_model.show_diagram()
    dot.format = "png"

    # Renderiza o diagrama em memória
    image_stream = io.BytesIO(dot.pipe(format="png"))

    # Retorna o arquivo como uma resposta HTTP
    return StreamingResponse(image_stream, media_type="image/png", headers={"Content-Disposition": "inline; filename=automaton.png"})