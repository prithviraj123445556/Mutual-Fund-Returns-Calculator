from fastapi import APIRouter, HTTPException, Query, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi import Response, status
from src.app.utils import calculate_profit ,verify_credentials
from src.app.schemas import ErrorBase, NetProfitResponse
from src.app.exceptions import SchemeCodeNotFound, InvalidDate, InvalidCapitalAmount
from src.app.logger import logger
from fastapi.responses import FileResponse


router = APIRouter()
security = HTTPBasic()


@router.get("/profit", status_code=200, response_model=NetProfitResponse, responses={
    500: {"model": ErrorBase, "description": "Internal Server Error"}
})
async def calculate_mutual_fund_profit(
    response: Response,
    credentials: HTTPBasicCredentials = Depends(security),
    scheme_code: str = Query(..., description="The unique scheme code of the mutual fund."),
    start_date: str = Query(..., description="The purchase date of the mutual fund."),
    end_date: str = Query(..., description="The redemption date of the mutual fund."),
    capital: Optional[float] = Query(1000000.0, description="The initial investment amount.")
):
     """
    Calculates mutual fund net profit.
    """
    if not verify_credentials(credentials):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    try:
        scheme_code = scheme_code.strip()
        start_date = start_date.strip()
        end_date = end_date.strip()

        net_profit = calculate_profit(scheme_code, start_date, end_date, capital)  
        return NetProfitResponse(net_profit=net_profit) 

    except SchemeCodeNotFound as e:
        logger.error(f"Scheme code not found: {e}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    except InvalidDate as e:
        logger.error(f"Invalid date: {e}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except InvalidCapitalAmount as e:
        logger.error(f"Invalid capital amount: {e}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    except Exception as e:
        error_response = ErrorBase(error=str(e))
        return JSONResponse(error_response.dict(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


@router.get("/")
async def read_index():
     """
    Serves index.html file.
    """
    return FileResponse("templates/index.html")
