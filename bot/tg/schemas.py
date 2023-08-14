# from typing import Optional
#
# from pydantic import BaseModel
#
#
# class Chat(BaseModel):
#     id: int
#     username: Optional[str] = None
#
#
# class Message(BaseModel):
#     message_id: int
#     chat: Chat
#     test: str
#
#
# class UpdateObj(BaseModel):
#     update_id: int
#     message: Message
#
#
# class GetUpdateResponse(BaseModel):
#     ok: bool
#     result: list[UpdateObj] = []
#
#
# class SendMessageResponse(BaseModel):
#     ok: bool
#     result: Message
from typing import Optional

from pydantic.main import BaseModel


class Chat(BaseModel):
    id: int
    username: Optional[str] = None


class Message(BaseModel):
    message_id: int
    chat: Chat
    text: str


class UpdateObj(BaseModel):
    update_id: int
    message: Message


class GetUpdateResponse(BaseModel):
    ok: bool
    result: list[UpdateObj] = []


class SendMessageResponse(BaseModel):
    ok: bool
    result: Message
