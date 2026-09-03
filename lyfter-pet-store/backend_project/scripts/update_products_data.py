from sqlalchemy import update
from app.db.models import products_table
from app.db.database import engine

products = [
  {"id": 1, "image": "/images/products/dog_food.jpg"},
  {"id": 2, "image": "/images/products/cat_litter.jpg"},
  {"id": 3, "image": "/images/products/dog_toy.jpg"},
  {"id": 4, "image": "/images/products/dog_bowl_double.jpg"},
  {"id": 5, "image": "/images/products/scratching_post.jpg"},
  {"id": 6, "image": "/images/products/pet_cage.jpg"},
  {"id": 7, "image": "/images/products/dog_treat_chicken_flavor.jpg"},
  {"id": 8, "image": "/images/products/fish_tank.jpg"},
  {"id": 9, "image": "/images/products/hamster_cage.jpg"},
  {"id": 10, "image": "/images/products/flea_collar.jpg"},
  {"id": 11, "image": "/images/products/vitamin_drops_for_birds.jpg"},
  {"id": 12, "image": "/images/products/dog_shampoo.jpg"},
  {"id": 13, "image": "/images/products/trash_bags.jpg"},
  {"id": 14, "image": "/images/products/fish_pellets.jpg"},
  {"id": 15, "image": "/images/products/automatic_pet_water_fountain.jpg"},
  {"id": 26, "image": "/images/products/bone_chew_toy.jpg"},
]

with engine.connect() as conn:
  for product in products:
    stmt = (
      update(products_table)
      .where(products_table.c.id == product["id"])
      .values(image=product["image"])
    )

    conn.execute(stmt)

  conn.commit()