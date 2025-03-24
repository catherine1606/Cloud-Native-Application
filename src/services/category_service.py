from src.persistence.db_handler import DBHandler

class CategoryService:
    @staticmethod
    def get_category(username, category):
        users = DBHandler.get_users()
        if username.lower() not in users:
            return "Error - unknown user"

        listings = DBHandler.get_listings()
        category_listings = [
            l for l in listings.values() if l["category"].lower() == category.lower()
        ]
        if not category_listings:
            return "Error - category not found"

        category_listings.sort(key=lambda x: x["creation_time"], reverse=True)
        return category_listings

    @staticmethod
    def get_top_category(username):
        users = DBHandler.get_users()
        if username.lower() not in users:
            return "Error - unknown user"

        listings = DBHandler.get_listings()
        category_count = {}
        for l in listings.values():
            category = l["category"]
            category_count[category] = category_count.get(category, 0) + 1

        if not category_count:
            return ""

        max_count = max(category_count.values())

        top_categories = sorted([
            category for category, count in category_count.items()
            if count == max_count
        ])

        return "\n".join(top_categories)
