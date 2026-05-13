from fastapi import APIRouter

router = APIRouter(prefix="/automation", tags=["Automation"])


@router.post("/create")
def create_automation_rule():

    return {
        "message": "Automation Rule Created"
    }