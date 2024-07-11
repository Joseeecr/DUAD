user_time = float(input("Ingrese un tiempo en segundos "))
if(user_time < 600):
    tiempo_faltante = 600 - user_time
    print(f"Te faltan {tiempo_faltante} segundos para alcanzar 10 minutos!")
else:
    print("Su número es mayor a 10 minutos!")
    
    """ Usé float para probar porque
    quería ver si ingresando 600.1 funcionaba con int
    pero me tiró error, entonces con float sí funcionó
    pero no sé si no será una muy buena práctica  
    """