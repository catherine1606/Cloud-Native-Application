import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.input_handler import parse_command
from src.output_handler import OutputHandler
from src.services.user_service import UserService
from src.services.listing_service import ListingService
from src.services.category_service import CategoryService

def main():
    while True:
        try:
            command = input("# ").strip()
            if not command:
                continue

            cmd, args = parse_command(command)

            if cmd == "REGISTER":
                result = UserService.register(*args)
                if result == "Success":
                    OutputHandler.success(result)
                else:
                    OutputHandler.error(result)

            elif cmd == "CREATE_LISTING":
                result = ListingService.create_listing(*args)
                if isinstance(result, str) and result.startswith("Error"):
                    OutputHandler.error(result)
                else:
                    OutputHandler.success(result)

            elif cmd == "DELETE_LISTING":
                result = ListingService.delete_listing(*args)
                if isinstance(result, str) and result.startswith("Error"):
                    OutputHandler.error(result)
                else:
                    OutputHandler.success(result)

            elif cmd == "GET_LISTING":
                result = ListingService.get_listing(*args)
                if isinstance(result, str) and result.startswith("Error"):
                    OutputHandler.error(result)
                else:
                    print(OutputHandler.listing_details(result))

            elif cmd == "GET_CATEGORY":
                result = CategoryService.get_category(*args)
                if isinstance(result, str) and result.startswith("Error"):
                    OutputHandler.error(result)
                else:
                    print(OutputHandler.category_listings(result))

            elif cmd == "GET_TOP_CATEGORY":
                result = CategoryService.get_top_category(*args)
                if isinstance(result, str) and result.startswith("Error"):
                    OutputHandler.error(result)
                else:
                    OutputHandler.success(result)

        except EOFError:
            break

if __name__ == "__main__":
    main()