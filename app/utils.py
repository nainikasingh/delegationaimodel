import pandas as pd

USERS_CSV_PATH = "delegation.users.csv"
TASKS_CSV_PATH = "delegation.tasks1.csv"

def load_user_role(user_id):
    df = pd.read_csv(USERS_CSV_PATH)
    user_row = df[df["_id"] == user_id]
    if not user_row.empty:
        return user_row.iloc[0]["role"]
    return None

def load_user_name(user_id):
    df = pd.read_csv(USERS_CSV_PATH)
    user_row = df[df["_id"] == user_id]
    if not user_row.empty:
        return user_row.iloc[0]["username"]
    return None
