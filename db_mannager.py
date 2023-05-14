import pandas as pd

files = {
    'events': './data_base/events.xlsx',
    'users': './data_base/users.xlsx',
    'users_events': './data_base/users_events.xlsx'
}


event_att = ['id', 'name', 'info', 'location']
user_att = ['id', 'fname', 'lname', 'email']


def keys_generator():
    k = 0
    while True:
        k += 1
        yield k


def add_event(event, users):
    new_event = {k: event[k] for k in event_att}
    df = pd.read_excel(files['events'])


def remove_event():
    pass


def update_event():
    pass


def add_user():
    pass


def remove_user():
    pass


def update_user():
    pass
