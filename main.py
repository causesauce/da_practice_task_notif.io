from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from pydantic import PositiveInt
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_204_NO_CONTENT, \
    HTTP_400_BAD_REQUEST, HTTP_200_OK
from tortoise.contrib.fastapi import register_tortoise

from models import MessageInputValidated, Message, Message_Pydantic, MessageInput, get_all, get_by_id, add_message, \
    update_message, delete_message

app = FastAPI()


API_KEY = "ed049313-16eb-4fc1-aa36-398d21255f76"
API_KEY_NAME = "access_token"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
        api_key_query: str = Security(api_key_query),
        api_key_header: str = Security(api_key_header)
):
    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Wrong credentials"
        )


@app.get("/messages", status_code=HTTP_200_OK)
async def get_messages():
    response_list = await get_all()
    return response_list


@app.get("/messages/{id_message}", status_code=HTTP_200_OK)
async def get_messages_by_id(id_message: PositiveInt):
    response = await get_by_id(id_message)
    return response


@app.post("/messages", status_code=HTTP_201_CREATED)
async def post_message_endpoint(message_input: MessageInput = None, api_key: APIKey = Depends(get_api_key)):
    if message_input is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="body should not be empty")
    message_obj = await add_message(message_input)
    return f'message with id {message_obj.id_message} has been created'


@app.put("/messages/{id_message}")
async def update_message_endpoint(
        id_message: PositiveInt,
        message_input: MessageInput = None,
        api_key: APIKey = Depends(get_api_key)
):
    if message_input is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="body should not be empty")
    message = await update_message(message_input, id_message)
    return {"detail": f"message with the id {id_message} has been modified",
            "message": message}


@app.delete("/messages/{id_message}", status_code=200)
async def delete_message_endpoint(id_message: PositiveInt, api_key: APIKey = Depends(get_api_key)):
    await delete_message(id_message)
    return {"details": "success"}


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)
