# TopLogger Notifier
This script can be used to notify you when a slot comes available at your favorite gym.

# Usage
Copy config_sample.py to config.py and update all settings. Make sure not to add config.py to git
because it contains your secrets.

Start script.
```bash
$ ./main.py
```


# Dependencies

## Installing dependencies
Setup an virtual environment and run the following.

```
$ pip install -r requirements.txt
```

## Updating dependencies
After installing a new dependency run the following to update requirements.txt.

(See how it works out when we do not pin versions for the required dependencies.)

```bash
$ pip-chill --no-version > requirements.txt
```

# Planned features
The following features could be implemented someday or not. The order of this list is not necessarely the order of implementation.

TODO's:
- [ ] Add logging
- [ ] Add unit tests
- [ ] Persist data between runs
- [ ] Add data of gyms
- [ ] Add feature to make it possible to CRUD desired slots
