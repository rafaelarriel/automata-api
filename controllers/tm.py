from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.mt import TuringMachine
from schemas.mt import TuringMachineSchema
from automata.tm.dtm import DTM
from fastapi.responses import StreamingResponse
import io

router = APIRouter(prefix="/turing-machines")

@router.post("")
def create_tm(tm: TuringMachineSchema, db: Session = Depends(get_db)):
    db_tm = TuringMachine(
        name=tm.name,
        states=tm.states,
        input_symbols=tm.input_symbols,
        tape_symbols=tm.tape_symbols,
        transitions=tm.transitions,
        initial_state=tm.initial_state,
        blank_symbol=tm.blank_symbol,
        final_states=tm.final_states
    )
    db.add(db_tm)
    db.commit()
    db.refresh(db_tm)
    return {"message": "Máquina de Turing criada com sucesso", "tm": db_tm}

@router.get("")
def list_all_tm(db: Session = Depends(get_db)):
    tms = db.query(TuringMachine).all()
    return tms

# Endpoint para recuperar uma Máquina de Turing (MT) por ID
@router.get("/{tm_id}")
def get_tm(tm_id: int, db: Session = Depends(get_db)):
    tm = db.query(TuringMachine).filter(TuringMachine.id == tm_id).first()
    if not tm:
        raise HTTPException(status_code=404, detail="Máquina de Turing não encontrada")
    return tm

# Endpoint para testar a aceitação de uma string por uma MT
@router.post("/{tm_id}/accept")
def test_tm_acceptance(tm_id: int, input_string: str, db: Session = Depends(get_db)):
    tm = db.query(TuringMachine).filter(TuringMachine.id == tm_id).first()
    if not tm:
        raise HTTPException(status_code=404, detail="Máquina de Turing não encontrada")
    
    # Cria um objeto DTM a partir dos dados do banco de dados
    tm_model = DTM(
        states=set(tm.states),
        input_symbols=set(tm.input_symbols),
        tape_symbols=set(tm.tape_symbols),
        transitions=tm.transitions,
        initial_state=tm.initial_state,
        blank_symbol=tm.blank_symbol,
        final_states=set(tm.final_states)
    )
    
    # Testa a aceitação da string
    accepts = tm_model.accepts_input(input_string)
    return {"accepts": accepts}

@router.get("/turing-machine/{mt_id}/visualize")
def turing_machine_visualize(mt_id: int, db: Session = Depends(get_db)):
    mt = db.query(TuringMachine).filter(TuringMachine.id == mt_id).first()
    if not mt:
        raise HTTPException(status_code=404, detail="Máquina de Turing não encontrada")

    mt_model = DTM(
        states=set(mt.states),
        input_symbols=set(mt.input_symbols),
        tape_symbols=set(mt.tape_symbols),
        transitions=mt.transitions,
        initial_state=mt.initial_state,
        blank_symbol=mt.blank_symbol,
        final_states=set(mt.final_states)
    )

    dot = mt_model.show_diagram()
    dot.format = "png"

    # Renderiza o diagrama em memória
    image_stream = io.BytesIO(dot.pipe(format="png"))

    # Retorna o arquivo como uma resposta HTTP
    return StreamingResponse(image_stream, media_type="image/png", headers={"Content-Disposition": "inline; filename=automaton.png"})