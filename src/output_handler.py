class OutputHandler:
    @staticmethod
    def success(message):
        """ 輸出成功訊息 """
        print(message, end="\n\n")

    @staticmethod
    def error(message):
        """ 統一錯誤訊息輸出 """
        print(message, end="\n\n")

    @staticmethod
    def listing_details(listing):
        """ 格式化商品資訊輸出 """
        return f"{listing['title']}|{listing['description']}|{listing['price']}|{listing['creation_time']}|{listing['category']}|{listing['username']}"

    @staticmethod
    def category_listings(listings):
        """ 以換行方式輸出所有分類商品 """
        return "\n".join(OutputHandler.listing_details(l) for l in listings)
