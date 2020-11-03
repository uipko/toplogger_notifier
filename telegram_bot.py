"""Small wrapper class around python-telegram-bot."""
from datetime import datetime
from typing import Dict

from dateutil.tz import gettz
from telegram.ext import CommandHandler
from telegram.ext import Updater

from models import QueueItem


class TelegramBot:

    """
    Setup python-telegram-bot.
        Add handlers for the following commands:
        - status: Display time of last check
        - reset: Reset the QueueItem.handled property so all queued item wil be checked again.
    """
    def __init__(self, token: str):
        # TODO: check if there's already an updater running or handle exception
        self.updater = Updater(token=token)
        dispatcher = self.updater.dispatcher

        # add handlers
        dispatcher.add_handler(CommandHandler('status', TelegramBot.status))
        dispatcher.add_handler(CommandHandler('reset', TelegramBot.reset))

        # GO
        self.updater.start_polling()

    def set_queue(self, queue: Dict[str, QueueItem]):
        """Set queue in Dispatcher.bot_data."""
        self.updater.dispatcher.bot_data['queue'] = queue

    def set_last_run(self, last_run: datetime):
        """Set last in Dispatcher.bot_data."""
        self.updater.dispatcher.bot_data['last_run'] = last_run

    # Command handlers
    @staticmethod
    def status(update, context):
        """Command handler to sends a messages with the current status."""
        last_run = context.bot_data['last_run']
        delta_minutes, _ = divmod((datetime.now(gettz()) - last_run).seconds, 60)
        msg = f"Last run: {delta_minutes} minutes " \
              f"ago on {last_run.strftime('%y-%m-%d %H:%M')}\n\n" \
              f"Searching for a slot in the following periods:\n"
        msg += '\n'.join(map(str, context.bot_data['queue']))
        context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

    @staticmethod
    def reset(update, context):
        """
        Command handler to resets all queued items which are marked as handled.
        This command handler also sends a messages when done.
        """
        for item in context.bot_data['queue']:
            item.set_handled(False)

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Looking for all queued periods again.")
