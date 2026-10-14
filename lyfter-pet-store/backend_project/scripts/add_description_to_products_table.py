from sqlalchemy import update
from app.db.models import products_table
from app.db.database import engine

products = [
  {
    "id": 1,
    "description": "Alimento seco para perros adultos, diseñado para complementar su nutrición diaria y ayudar a mantenerlos activos."
  },
  {
    "id": 2,
    "description": "Arena para gatos que forma grumos para facilitar la limpieza del arenero y mantener un espacio más higiénico."
  },
  {
    "id": 3,
    "description": "Juguete de cuerda resistente, ideal para juegos de tirar y morder con perros de tamaño mediano."
  },
  {
    "id": 4,
    "description": "Comedero doble de acero inoxidable con base antideslizante, práctico para servir agua y alimento."
  },
  {
    "id": 5,
    "description": "Rascador con poste de sisal que permite a los gatos afilar sus uñas y satisfacer su instinto natural de arañar."
  },
  {
    "id": 6,
    "description": "Transportadora de plástico para facilitar el traslado de mascotas medianas, con estructura práctica para viajes y visitas veterinarias."
  },
  {
    "id": 7,
    "description": "Premio para perros con sabor a pollo, ideal para complementar su rutina de recompensas."
  },
  {
    "id": 8,
    "description": "Pecera de vidrio de 20 litros que incluye tapa y filtro para facilitar el montaje y mantenimiento del acuario."
  },
  {
    "id": 9,
    "description": "Jaula equipada con rueda de ejercicio y bebedero para ofrecer a tu hámster un espacio con accesorios básicos."
  },
  {
    "id": 10,
    "description": "Collar antiparasitario Seresto para perros grandes, diseñado para ayudar a proteger contra pulgas y garrapatas."
  },
  {
    "id": 11,
    "description": "Suplemento vitamínico en gotas para añadir al agua de aves exóticas, siguiendo las indicaciones del fabricante o veterinario."
  },
  {
    "id": 12,
    "description": "Champú formulado para la higiene de perros con piel sensible, indicado para uso veterinario según sus instrucciones."
  },
  {
    "id": 13,
    "description": "Bolsas para recoger los desechos de tu perro durante los paseos, presentadas en un práctico rollo de 15 unidades."
  },
  {
    "id": 14,
    "description": "Alimento para peces tropicales en presentación de 100 g, pensado para complementar su alimentación diaria."
  },
  {
    "id": 15,
    "description": "Bebedero automático de 2 litros con filtro de carbón activado, diseñado para ayudar a mantener el agua de las mascotas fresca y limpia."
  },
  {
    "id": 26,
    "description": "Juguete con forma de hueso para que los perros puedan entretenerse mordiendo durante sus momentos de juego."
  },
]

with engine.connect() as conn:
  for product in products:
    stmt = (
      update(products_table)
      .where(products_table.c.id == product["id"])
      .values(description=product["description"])
    )

    conn.execute(stmt)

  conn.commit()