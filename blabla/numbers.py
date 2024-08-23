import logging

def uno():
    return 1

def dos():
    try:
        return 2
    except Exception:
        logging.exception("Beh!")

def tres():
    return 3