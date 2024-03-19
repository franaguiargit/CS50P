expression = input('ingresar: ')

x, y ,z = expression.split(' ')

def aritmetica(x,y,z):
    if y == "+":
        resultado = float(int(x) + int(z))
        print(f"{x} + {z} = {resultado}")
    elif y == "-" :
        resultado = float(int(x) - int(z))
        print(f"{x} - {z} = {resultado}")
    elif y == "/" :
        resultado = float(int(x) / int(z))
        print(f"{x} / {z} = {resultado}")
    elif y == "*" :
        resultado = float(int(x) * int(z))
        print(f"{x} * {z} = {resultado}")


aritmetica(x,y,z)