import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings

USER = "root"
PASSWORD = "password"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "db_311"
TABLENAME = "table_311"

# create dataframe
austin311_df = pd.read_csv("311_Unified_Data_Test_Site_2019.csv")

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")

try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}.  Database {DATABASE} may already exist."
    )
    pass

engine.execute(f"USE {DATABASE}")
engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")
austin311_df.to_sql(name=TABLENAME, con=engine)

