

.. image:: https://github.com/uipko/toplogger_notifier/workflows/Pylint/badge.svg?branch=main
   :target: https://github.com/uipko/toplogger_notifier/
   :alt: Pylint

.. image:: https://api.codacy.com/project/badge/Grade/b737729d31d440f0af5a5f1e115da148
   :alt: Codacy Badge
   :target: https://app.codacy.com/gh/uipko/toplogger_notifier?utm_source=github.com&utm_medium=referral&utm_content=uipko/toplogger_notifier&utm_campaign=Badge_Grade

Table of contents
=================

- `Introduction`_

- `Prerequisites`_
    - `TopLogger account`_
    - `Telegram account & bot`_

- `Installing`_
    - `Setup environment`_
    - `Configure script`_

- `Usage`_
    - `Run TopLogger notifier`_
    - `Telegram bot commands`_

- `Contributing`_
    - `Updating dependencies`_

- `Possible new features`_


Introduction
============
Because of the COVID measures (in the Netherlands) reservations are obliged for a lot of activities,
in this case sport climbing/bouldering. The number of slots are very limited (30 at the moment of
writing). Some gyms are pretty popular and crowded. Hence, reservations are depleted pretty
quickly.

A lot of bouldering gyms (in the Netherlands) are using the TopLogger service to arrange the
reservations. Manually keeping track of slots coming available is a daunting task. This script
can be used to notify you when a slot comes available at your favorite gym(s).

At the moment this script does not has persistent storage. Keeping track of sent notifications will
only be done in memory. Adding persistent storage is one of the planned features, but nobody knows
if and when this will feature will be implemented.


Prerequisites
=============
The following accounts are needed for this script to work.

TopLogger account
-----------------
First of all you need a TopLogger account so we can keep rack of available slots at your favorite
gym. Considering you're looking at this script you probably already have an account. If not go to
https://toplogger.nu to create an account. Credentials of your account need to be added to
:code:`config.py`.

Telegram account & bot
----------------------
To notify you about available slots the script uses Telegram. For this to work you need to have a
Telegram account and create a Telegram bot. Create a group and add your bot to ths group.

For all of this to work you need to copy API token and chat_id (see:
https://api.telegram.org/bot<TOKEN>/getUpdates ) to :code:`config.py`.


Installing
==========
No fancy packaging (yet). So if you want to use this script just clone the repo and run it.

Go to an appropriate folder and clone this repository.

.. code-block:: bash

    $ git clone git@github.com:uipko/toplogger_notifier.git

Setup environment
-----------------
Setup an virtual environment and install the dependencies.

.. code-block:: bash

    $ python -m venv .venv && . .venv/bin/activate
    $ pip install -r requirements.txt

Configure script
----------------
Copy :code:`config_sample.py` to :code:`config.py` and update all settings.

*NB: Make sure not to add config.py to git because it contains your secrets.*

Usage
=====

Run TopLogger notifier
----------------------
Start script and save 'logging' to file.

.. code-block:: bash

    $ python -u ./main.py | tee `date -Iseconds`.log

Telegram bot commands
---------------------
The TopLogger Notifier telegram bot provides the following commands:

- status: Show last run & queued periods
- reset: Reset notified periods so we will notified again if there's a available slot.

Contributing
============
If you're missing something and have some copious-free-time to to spare, feel free to create a
pull request.

Updating dependencies
---------------------
After installing a new dependency run the following to update requirements.txt.

(See how it works out when we do not pin versions for the required dependencies.)

.. code-block:: bash

    $ pip-chill --no-version > requirements.txt

Possible new features
=====================
The following features could be implemented someday or not. Hopefully this COVID situation will
nog give me enough time to implement all these features.The order of this list is not necessarily
the order of implementation.

Idea's for new features:

- Add logging
- Setup pytest and unit tests for existing code
- Persist data between runs
- Add data of gyms
- Add packaging
- Add feature to make it possible to CRUD desired slots
- Add automagically booking of available slot
