import logging
from typing import Optional, TypeVar, Type
from django.conf import settings
import requests
from pydantic import ValidationError, BaseModel

from bot.tg.schemas import GetUpdateResponse, SendMessageResponse


logger = logging.getLogger(__name__)

T = TypeVar('T', bound=BaseModel)


class TgClientError(Exception):
    ...


class TgClient:
    def __init__(self, token: Optional[str] = None):
        self.__token = token if token else settings.BOT_TOKEN
        self.__url = f'https://api.telegram.org/bot{self.__token}/'

    def __get_url(self, method: str) -> str:
        return f'{self.__url}{method}'


    def get_updates(self, offset: int = 0, timeout: int = 60, **kwargs) -> GetUpdateResponse:
        data = self._get('getUpdates', offset=offset, timeout=timeout, **kwargs)
        return self.__serializer_tg_response(GetUpdateResponse, data)

    def send_message(self, chat_id: int, text: str, **kwargs) -> SendMessageResponse:
        data = self._get('sendMessage', chat_id=chat_id, text=text, **kwargs)
        return self.__serializer_tg_response(SendMessageResponse, data)

    def _get(self, method: str, **params) -> dict:
        url = self.__get_url(method)
        params.setdefault('timeout', 10)
        response = requests.get(url, params=params)
        if not response.ok:
            logger.warning('Invalid status code %d from command %s', response.status_code, method)
            raise TgClientError
        return response.json()


    @staticmethod
    def __serializer_tg_response(serializer_class: Type[T], data: dict) -> T:
        try:
            return serializer_class(**data)
        except ValidationError:
            logger.error('Failed to serializer telegram response: %s', data)
            raise TgClientError

