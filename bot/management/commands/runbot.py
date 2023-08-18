# import logging
# import secrets
#
# from django.core.management import BaseCommand, CommandError
# from django.conf import settings
# import json
#
# from bot.models import TgUser
# from bot.tg.bot_logic import get_user_goals, show_categories
# from bot.tg.client import TgClient
# from bot.tg.schemas import GetUpdateResponse, SendMessageResponse, Message
#
#
# # logger = logging.getLogger(__name__)
#
#
# class Command(BaseCommand):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.tg_client = TgClient()
#         self.users_data = {}
#
#
#     # def handle(self, *args, **options):
#     #     offset = 0
#     #     self.stdout.write(self.style.SUCCESS('Bot started...'))
#     #     while True:
#     #         res = self.tg_client.get_updates(offset=offset, allowed_updates='message')
#     #         for item in res.result:
#     #             offset = item.update_id + 1
#     #             self.handle_message(item.message)
#     def add_arguments(self, parser):
#         parser.add_argument('runbot', nargs='?', default='runbot')
#     def handle(self, *args, **options):
#         if options['runbot']:
#             offset = 0
#             try:
#                 while True:
#                     res = self.tg_client.get_updates(offset=offset)
#
#                     for item in res.result:
#                         offset = item.update_id + 1
#                         self.handle_message(item.message)
#             except Exception as e:
#                 raise CommandError(f'An error occurred: {e}')
#     #
#     #
#     # def handle_message(self, msg: Message):
#     #     tg_user, _ = TgUser.objects.get_or_create(chat_id=msg.chat.id, defaults={'username': msg.chat.username})
#     #     # self.tg_client.send_message(chat_id=msg.chat.id, text=msg.text)
#     #     if not tg_user.is_verified:
#     #         tg_user.update_verification_code()
#     #         self.tg_client.send_message(msg.chat.id, f'Verification code: {tg_user.verification_code}')
#     #
#     #     else:
#     #         self.handle_message(tg_user, msg)
#     #
#     # def handel_auth_user(self, tg_user: TgUser, msg: Message):
#     #     if msg.text.startswith('/'):
#     #         if msg.text == '/goals':
#     #             ...
#     #         elif msg.text == '/create':
#     #             ...
#     #         elif msg.text == '/cancel':
#     #             ...
#
#
#
#
#         # self.tg_client.send_message(msg.chat.id, f'You already verified')
#     # def handle_auth_user(self, tg_user: TgUser, message: Message) -> None:
#     #     """
#     #     Handle messages written by the user in the Bot's chat.
#     #
#     #     Args:
#     #         tg_user (TgUser): The Telegram user object.
#     #         message (Message): Message object with chat_id and message text.
#     #     """
#     #     if message.text.startswith('/'):  # check if message is command
#     #         match message.text:
#     #             case '/goals':
#     #                 text = get_user_goals(tg_user.user.id)
#     #             case '/create':
#     #                 text = show_categories(user_id=tg_user.user.id, chat_id=message.chat.id, users_data=self.users_data)
#     #             case '/cancel':
#     #                 if self.users_data[message.chat.id]:
#     #                     del self.users_data[message.chat.id]
#     #                 text = 'Creation cancelled'
#     #             case _:
#     #                 text = 'Unknown command'
#     #     elif message.chat.id in self.users_data:
#     #         next_handler = self.users_data[message.chat.id].get('next_handler')
#     #         text = next_handler(
#     #             user_id=tg_user.user.id, chat_id=message.chat.id, message=message.text, users_data=self.users_data
#     #         )
#     #     else:
#     #         text = 'List of commands:\n/goals - Show your goals\n' '/create - Create a goal\n/cancel - Cancel to create'
#     #     self.client.send_message(chat_id=message.chat.id, text=text)
#
#     def handle_message(self, message: Message) -> None:
#         """
#         Handle messages written by the user in the Bot's chat.
#
#         Args:
#             message (Message): Message object with chat_id and message text.
#         """
#         chat_id = message.chat.id
#         tg_user, _ = TgUser.objects.get_or_create(chat_id=chat_id, defaults={'username': message.chat.username})
#
#         if not tg_user.is_verified:
#             token = secrets.token_urlsafe()[:16]
#             tg_user.verification_code = token  # Set the new verification code
#             tg_user.save()
#             message = f"Hello!\nIt seems you need to link your account.\nHere's the verification code: {token}"
#             self.tg_client.send_message(chat_id=chat_id, text=message)
#         else:
#             self.handle_auth_user(tg_user=tg_user, message=message)
#
#     def handle_auth_user(self, tg_user: TgUser, message: Message) -> None:
#         """
#         Handle messages written by the user in the Bot's chat.
#
#         Args:
#             tg_user (TgUser): The Telegram user object.
#             message (Message): Message object with chat_id and message text.
#         """
#         if message.text.startswith('/'):  # check if message is command
#             if message.text == '/goals':
#                 text = get_user_goals(tg_user.user.id)
#             elif message.text == '/create':
#                 text = show_categories(user_id=tg_user.user.id, chat_id=message.chat.id, users_data=self.users_data)
#             elif message.text == '/create':
#                 if self.users_data[message.chat.id]:
#                     del self.users_data[message.chat.id]
#                 text = 'Creation cancelled'
#
#         elif message.chat.id in self.users_data:
#             next_handler = self.users_data[message.chat.id].get('next_handler')
#             text = next_handler(
#                 user_id=tg_user.user.id, chat_id=message.chat.id, message=message.text, users_data=self.users_data
#             )
#         else:
#             text = 'List of commands:\n/goals - Show your goals\n' '/create - Create a goal\n/cancel - Cancel to create'
#         self.tg_client.send_message(chat_id=message.chat.id, text=text)
from typing import Optional

from django.core.management import BaseCommand


from bot.models import TgUser
from bot.tg.client import TgClient
from bot.tg.schemas import Message
from goals.models import Goal, GoalCategory


class Command(BaseCommand):

    help = "run bot"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient()
        self.users_data = {}

    def handle(self, *args, **options):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                self.handle_message(item.message)

    def handle_message(self, msg: Message):
        tg_user, created = TgUser.objects.get_or_create(chat_id=msg.chat.id)

        if tg_user.user:
            self.handle_authorized_user(tg_user, msg)
        else:
            self.handle_unauthorized_user(tg_user, msg)

    def handle_authorized_user(self, tg_user: TgUser, msg: Message):
        commands: list = ['/goals', '/create', '/cancel']
        create_chat: Optional[dict] = self.users_data.get(msg.chat.id, None)
        self.tg_client.send_message(
            chat_id=msg.chat.id,
            text=f'Доступные команды:\n/goals\n/create\n/cancel '
        )

        if msg.text == '/cancel':
            self.users_data.pop(msg.chat.id, None)
            create_chat = None
            self.tg_client.send_message(chat_id=msg.chat.id, text='Операция отменена')

        if msg.text in commands and not create_chat:
            if msg.text == '/goals':
                qs = Goal.objects.filter(
                    category__is_deleted=False, category__board__participants__user_id=tg_user.user.id
                ).exclude(status=Goal.Status.archived)
                goals = [f'{goal.id} - {goal.title}' for goal in qs]
                self.tg_client.send_message(chat_id=msg.chat.id, text='Нет целей' if not goals else '\n'.join(goals))

            if msg.text == '/create':
                categories_qs = GoalCategory.objects.filter(
                    board__participants__user_id=tg_user.user.id, is_deleted=False
                )

                categories = []
                categories_id = []
                for category in categories_qs:
                    categories.append(f'{category.id} - {category.title}')
                    categories_id.append(str(category.id))

                self.tg_client.send_message(
                    chat_id=msg.chat.id, text=f'Выберите номер категории:\n' + '\n'.join(categories)
                )
                self.users_data[msg.chat.id] = {
                    'categories': categories,
                    'categories_id': categories_id,
                    'category_id': '',
                    'goal_title': '',
                    'stage': 1,
                }
                if msg.text not in commands and create_chat:
                    if create_chat['stage'] == 2:
                        Goal.objects.create(
                            user_id=tg_user.user.id,
                            category_id=int(self.users_data[msg.chat.id]['category_id']),
                            title=msg.text,
                        )
                        self.tg_client.send_message(chat_id=msg.chat.id, text='Цель сохранена')
                        self.users_data.pop(msg.chat.id, None)

                    elif create_chat['stage'] == 1:
                        if msg.text == '/cancel':
                            self.users_data.pop(msg.chat.id, None)
                            create_chat = None
                            self.tg_client.send_message(chat_id=msg.chat.id, text='Операция отменена')

                        if msg.text in create_chat.get('categories_id', []):
                            self.tg_client.send_message(chat_id=msg.chat.id, text='Введите название цели')
                            self.users_data[msg.chat.id] = {'category_id': msg.text, 'stage': 2}
                        else:
                            self.tg_client.send_message(
                                chat_id=msg.chat.id,
                                text='Введен неправильный номер категории\n' + '\n'.join(
                                    create_chat.get('категории', [])),
                            )
        if msg.text not in commands and not create_chat:
            self.tg_client.send_message(chat_id=msg.chat.id, text=f'Неизвестная команда')

    def handle_unauthorized_user(self, tg_user: TgUser, msg: Message):
        code = tg_user.generate_verification_code()
        tg_user.verification_code = code
        tg_user.save()

        self.tg_client.send_message(chat_id=msg.chat.id, text=f'Ваш код верификации: {code}')
