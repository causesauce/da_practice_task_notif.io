from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, constr, PositiveInt, validator
from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator

ZERO_MESSAGE_COUNTER = 0


class MessageInput(BaseModel):
    body: Optional[str]


class MessageInputValidated(BaseModel):
    body: str

    @validator('body', pre=True)
    def validate_body(cls, body):
        if body is None or len(body) > 160 or len(body) < 1:
            raise HTTPException(status_code=400, detail="body should not be empty")
        else:
            return body


class MessageResponse(BaseModel):
    body: Optional[constr(min_length=1, max_length=160)]
    counter: PositiveInt


class Message(Model):
    id_message = fields.IntField(pk=True)
    body = fields.CharField(160)
    counter = fields.IntField(pk=False)

    def __str__(self):
        return self.id_message

    async def increase_counter(self):
        self.counter += 1
        await self.save()

    async def reset_counter(self):
        self.counter = 0
        await self.save()


Message_Pydantic = pydantic_model_creator(Message, name="MessageOut", exclude=('id_message',))

Message_Pydantic_With_Id = pydantic_model_creator(Message, name="MessageOutWithIds")


async def delete_message(id_message: int):
    message = await Message.get(id_message=id_message)
    await message.delete()


async def add_message(message_input: MessageInput):
    message_input_model = MessageInputValidated.parse_obj(dict(body=message_input.body))
    message_obj = Message(body=message_input_model.body, counter=ZERO_MESSAGE_COUNTER)
    await message_obj.save()
    return message_obj


async def update_message(message_input: MessageInput, id_message: int):
    message_input_model = MessageInputValidated.parse_obj(dict(body=message_input.body))
    message = await Message.get(id_message=id_message)
    message.body = message_input_model.body
    message.counter = ZERO_MESSAGE_COUNTER
    await message.save()
    message = await Message_Pydantic.from_tortoise_orm(message)
    return message


async def get_all():
    messages = await Message.all()
    response = list()
    for message in messages:
        await message.increase_counter()
        response.append(await Message_Pydantic.from_tortoise_orm(message))
    return response


async def get_all_with_ids():
    messages = await Message.all()
    response = list()
    for message in messages:
        await message.increase_counter()
        response.append(await Message_Pydantic_With_Id.from_tortoise_orm(message))
    return response


async def get_by_id(id_message: int):
    message = await Message.get(id_message=id_message)
    await message.increase_counter()
    response = await Message_Pydantic.from_tortoise_orm(message)
    return response
