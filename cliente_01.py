class Cliente:
  
  def __init__(self, nome):
    self.__nome = nome 
   
  @property # com ele nao eh necessario nome()
  def nome(self):
    return self.__nome.title() 
  
  @nome.setter # Ao inves de cliente.nome('Gustavo'), Uso cliente.nome = 'Gustavo'  $variavel.setter
  def nome(self, nome):
    self.__nome = nome
    