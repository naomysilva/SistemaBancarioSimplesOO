from ast import main
from Conta import * 

Conta_principal = Conta("Nubank","Naomy",123,500)
Conta_secundaria = Conta("Bradesco","Leonardo",456,1500)

Conta_principal.depositar(300)
Conta_principal.imprimiSaldo()
Conta_principal.informação()
Conta_principal.sacar(100)
Conta_principal.imprimiSaldo()
Conta_principal.tranferir(Conta_secundaria,400)
Conta_secundaria.informação()
Conta_principal.imprimiSaldo()
Conta_secundaria.imprimiSaldo()

if __name__ == "__main__":
    main()