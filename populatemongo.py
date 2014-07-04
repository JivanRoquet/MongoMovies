from pymongo import MongoClient


def get_mongo_db(host, port, username, password, db):
    """ Returns a connection to a MongoDB database """
    if not host and not port:
        mg = MongoClient()
    elif host and port and not username and not password:
        mg = MongoClient(host, port)
    else:
        uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        mg = MongoClient(uri)

    return mg[db]


def get_columns(filename):
    sequences = {
        'u.user': ['user_id', 'gender', 'age', 'occupation', 'zip_code'],
        'u.data': ['user_id', 'item_id', 'rating', 'timestamp'],
        'u.item': ['item_id', 'title', 'release_date', 'video_release_date', 'imdb_url',
                   'unknown',
                   'action',
                   'aventure',
                   'animation',
                   'children',
                   'comedy',
                   'crime',
                   'documentary',
                   'drama',
                   'fantasy',
                   'noir',
                   'horror',
                   'musical',
                   'mystery',
                   'romance',
                   'scifi',
                   'thriller',
                   'war',
                   'western']
    }

    return sequences[filename]
