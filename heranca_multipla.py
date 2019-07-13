class Programa:
  def __init__(self, nome, ano):
    self.__nome = nome
    self.ano = ano
    self._likes = 0

  @property
  def likes(self):
    return self._likes

  def set_like(self):
    self._likes += 1
  
  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, novo_nome):
    self.__nome = novo_nome.title()
  
  def __str__(self):
    return f'{self.__nome} {self.ano} {self._likes} Likes'

class Filme(Programa):
   def __init__(self, nome, ano, duracao):
    super().__init__(nome, ano)
    self.duracao = duracao

   def __str__(self):
    return f'{self.nome} {self.ano} {self.duracao} Min {self._likes} Likes'
    

class Serie(Programa):
   def __init__(self, nome, ano, temporada):
    super().__init__(nome, ano)    
    self.temporada = temporada

   def __str__(self):
    return f'{self.nome} {self.ano} {self.temporada} Temporadas {self._likes} Likes'


class Playlist:
  def __init__(self, nome, programas):
    self.nome = nome
    self._programas = programas

  def __getitem__(self, item):
    return self._programas[item]

  @property
  def listagem(self):
    return self._programas

  @property
  def __len__(self):
    return len(self._programas)

  

mulher_maravilha = Filme('Mulher Maravilha',2018, 80)
mulher_maravilha.set_like()
 

friends = Serie('Friends',1999, 10)
friends.set_like()



filmes_e_series = [mulher_maravilha, friends]
fim_de_semana = Playlist('Fim de semana', filmes_e_series)


for programas in fim_de_semana:
  print(programas)