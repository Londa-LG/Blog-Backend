#  Blog API

A blog API with CRUD functionality.

## Requirements
- python develoment environment
- fastapi
- pydantic-settings

## Installing 

### With the requirements.tx file

```
pip install -r requirements.txt
```

### Manually

Install fastapi 

```
pip install fastapi[all]
```

Install pydantic-settings.This is used for handling environment variables.

```
pip install pydantic-settings
```

## Configuration

Before running the application you'll need to create a .env file for your envirnoment variables.

Here's an example of doing from the terminal

```
touch .env
```

Next we need to assign our environment vairables.So type the following in the .env file

```
SECRET_KEY="GenerateStrings"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
SQLALCHEMY_DATABASE_URL="sqlite:///Test.db"
```

- SECRET_KEY: The key string for JWT encoding.You can generate your own should you wish.
- ALGORITHM: The algorithm used to encode the JWT Bearer token.
- ACCESS_TOKEN_EXPIRE_MINUTES: How long it takes for the token to expire.
- SQLALCHEMY_DATABASE_URL: Link to your database.

## Running

Once you've install all the required packages and created the .env file run the following command to start the development server.

```
uvicoron main:app --reload
```

Send all requests to [localhost:8000/](http://127.0.0.1:8000)

## Functionality

You can view simple endpoint documentation directly from the application by visiting: [localhost:8000/docs](http://127.0.0.1:8000/docs)
