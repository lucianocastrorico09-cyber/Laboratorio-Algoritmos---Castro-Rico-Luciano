# 2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debe finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un programa que lea los datos de las cuentas corrientes e informe:
#● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo, sabiendo que:
    #○ Estado de la cuenta:
    #○ “Acreedor” si el saldo es &gt; 0.
    #○ “Deudor” si el saldo es &lt; 0.
    #○ “Nulo” si el saldo es = 0.
#● b) La suma total de los saldos acreedores.

totalAcreedores = 0

while True:
    numeroCuenta = int(input("Ingrese el número de cuenta: "))


    if numeroCuenta < 0:
        break

    saldo = int(input("Ingrese el saldo actual: "))

    if saldo > 0:
        estado = "Acreedor"
        totalAcreedores += saldo
    elif saldo < 0:
        estado = "Deudor"
    else:
        estado = "Nulo"

    print(f"Número de cuenta: {numeroCuenta} - Estado: {estado}")

print(f"Total de saldos acreedores: {totalAcreedores}")