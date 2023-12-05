from fastapi import HTTPException
from starlette import status

# Custom exception for Scheme Code Not Found
class SchemeCodeNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,  # HTTP 404 status code for resource not found
            detail="Scheme code not found",  # Error message for this exception
        )

# Custom exception for Invalid Date
class InvalidDate(HTTPException):
    def __init__(self, detail="Invalid date"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,  # HTTP 400 status code for bad request
            detail="Invalid date",  # Error message for this exception
        )

# Custom exception for Invalid Capital Amount
class InvalidCapitalAmount(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,  # HTTP 400 status code for bad request
            detail="Invalid capital amount. Please provide a valid number.",  # Error message for this exception
        )
