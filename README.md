# Mutual Fund Returns Calculator

This project implements a simple FastAPI application to calculate the profit for a mutual fund investment based on scheme code, purchase date, redemption date, and initial investment capital.

## Project Structure

- **`src/app/`**: Contains the FastAPI application code.
- **`tests/`**: Contains test files for the FastAPI endpoints.
- **`README.md`**: This file, providing an overview of the project.
- **`requirements.txt`**: This file, providing an requirements of the project.


## Usage

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/mutual_fund_calculator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mutual_fund_calculator
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Basic Authorization
set the env file provided for security variables and authentcation 


### Running the Application

Run the FastAPI application:

```bash
uvicorn src.app.main:app --reload
```
add the env content from the .env file provided.

Access the API at http://127.0.0.1:8000.


### Authorizing app
Authorize app using the user_is and password from the env file

### Running Tests
Execute the tests using pytest:

```bash
pytest
```

## API Endpoint
/profit
Description: Calculates the profit for a mutual fund investment.
HTTP Method: GET
Query Parameters:
scheme_code: Unique scheme code of the mutual fund.
start_date: Purchase date of the mutual fund (format: dd-mm-yyyy).
end_date: Redemption date of the mutual fund (format: dd-mm-yyyy).
capital: Initial investment amount (optional, default: 1000000.0).
Example usage:

```bash
GET /profit?scheme_code=101206&start_date=26-07-2023&end_date=18-10-2023&capital=1000000
```

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License.