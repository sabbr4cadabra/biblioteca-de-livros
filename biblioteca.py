class Livro:

  def __init__(self, titulo, autor):

    self.titulo = titulo

    self.autor = autor

    self.disponivel = True



  def emprestar(self):

    if self.disponivel:

      self.disponivel = False

      print(f"O livro '{self.titulo}' foi emprestado.")

    else:

      print(f"O livro '{self.titulo}' não está disponível no momento.")



  def devolver(self):

    if not self.disponivel:

      self.disponivel = True

      print(f"O livro '{self.titulo}' foi devolvido.")

    else:

      print(f"O livro '{self.titulo}' já está disponível.")





class Biblioteca:

  def __init__(self):

    self.livros = []



  def adicionar_livro(self, livro):

    self.livros.append(livro)



  def listar_livros_disponiveis(self):

    print("Livros disponíveis na biblioteca:")

    for livro in self.livros:

      if livro.disponivel:

        print(f"- {livro.titulo} por {livro.autor}")



  def alugar_livro(self, titulo):

    for livro in self.livros:

      if livro.titulo == titulo:

        livro.emprestar()

        return

    print("Livro não encontrado na biblioteca.")





# Livros Fic

livro1 = Livro("Python for Beginners", "John Smith")

livro2 = Livro("Data Science Essentials", "Maria Garcia")

livro3 = Livro("Introduction to Algorithms", "Thomas Cormen")



# Adicionando livros à biblioteca

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)

biblioteca.adicionar_livro(livro2)

biblioteca.adicionar_livro(livro3)



# Listando livros disponíveis

biblioteca.listar_livros_disponiveis()



# Alugando um livro

biblioteca.alugar_livro("Python for Beginners")

biblioteca.listar_livros_disponiveis()



# Tentando alugar o mesmo livro novamente

biblioteca.alugar_livro("Python for Beginners")

