class tabuada:
  def __init__(self, n1, n2):
    self.n1 = n1
    self.n2 = n2
    
  def resultado(self, op):
    if(op == '+'):
      resultado = (self.n1 + self.n2)
    if(op == '-'):
      resultado = (self.n1 - self.n2)
    if(op == '*'):
      resultado = (self.n1 * self.n2)
    if(op == '/'):
      resultado = (self.n1 / self.n2)
      
    print(f'O resultado eh {resultado}')

