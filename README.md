# FastApi_Singin_up

This project demonstrates a **FastAPI** application that handles user registration and authentication using JWT (JSON Web Tokens). The application provides secure sign-up and login features and is designed to be a starting point for integrating authentication into FastAPI-based systems.

## Features

- **User Sign-up**: New users can register using their email and password.
- **User Authentication**: Implemented using JWT for secure access tokens.
- **Password Hashing**: User passwords are stored securely with password hashing.
- **Database Integration**: Easily configurable with a database (e.g., SQLite, PostgreSQL) to store user data.
- **FastAPI**: A modern and fast (high-performance) Python web framework.
  
## Installation

### Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- JWT

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/abdorhl/FastApi_Singin_up.git
    cd FastApi_Singin_up
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables in a `.env` file (create one in the root directory):

    ```bash
    SECRET_KEY="your_secret_key"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5. Run the application:

    ```bash
    uvicorn main:app --reload
    ```

6. Access the API documentation:

    Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view and interact with the API.

## Usage

- **Sign-up**: Create a new user account by providing a valid email and password.
- **Login**: Obtain a JWT token by logging in with your credentials.
- **Access Secure Routes**: Pass the JWT token in the `Authorization` header to access secured routes.

## Project Structure

```bash
FastApi_Singin_up/
│
├── main.py                # Entry point for FastAPI app
├── jwt_token.py           # JWT token creation and verification logic
├── schema.py              # Pydantic models (schemas) for validation
├── database.py            # Database configuration and setup
├── .env                   # Environment variables (SECRET_KEY, etc.)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or want to add new features.

## License

This project is licensed under the MIT License.
