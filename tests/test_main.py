import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from main import handle_command

def test_register():
    assert handle_command("REGISTER user1") == "Success"
    assert handle_command("REGISTER user2") == "Success"
    assert handle_command("REGISTER user2") == "Error - user already existing"

def test_create_and_get_listing():
    assert handle_command("CREATE_LISTING user1 'Phone model 8' 'Black color, brand new' 1000 'Electronics'") == "100001"
    assert handle_command("CREATE_LISTING user1 'Black shoes' 'Training shoes' 100 'Sports'") == "100002"

    listing = handle_command("GET_LISTING user1 100001")
    assert listing.startswith("Phone model 8|Black color, brand new|1000|")
    assert "Electronics|user1" in listing

def test_user2_listing_and_get():
    assert handle_command("CREATE_LISTING user2 'T-shirt' 'White color' 20 'Sports'") == "100003"

    listing = handle_command("GET_LISTING user1 100003")
    assert listing.startswith("T-shirt|White color|20|")
    assert "Sports|user2" in listing