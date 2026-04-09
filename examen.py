# EXAMEN DE RECUPERACIÓN - UNIDAD 2

# IMPORTANTE:
# 1. La salida debe ser ÚNICAMENTE el resultado. No agregues texto extra.
# 2. No modifiques las condiciones del menú (if/elif).
# 3. Usa solo una función print() por ejercicio.

problema = int(input("Número del problema (1-10): "))

if problema == 1:
    # Problema 1: Área de un círculo con radio 15.
    # Fórmula: Area = 3.1416 * r^2
    r = 15
    # Tu código aquí
    area_of_circle = (3.14 * (r ** 2))
    print('Area of circle with radius 2:', area_of_circle)
elif problema == 2:
    # Problema 2: Genera una clave de producto (concatenar) con código y lote.
    # Resultado esperado: "prod-88-loteb" (todo en minúsculas).
    codigo = 88
    lote = "-LoteB"
    # Tu código aquí
    clave = 'prod-' + str(codigo) + lote.lower()
    print(clave)
elif problema == 3:
    # Problema 3: Verifica si el carácter '@' está en el correo dado.
    email = "usuario.upa.edu.mx"
    # Tu código aquí
    print('Is \'@\' in usuario.ups.edu.mx?', '@' in email)
elif problema == 4:
    # Problema 4: Convierte todo el texto a MAYÚSCULAS.
    aviso = "el examen termina pronto"
    # Tu código aquí
    aviso_min = aviso.upper()
    print(aviso_min)
elif problema == 5:
    # Problema 5: Convierte el string "150.50" a float y luego a entero.
    # Imprime ambos resultados en una sola línea.
    dato = "150.50"
    # Tu código aquí
    dato_float = float(dato)
    dato_entero = int(dato_float)
    print('Float:', dato_float,'Entero:', dato_entero)
elif problema == 6:
    # Problema 6: Conversión de Temperatura (Celsius a Fahrenheit).
    # C=30. Fórmula: F = (C * 1.8) + 32
    celsius = 30
    # Tu código aquí
    fahrenheit = (celsius * 1.8) + 32
    print('30 celsius a Fahrenheit:', fahrenheit)
elif problema == 7:
    # Problema 7: Extrae los primeros 5 caracteres de la cadena.
    frase = "Programación en Python"
    # Tu código aquí
    resultado = frase[:5]
    print(resultado)
elif problema == 8:
    # Problema 8: Calcula la Densidad de un objeto.
    # Masa: 500kg, Volumen: 2m^3. Fórmula: d = m / v
    m = 500
    v = 2
    # Tu código aquí
    d = m/v
    print('Densidad:', d)
elif problema == 9:
    # Problema 9: Determina si un número es negativo.
    numero = -15
    # Tu código aquí
    es_negativo = numero < 0
    print('Es -15 negativo?', es_negativo)
elif problema == 10:
    # Problema 10: Calcula la Energía Potencial.
    # m=5kg, h=10m, g=9.81. Fórmula: Ep = m * g * h
    m = 5
    h = 10
    g = 9.81
    # Tu código aquí
    EP = m * g * h
    print('Energia Potencial:', EP)
else:
    print("Ingresa un número entre 1 y 10.")