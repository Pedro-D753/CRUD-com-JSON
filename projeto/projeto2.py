import json
# importa o JSON que tem como função nesse código "banco" da Biblioteca para gerenciar

livros = []
#lista vazia

# Carregar os livros existentes, se houver

with open("projeto2.json", "r", encoding="utf-8") as f:
             # abre o arquivo json
    
            livros = json.load(f)
            # lê o arquivo json
        

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
            # dicionario
            livro['nome'] = input('Digite o nome do livro: ').strip().lower()
            livro['autor'] = input('Digite o nome do autor do livro: ').strip().lower()
            livros.append(livro) 
            # Adiciona um elemento no final da lista, nesse caso no JSON

            with open("projeto2.json", "w", encoding="utf-8") as f:
                
                json.dump(livros, f, ensure_ascii=False, indent=4)
                # cria um arquivo JSON com recuo de 4 espaços

            print(" Livro cadastrado com sucesso!")

        case '2':
            for livro in livros:
                print(f"Nome: {livro['nome']}, Autor: {livro['autor']}")
                # Mostra o livro cadastrado junto ao autor da obra literária

        case '3':
            for livro in livros:
                print(f"Nome: {livro['nome']}, Autor: {livro['autor']}")
            nome = input('Digite o nome do livro que deseja atualizar: ').strip().lower()
            if livro['nome'] == nome:
                    livro['nome'] = input('Novo nome: ').strip().lower()
                    livro['autor'] = input('Novo autor: ').strip().lower()
                    livro['genero_literario'] = input('Novo gênero literário').strip().lower()
                    with open("projeto2.json", "w", encoding="utf-8") as f:
                        json.dump(livros, f, ensure_ascii=False, indent=4)
                    print("Livro atualizado com sucesso!")
                    

        case '4':
            for livro in livros:
              print(f"Nome: {livro['nome']}, Autor: {livro['autor']}")
              delete = input('Digite o nome do livro que deseja excluir: ').strip().lower()
            if livro['nome'] == delete:
                    livros.remove(livro)
                    with open("projeto2.json", "w", encoding="utf-8") as f:
                        json.dump(livros, f, ensure_ascii=False, indent=4)
                    print(f" Livro '{delete}' excluído com sucesso!")
                    # livro deletado
                    

        case '5':
            print('Programa encerrado. Até logo!')
            break

        case _:
            print("Opção inválida, tente novamente.")
