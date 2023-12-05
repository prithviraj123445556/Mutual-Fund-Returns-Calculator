from fastapi import HTTPException
from starlette import status


class SchemeCodeNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Scheme code not found",)

class InvalidDate(HTTPException):
    def __init__(self,detail="Invalid date"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid date",
        )

class InvalidCapitalAmount(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid capital amount. Please provide a valid number.",
        )