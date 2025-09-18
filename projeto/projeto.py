import json

# cadastrar, listar, atualizar e excluir livros, armazenando as informações em arquivos JSON.

livros = []
while True:
    livro = {}
    
    print('--- SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ---')
    # menu 
    print('1 - Cadastrar livro.')
    print('2 - Listar.')
    print('3 - Atualizar.')
    print('4 - Excluir livro.')
    print('5 - Encerrar programa.')

    opcao = input('Digite a opção que deseja selecionar: ')
     
    match opcao:
        case '1':
            livro['nome'] = input('Digite o nome do livro: ').strip().lower()
            livro['autor'] = input('Digite o nome do autor do livro: ').strip().lower()

            with open(fr"projeto.json", "w", encoding='utf-8') as f:
             json.dump(livro, f,ensure_ascii=False, indent=4)
            livros.append(livro)
            
        case '2':
           with open("projeto.json", "r", encoding="utf-8") as f: 
            livros = json.load(f) 
            for livro in livros:
                print(f"Nome: {livro['nome']}, Autor: {livro['autor']}")
            

        case '3':
          livro = input('Digite o nome do livro que deseja atualizar:').strip().lower
          with open("projeto.json", "r", encoding="utf-8") as f: 
            livros = json.load(f) 
        case '4':
         delete = input('Digite o nome do livro que deseja excluir: ').strip().lower()
         with open("projeto.json", "w", encoding="utf-8") as f: 
          excluir = json.load(f) 
          for livro in excluir:
            if livro['nome'] == delete:
                excluir.remove(livro)
                with open("projeto.json", "w", encoding="utf-8") as f:
                    json.dump(excluir, f, ensure_ascii=False, indent=4)
                print(f'Livro {delete} excluído com sucesso!')
          
        case '5':
          print('Programa encerrado. Até logo!')
         
          break
