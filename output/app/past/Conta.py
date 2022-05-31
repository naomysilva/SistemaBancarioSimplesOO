class Conta:
    def __init__(self,banco,tituloConta,agencia,saldo):
        self.banco = banco
        self.tituloConta = tituloConta
        self.agencia = agencia
        self.saldo = saldo
    
    def informação(self):
        print("Olá ", self.tituloConta," seu banco é", self.banco, "e o numero da sua agencia é:", self.agencia)
        
    def imprimiSaldo(self):
        print("Saldo: R$ %.2f" % self.saldo)
        
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("saldo insuficiente para esta operação")
            return False
    def depositar(self,valor):
        self.saldo += valor
        
    def tranferir(self,conta_destino,valor):
        if self.sacar(valor) == True:
            conta_destino.depositar(valor)
            
