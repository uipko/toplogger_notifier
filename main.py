"""This script can be used to notify you when a slot comes available at your favorite gym.
Update the settings in config.py.
"""
from datetime import datetime
from datetime import timedelta
import logging
import time
from typing import Dict
from typing import List

from dateutil.tz import gettz

from models import QueueItem
from models import Slot
from telegram_bot import TelegramBot

try:
    import config
except ImportError:
    import config_sample as config
from toplogger import TopLogger


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def notify(telegram: TelegramBot, item: QueueItem, slots: List[Slot]):
    """Send Telegram notification for available slots."""
    if not slots:
        return

    message = f"Slot(s) available at {item.gym['name']} on {slots[0].date.strftime('%A %d %B')}"
    for slot in slots:
        message += f"\n -> {slot.start_at.strftime('%H:%M')} - {slot.end_at.strftime('%H:%M')}"
    if config.DEBUG:
        print(f"DEBUG: message\n\t{message}")
    else:
        # TODO: get config.CHAT_ID from telegram-bot
        telegram.updater.bot.send_message(chat_id=config.CHAT_ID, text=message)


def check(top_logger: TopLogger, telegram: TelegramBot, queue: Dict[str, QueueItem]) -> int:
    """Check for available slot(s) based on given items in queue."""
    now = datetime.now(gettz())
    # register last_run for command /status message
    telegram.set_last_run(now)

    # TODO: add proper logging
    print(f"{now}  --  START: check for {len(queue)} slots")
    available = 0
    for item in queue:
        # TODO: find out if the 10 days check is DB only
        if now < item.period.start <= (now + timedelta(10)) and not item.handled:
            top_logger.gym = item.gym
            available_slots = top_logger.available_slots(item.period)
            if available_slots:
                notify(telegram, item, available_slots)
                item.set_handled(True)
                available += len(available_slots)

    # TODO: add proper logging
    print(f"{datetime.now()}  --  FINISH: found {available} new slots")

    return available


def repeat(top_logger: TopLogger, telegram: TelegramBot, queue: List[QueueItem], interval: int):
    """Run check each INTERVAL seconds."""
    check(top_logger, telegram, queue)

    if interval != -1:
        minimal_interval = 1 if config.DEBUG else 30
        interval = max(minimal_interval, interval)
        time.sleep(interval)
        repeat(top_logger, telegram, queue, interval)


def main():
    """
    Start Top Logger notifier.
    Make sure you've set all necessary settings in config.py
    """
    top_logger = TopLogger()
    queue = config.QUEUE
    # setup telegram
    telegram_bot = TelegramBot(config.TOKEN)
    telegram_bot.set_queue(queue)

    # start schedule
    repeat(top_logger, telegram_bot, queue, config.INTERVAL)


if __name__ == '__main__':
    main()
