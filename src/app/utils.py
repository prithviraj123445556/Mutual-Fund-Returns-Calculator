import requests
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from src.app.exceptions import SchemeCodeNotFound, InvalidDate ,InvalidCapitalAmount
from fastapi.security import HTTPBasicCredentials
import os
from dotenv import load_dotenv


def get_nav_from_api(scheme_code, date):
    """
    Fetches NAV (Net Asset Value) from an API for a given scheme code and date.
    """
    try:
        load_dotenv()
        api_url = os.getenv("API_URL")
        full_api_url = f"{api_url}/{scheme_code}"
        response = requests.get(full_api_url)
        
        if response.status_code == 200:
            data = response.json()['data']
            
            if not data: 
                raise SchemeCodeNotFound()
                
            for entry in data:
                if entry['date'] == date:
                    return entry['nav']
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found") 

    except SchemeCodeNotFound:
        raise  

    except HTTPException as e:
        raise e 

    

def calculate_profit(scheme_code, start_date, end_date, capital=1000000.0):
    """
    Calculates the net profit of a mutual fund investment.
    """
    try:
        try:
            start_date = datetime.strptime(start_date, '%d-%m-%Y')
            end_date = datetime.strptime(end_date, '%d-%m-%Y')
        except ValueError:
            raise InvalidDate("Invalid date format. Please provide dates in 'dd-mm-yyyy' format.")
        
        try:
            capital = float(capital)
        except ValueError:
            raise InvalidCapitalAmount()
        
        current_date = start_date
        while current_date <= end_date:
            nav = get_nav_from_api(scheme_code, current_date.strftime('%d-%m-%Y'))
            nav = float(nav)
            if nav:
                break
            current_date += timedelta(days=1)

        if not nav:
            raise("NAV data not available for the provided dates.")

        units_allotted = capital / nav

        current_end_date = end_date
        while True:
            redemption_nav = get_nav_from_api(scheme_code, current_end_date.strftime('%d-%m-%Y'))
            redemption_nav = float(redemption_nav)
            if redemption_nav:
                break
            current_end_date += timedelta(days=1)
        value_on_redemption = units_allotted * redemption_nav
        net_profit = value_on_redemption - capital
        return net_profit
    
    except InvalidDate:
        raise  

    except InvalidCapitalAmount:
        raise  

    except HTTPException as e:
        raise e  
    

def verify_credentials(credentials: HTTPBasicCredentials):
    """
    Verifies user credentials.
    """
    load_dotenv()
    username = os.getenv("USERID")
    password = os.getenv("PASSWORD")

    if credentials.username == username and credentials.password == password:
        return True
    return False
