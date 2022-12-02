#Mi Calculadora
print("Bienvenido a mi calculadora")
#print(" ")
#opcion = [0, 1, 2, 3, 4, 5]
op = 0
while int(op) <= 5:
    print(' ')
    op = input('Ingresa la operacion a realizar: 1.SUMAR - 2.RESTAR 3.MULTIPLICAR 4.DIVIDIR 5.Seleccionar otra opcion aritmetica 6.SALIR: ')
    if int(op) == 5:
        print('Volver a seleccionar opcion aritmetica')
        print(' ')
        op = input('Ingresa la operacion a realizar: 1.SUMAR - 2.RESTAR 3.MULTIPLICAR 4.DIVIDIR 5.Seleccionar otra opcion aritmetica 6.SALIR: ')
    if int(op) == 6:
            print('bye bye ;)')
            exit
    else:
        if int(op) >= 7:
            print('opcion invalida')
            op = input('Ingresa la operacion a realizar: 1.SUMAR - 2.RESTAR 3.MULTIPLICAR 4.DIVIDIR 5.Seleccionar otra opcion aritmetica 6.SALIR: ')
            print(' ')
        else:
            num1 = input('Ingresa el primer numero: ')
            num2 = input('Ingresa el segundo numero: ')
            print(' ')
        if int(op) == 1:
            sum = int(num1) + int(num2)
            print("El resultado de la suma es: " + str(sum))
        else:
            if int(op) == 2:
                if num1 > num2:
                    res = (int(num1) - int(num2))
                    print("El resultado de la resta es: " + str(res))
                else:
                    res = (int(num2) - int(num1))
                    print("El resultado de la resta es: " + str(res))
            else:
                if int(op) == 3:
                    mul = (int(num1) * int(num2))
                    print("El resultado de la multiplicacion es: " + str(mul))
                else:
                    if int(op) == 4:
                        if num1 < num2:
                            print('El primer numero ingresado es menor que el segundo')
                            div = int(0)
                            print("El resultado de la division es: " + str(div))
                        else:
                            div = (float(num1) / float(num2))
                            print("El resultado de la division es: " + str(div))
                            
                        
                                
                        
