class Conta:
  def __init__(self, numero, titular, saldo, limite):
    print(f'Valor do self eh: {self}')
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite



  def extrato(self):
    print(f'Saldo do {self.__titular}: {self.__saldo}')

  def __pode_sacar(self, valor):
    valordisp = (self.__saldo + self.__limite)
    return valor <= valordisp


  def saque(self, valor):
    if(self.__pode_sacar(valor)):
      self.__saldo -= valor
    else:
      print('O valor excedeu o limite')
    print(f' Saldo final do {self.__titular}: {self.__saldo}')
  
  def depositar(self, valor):
    self.__saldo += valor
    print(f' Saldo final do {self.__titular}: {self.__saldo}')

  def transferir(self, valor, destino):
    self.saque(valor)
    destino.depositar(valor)  

  @property
  def saldo(def):
    return self.__saldo

  @property 
  def titular(def):
    return self.__titular
  
  @property
  def limite(def):
    return self.__limite
  
  @limite.setter
  def limite(def, limite):
    self.__limite = limite

  @staticmethod
  def codigo_banco():
    return '001'

  @staticmethod
  def codigos_bancos():
    return {'BB': '001','CAIXA': '104','BRADESCO': '237'}
     
     


