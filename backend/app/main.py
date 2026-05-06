from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import clientes, equipamentos, relatorios, auth, funcionarios

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestão de Assistência Técnica")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router)
app.include_router(equipamentos.router)
app.include_router(relatorios.router)
app.include_router(auth.router)
app.include_router(funcionarios.router)

@app.get("/")
def root():
    return {
        "message": "Sistema de Gestão de Assistência Técnica",
        "version": "1.0.0",
        "docs": "/docs"
    }
