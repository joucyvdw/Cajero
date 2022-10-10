#Cajero JCGP
class ATM:
    saldo=1000
    intentos=0
    while intentos<3:
        password = input ('Escriba Contraseña: ')
        intentos = intentos+1
        if password == ('1234'):
            print('Menu')
            print('1 : Consultar saldo ')
            print('2 : Retirar saldo ')
            print('3 : Histórico de Movimientos ')
            print('4 : Salir ')
            while True:
                opcion = int(input('Seleccione la opcion deseada:'))
                if opcion == 1:
                    print('Tiene un saldo disponible de: '+str(saldo))
                    break
                elif opcion == 2:
                    r = int(input('Cuanto desea retirar?'))
                    if r <= saldo:
                        Ns = saldo-r
                        print('Su saldo ha sido actualisado a:'+str(Ns))
                        break
                    elif r > saldo:
                        print('Saldo insuficiente')
                        break
                elif opcion == 3:
                    print('Movimientos realizados')
                    break
                elif opcion == 4:
                    print('Gracias por usar nuestros servicios')
                    break
        else:
            print('Contraseña Incorrecta Vuelva a Intentarlo')
    else:
        if intentos==3:
            print('Intentos agotados')



