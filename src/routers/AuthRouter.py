import fastapi

router = fastapi.APIRouter(
    tags=["auth"]
)

@router.post("/login")
def login():
    ...

@router.post("/signup")
def signup():
    ...
