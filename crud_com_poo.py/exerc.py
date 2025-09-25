# Sistema de gerenciamento de uma biblioteca com POO e JSON
import json
livros = []
with open("poo.json", "r", encoding="utf-8") as f:
             # abre o arquivo json
    
            livros = json.load(f)

class Biblioteca():
    def __init__(self, nome_livro, autor, ID):
     self.livro = nome_livro
     self.autor = autor
     self.ID = ID

@property
def nome_livro(self):
        return self.__nome_livro
    
@nome_livro.setter
def nome(self,novo_livro):
       self.__nome = novo_livro

@ property
def autor(self):
        return self.__autor
    
@autor.setter
def autor(self, autor):
        self.__autor = autor

@ property
def ID(self):
        return self.__ID
    
@ID.setter
def ID(self, ID):
        self.__ID = ID


while True:
    print('--- SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ---')
    print('1 - Cadastrar livro.')
    print('2 - Listar.')
    print('3 - Atualizar.')
    print('4 - Excluir livro.')
    print('5 - Encerrar programa.')

    opcao = input('Digite a opção que deseja selecionar: ')

    match opcao:
     case '1':
         livro = {}
         livro = {}
            # dicionario
         livro['nome'] = input('Digite o nome do livro: ').strip().lower()
         livro['autor'] = input('Digite o nome do autor do livro: ').strip().lower()
         livro['ID'] = input('Digite o número do ID: ')
         livros.append(livro) 
          
         with open("poo.json", "w", encoding="utf-8") as f:
             json.dump(livros, f, ensure_ascii=False, indent=4)   
            
     case '2':
      dados = Biblioteca('Alienista', 'Machado de Assis', '01')
      print(dados.livro)
      print(dados.autor)
      print(dados.ID)
      with open("poo.json", "w", encoding="utf-8") as f:
             json.dump(livros, f, ensure_ascii=False, indent=4)
    
     case '3':
      ...
    
     case '4':
      ...
    
     case '5':
      print('Programa encerrado. Até logo!')
      break
        
     case _:
      print("Opção inválida, tente novamente.")