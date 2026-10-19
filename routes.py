from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"status": "success", "message": "DevSecOps Python API Active"}

@router.get("/health")
def health_check():
    return {"status": "healthy", "service": "python-fastapi"}
