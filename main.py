from arguments import get_args
from utils import get_db, get_all_documents, convert_to_bio_format_bengali

if __name__ == '__main__':
    args = get_args()
    
    db = get_db(args.mongo_username, args.mongo_password, args.db_name)
    collection = db[args.collection_name]

    documents = get_all_documents(collection)

    data = {'text':documents[0]['InformalBangla'], 'slots':documents[0]['InformalBangla_Slots']}
    # data = {'text': 'আমি আমার বয়ফ্রেন্ডের সাথে আমার অবস্থান শেয়ার করতে চাই', 'slots': {'contact': 'আমার বয়ফ্রেন্ড', 'sharingDuration': ''}}

    print(convert_to_bio_format_bengali(data))

