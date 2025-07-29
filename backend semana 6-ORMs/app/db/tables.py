from sqlalchemy import Table, Column, Integer, String, BigInteger, SmallInteger, DateTime, func, ForeignKey
from db.connection import engine, metadata_obj

users_table = Table(
  "users",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("full_name", String(100), nullable=False),
  Column("email", String(100), nullable=False, unique=True),
  Column("phone_number", BigInteger, nullable=False, unique=True),
  Column("created_date", DateTime, server_default=func.now())
)

address_table = Table(
  "addresses",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("street", String(25), nullable=False),
  Column("city", String(25), nullable=False),
  Column("province", String(25), nullable=False),
  Column("zip_code", String(20), nullable=False),
  Column("country", String(20), nullable=False),
  Column("user_id", ForeignKey("users.id"), nullable=False),
  Column("created_date", DateTime, server_default=func.now())
)

cars_table = Table(
  "cars",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("make", String(25), nullable=False),
  Column("model", String(25), nullable=False),
  Column("year_of_manufacture", SmallInteger, nullable=False),
  Column("user_id", ForeignKey("users.id"), nullable=True),
  Column("created_date", DateTime, server_default=func.now())
)

if __name__ == "__main__":
  try:
    metadata_obj.create_all(engine)
  except Exception as error:
    print(f"An error ocurrred: {error}")