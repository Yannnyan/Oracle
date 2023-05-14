import pandas as pd

data_file = "Book1.xlsx"

columns_user = ["ID", "Email", "University", "Role"]
columns_events = ["User_ID", "Event_ID", "Description"]

db = pd.read_excel(data_file, columns_user)
print(db)
