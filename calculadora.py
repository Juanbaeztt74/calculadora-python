contraseña = "JUAN123"

CONTRA1 = input("INGRESE LA CONTRASEÑA: ").strip()

if CONTRA1 == "JUAN123" :
    print("CONTRASEÑA CORRECTA")
    input("PRESIONA ENTER PARA CONTINUAR")
    
    
    
else:
  print("CONTRASEÑA INCORRECTA")
  input("PRESIONA ENTER PARA SALIR")
  exit()


NOMBRE = input("PARA CONTINUAR DIME TU NOMBRE: ").upper()

print("HOLA", NOMBRE, "BIENVENIDO")

Num1 = int(input("DIME EL PRIMER VALOR"))
Num2 = int(input("DIME EL SEGUNDO VALOR"))

SUMA = Num1 + Num2
MULTI = Num1 * Num2
RESTA = Num1 - Num2
DIVIS = Num1 // Num2

print(NOMBRE," El RESULATADO DE LA SUMA ES:" ,SUMA, "Y SU TIPO DE DATO ES: ", type(SUMA))
print(NOMBRE," El RESULATADO DE LA MULTIPLICACION ES:" ,MULTI, "Y SU TIPO DE DATO ES: ", type(MULTI))
print(NOMBRE," El RESULATADO DE LA RESTA ES:" ,RESTA, "Y SU TIPO DE DATO ES: ", type(RESTA))
print(NOMBRE," El RESULATADO DE LA DIVISION ES:" ,DIVIS, "Y SU TIPO DE DATO ES: ", type(DIVIS))

print("-----------------------------------------------------------------------------------")
print("GRACIAS POR UTILIZAR LA CALCULADORA")
