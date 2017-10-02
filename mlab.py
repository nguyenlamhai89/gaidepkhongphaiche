import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds151024.mlab.com:51024/nlhai89
host = "ds151024.mlab.com"
port = 51024
db_name = "nlhai89"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
