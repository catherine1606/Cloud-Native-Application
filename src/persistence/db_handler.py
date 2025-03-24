from tinydb import TinyDB, Query

DB_PATH = "db.json"

class DBHandler:
    db = TinyDB(DB_PATH)
    users_table = db.table("users")
    listings_table = db.table("listings")

    @classmethod
    def add_user(cls, username):
        """ 新增使用者 """
        if cls.users_table.contains(Query().username == username.lower()):
            return False  # 使用者已存在
        cls.users_table.insert({"username": username.lower()})
        return True

    @classmethod
    def get_users(cls):
        """ 取得所有使用者 """
        return {user["username"]: user for user in cls.users_table.all()}

    @classmethod
    def add_listing(cls, listing):
        """ 新增商品 """
        cls.listings_table.insert(listing)

    @classmethod
    def get_listings(cls):
        """ 取得所有商品 """
        return {l["listing_id"]: l for l in cls.listings_table.all()}

    @classmethod
    def delete_listing(cls, listing_id):
        """ 刪除商品 """
        return cls.listings_table.remove(Query().listing_id == listing_id)