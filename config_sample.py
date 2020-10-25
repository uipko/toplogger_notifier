"""
All settings for this TopLogger script.

Copy this file to config.py and make sure not to add config.py to git.
"""
# from models import Period
# from models import QueueItem

# TOP_LOGGER
USER = '<CHANGE_ME>'
PASSWORD = '<CHANGE_ME>'

# TELEGRAM
TOKEN = '<CHANGE_ME>'
CHAT_ID = '<CHANGE_ME>'

# SCRIPT SETTINGS
# do not send Telegram message
DEBUG = False
# Time in seconds between to checks, minimal=30, -1 => do not repeat
INTERVAL = 60 * 60
GYMS = {
    # Add here your gym, EG:
    # 'delfts_bleau': {'id': 38, 'area_id': 31},
}
QUEUE = [
    # Add here your periods of interest, EG:
    # QueueItem(GYMS['delfts_bleau'], Period('2020-10-16 11:30', '2020-10-16 14:30')),
]
