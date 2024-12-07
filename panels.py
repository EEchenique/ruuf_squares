def calculate_max_panels(x, y, a, b):
    """
    Calcula el número máximo de paneles que caben en un techo.
    Los paneles pueden colocarse horizontal o verticalmente (rotación de 90°).
    
    Arguments:
        x (float): Ancho del techo
        y (float): Alto del techo
        a (float): Alto del panel
        b (float): Ancho del panel
    
    Returns:
        int: Número máximo de paneles que caben
    """
    # Validaciones
    if not all(isinstance(dim, (int, float)) for dim in [x, y, a, b]):
        raise TypeError("Todas las dimensiones deben ser números")
    
    if not all(dim > 0 for dim in [x, y, a, b]):
        raise ValueError("Todas las dimensiones deben ser positivas")
    
    if min(a, b) > min(x, y) or max(a, b) > max(x, y):
        return 0  # Si el panel es más grande que el techo, no cabe ninguno

    max_paneles = 0
    
    # caso 1: panel horizontal
    # Probamos colocando paneles horizontalmente (acostados)
    filas_h = y // a  # Número de filas que caben
    for i in range(int(filas_h) + 1):
        espacio_usado_y = i * a
        espacio_restante_y = y - espacio_usado_y
        
        # Paneles horizontales en las filas completas
        paneles = i * (x // b)
        
        # Si queda espacio vertical, intentamos poner paneles verticales
        if espacio_restante_y >= b:
            paneles += (x // a) * (espacio_restante_y // b)
            
        max_paneles = max(max_paneles, paneles)
    
    # caso 2: panel vertical
    # Probamos colocando paneles verticalmente (parados)
    columnas_v = x // a  # Número de columnas que caben
    for i in range(int(columnas_v) + 1):
        espacio_usado_x = i * a
        espacio_restante_x = x - espacio_usado_x
        
        # Paneles verticales en las columnas completas
        paneles = i * (y // b)
        
        # Si queda espacio horizontal, intentamos poner paneles horizontales
        if espacio_restante_x >= b:
            paneles += (y // a) * (espacio_restante_x // b)
            
        max_paneles = max(max_paneles, paneles)
    
    return int(max_paneles)

# Ejemplo de uso
if __name__ == "__main__":
    dimensiones = input("Ingrese las dimensiones del techo y del panel (x, y, a, b): ")
    x, y, a, b = map(float, dimensiones.split())
    resultado = calculate_max_panels(x, y, a, b)
    print(f"Número máximo de paneles: {resultado}")  