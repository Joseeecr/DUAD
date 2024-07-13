sales = [
    {
        "date" : "29/05/2024",
        "costumer_email": "keilor.chacon@gmail.com",
        "items": [
            {
                "name": "Balón de fútbol",
                "upc":"item-448",
                "unit_price":30,
            },           
            {
                "name": "Tacos de fútbol",
                "upc":"item-445",
                "unit_price":90,
            },
            {
                "name": "Espinilleras",
                "upc":"item-440",
                "unit_price":10,
            },
        ],
    },    
    {
        "date" : "30/05/2024",
        "costumer_email": "bele.chinchilla@gmail.com",
        "items": [
            {
                "name": "Esmalte para uñas",
                "upc":"item-157",
                "unit_price":2.2,
            },
        ],
    },    
    {
        "date" : "27/05/2024",
        "costumer_email": "tefa.granados@gmail.com",
        "items": [
            {
                "name": "Esmalte para uñas",
                "upc":"item-157",
                "unit_price":2.2,
            },  
            {
                "name": "Corta uñas",
                "upc":"item-155",
                "unit_price":3,
            },
        ],
    },    
    {
        "date" : "02/06/2024",
        "costumer_email": "andres.chacon@gmail.com",
        "items": [
            {
                "name": "Tacos de fútbol",
                "upc":"item-445",
                "unit_price":90,
            }, 
            {
                "name": "Espinilleras",
                "upc":"item-440",
                "unit_price":10,
            },  
            {
                "name": "Botella de agua",
                "upc":"item-300",
                "unit_price":5.50,
            },    
            {
                "name": "Camiseta deportiva",
                "upc":"item-470",
                "unit_price":20,
            },
        ],
    },   
    {
        "date" : "27/05/2024",
        "costumer_email": "yola.brenes@gmail.com",
        "items": [
            {
                "name": "Botella de agua",
                "upc":"item-300",
                "unit_price":5.50,
            }, 
            {
                "name": "Balón de fútbol",
                "upc":"item-448",
                "unit_price":30,
            },
        ],
    }, 
]
upc_total_sales = {}
for sale in sales:
    for item in sale["items"]:
        upc = item["upc"]
        unit_price = item["unit_price"]
        if upc in upc_total_sales:
            upc_total_sales[upc] += unit_price
        else:
            upc_total_sales[upc] = unit_price
print(upc_total_sales)