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

# Add here your favorite gyms.
# The list of gyms can be found here:
# https://api.toplogger.nu/v1/gyms
# Find your favorite gym and check for reservation_areas here.
# https://api.toplogger.nu/v1/gyms/<YOUR GYM ID>/reservation_areas
GYMS = {
    # 'be_amsterdam': {'id': 100, 'area_id': 65, 'name': 'Be Boulder Amsterdam'},
}

# Add here your periods of interest for a gym from the GYMS dictionary. All available slots which
# start and end in this period will be notified.
QUEUE = [
    # QueueItem(GYMS['be_amsterdam'], Period.from_strings('2020-10-16 11:30', '2020-10-16 14:30')),
]
