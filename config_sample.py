"""
All settings for this TopLogger script.

Copy this file to config.py and make sure not to add config.py (including your secrets) to git.
"""
# from models import Period
# from models import QueueItem

# TELEGRAM
TOKEN = ''
CHAT_ID = ''

# SCRIPT SETTINGS
# do not send Telegram message
DEBUG = False
# Time in seconds between to checks, minimal=30, -1 => do not repeat
INTERVAL = 60 * 60
GYMS = {
    # Add here your gym, EG:
    # The list of gyms can be found here:
    # https://api.toplogger.nu/v1/gyms
    # Find your favorite gym and check for reservation_areas. If there are reservation areas fill
    # in the id, if not remove area_id.
    # 'be_boulder_amsterdam': {'id': 100, 'area_id': 65},
}
QUEUE = [
    # Add here your periods of interest, EG:
    # QueueItem(GYMS['be_boulder_amsterdam'], Period('2020-10-16 11:30', '2020-10-16 14:30')),
]
