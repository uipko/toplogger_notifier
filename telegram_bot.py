"""
Small wrapper class around python-telegram-bot
"""
from telegram.ext import CommandHandler
from telegram.ext import Updater


class TelegramBot:
    """
    Setup python-telegram-bot.

        Add handlers for the following commands:
        - status: Display time of last check
        - reset: Reset the QueueItem.handled property so all queued item wil be checked again.
    """

    def __init__(self, token):
        self.updater = Updater(token=token)
        dispatcher = self.updater.dispatcher

        # add handlers
        dispatcher.add_handler(CommandHandler('status', TelegramBot.status))
        dispatcher.add_handler(CommandHandler('reset', TelegramBot.reset))

        # GO
        self.updater.start_polling()

    def set_queue(self, queue):
        """
        Set queue in Dispatcher.bot_data
        """
        self.updater.dispatcher.bot_data['queue'] = queue

    def set_last_run(self, datetime):
        """
        Set last in Dispatcher.bot_data
        """
        self.updater.dispatcher.bot_data['last_run'] = datetime

    # Command handlers
    @staticmethod
    def status(update, context):
        """
        This command handler sends a messages with the current status.
        """
        msg = f"Last run: {context.bot_data['last_run'].strftime('%y-%m-%d %H:%M')}\n\n" \
              f"Searching for a slot in the following periods:\n"
        msg += '\n'.join(map(str, context.bot_data['queue']))
        context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

    @staticmethod
    def reset(update, context):
        """
        This command handler resets all queued items which are marked as handled. This handler
        also sends a messages when done.
        """
        for item in [item for item in context.bot_data['queue'] if item.handled]:
            item.set_handled(False)

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Looking for all queued periods again.")
