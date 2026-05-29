import csv

# Función para realizar la operación matemática
def realizar_operacion(operacion, num1, num2):
    if operacion == "SUM":
        return num1 + num2
    elif operacion == "SUB":
        return num1 - num2
    elif operacion == "MUL":
        return num1 * num2
    elif operacion == "DIV":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: division por cero"
    elif operacion == "POW":
        try:
            resultado = num1 ** num2
            return resultado
        except OverflowError:
            return "Error: numero muy grande"
    else:
        return "Operacion desconocida"

# Leer el archivo CSV
filas_actualizadas = []

with open("data/math_operations.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    encabezados = list(lector.fieldnames)
    if "result" not in encabezados:
        encabezados = encabezados + ["result"]
    for fila in lector:
        operacion = fila["operation"]
        num1 = float(fila["operand_1"])
        num2 = float(fila["operand_2"])
        resultado = realizar_operacion(operacion, num1, num2)
        fila["result"] = resultado
        filas_actualizadas.append(fila)

# Guardar el CSV con los resultados
with open("data/math_operations.csv", "w", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=encabezados)
    escritor.writeheader()
    escritor.writerows(filas_actualizadas)

print("Listo! El archivo CSV fue actualizado con los resultados.")