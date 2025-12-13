from app.metadata import get_all_datasets_metadata
from app.db import conn



data = get_all_datasets_metadata(conn)

print(data)
