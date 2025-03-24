from datetime import datetime
from src.persistence.db_handler import DBHandler

class ListingService:
    @staticmethod
    def create_listing(username, title, description, price, category):
        users = DBHandler.get_users()
        if username.lower() not in users:
            return "Error - unknown user"

        listings = DBHandler.get_listings()
        listing_id = str(100000 + len(listings) + 1)
        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_listing = {
            "listing_id": listing_id,
            "username": username,
            "title": title,
            "description": description,
            "price": price,
            "category": category,
            "creation_time": creation_time
        }
        DBHandler.add_listing(new_listing)
        return listing_id

    @staticmethod
    def delete_listing(username, listing_id):
        listings = DBHandler.get_listings()
        if listing_id not in listings:
            return "Error - listing does not exist"
        if listings[listing_id]["username"].lower() != username.lower():
            return "Error - listing owner mismatch"
        
        DBHandler.delete_listing(listing_id)
        return "Success"

    @staticmethod
    def get_listing(username, listing_id):
        users = DBHandler.get_users()
        if username.lower() not in users:
            return "Error - unknown user"
        
        listings = DBHandler.get_listings()
        if listing_id not in listings:
            return "Error - not found"
        
        l = listings[listing_id]
        return l
