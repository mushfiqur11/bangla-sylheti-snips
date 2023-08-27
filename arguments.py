def read_env():
    import os
    from dotenv import load_dotenv
    load_dotenv()
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
    return MONGO_USERNAME, MONGO_PASSWORD

def get_args():
    import argparse
    parser = argparse.ArgumentParser()
    username, password = read_env()
    parser.add_argument('--mongo_username', type=str, default=username)
    parser.add_argument('--mongo_password', type=str, default=password)
    parser.add_argument('--db_name', type=str, default='NLU')
    parser.add_argument('--collection_name', type=str, default='data_gen')
    args = parser.parse_args()
    return args