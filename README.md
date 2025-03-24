# CLI Project

## Project Structure
``` 
R12725040_assignment01/
│── src/
│   ├── main.py               # Presentation layer
│   ├── input_handler.py      # Presentation layer
│   ├── services/             # Service layer
│   │   ├── user_service.py   # User
│   │   ├── listing_service.py # List
│   │   ├── category_service.py # Category
│   ├── persistence/          # Persistence layer
│   │   ├── db_handler.py     # database
│   ├── output_handler.py     # Presentation layer
│── build.sh
│── run.sh
│── README.md
│── db.json                   # TinyDB
``` 

## Environment
- Operating System: **macOS**
- Execution Environment: **Conda base environment**
- Language: **Python** (Python Version: **3.12**)
- Required Package: **tinydb** (Lightweight database)

## Build
```
./build.sh
```

## Run
```
./run.sh
```
