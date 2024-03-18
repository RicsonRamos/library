import os
import csv
import time

class Cabecalho:
    def imprimir(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo = "BIBLIOTECA FACULDADE ANHANGUERA"
        subtitulo = "GESTÃO DO ACERVO"
        print('=' * 80)
        print(titulo.center(80))
        print(subtitulo.center(80))
        print('=' * 80)

class Encerramento:
    def encerrar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho = Cabecalho()
        cabecalho.imprimir()
        #print("\n\nEncerrando Programa")
        animacao = "Encerrando Programa"
        for _ in range(5):  # Definindo 5 iterações para a animação
            animacao += "."  # Adiciona um ponto à string
            print(animacao, end="\r")  # Imprime a string sem nova linha
            time.sleep(0.5)  # Aguardar 0.5 segundos entre cada ponto
        print()  # Adicionar nova linha após a animação
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()

class Pesquisa:
    
    def imprimir(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho = Cabecalho()
        cabecalho.imprimir()
        print("PESQUISA".center(80))
        print("[1] Pesquisar por livro\n"
              "[2] Pesquisar por usuário\n"
              "[0] Sair\n")
        opcao = input("Digite o número e clique em enter: ")
        
        if opcao == "1":
            titulo = input("Digite o título ou ISBN do livro que deseja pesquisar: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho.imprimir()
            print("PESQUISA".center(80))
            self.pesquisar_livro(titulo)
        elif opcao == "2":
            nome = input("Digite o nome ou ID do usuário que deseja pesquisar: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho.imprimir()
            print("PESQUISA".center(80))
            self.pesquisar_usuario(nome)
        elif opcao == "0":
            encerramento = Encerramento()  # Criar uma instância de Encerramento
            encerramento.encerrar()  # Chamar o método encerrar de Encerramento
        else:
            print("Opção inválida! Digite novamente o número correspondente.")
            self.imprimir()

    # Função para pesquisar um livro pelo título
    def pesquisar_livro(self, titulo):
        with open('livros.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            livro_encontrado = False
            for row in reader:
                if row['titulo'].lower().startswith(titulo.lower()) or row['isbn'].startswith(titulo.lower()):
                    print("\nLivro encontrado:")
                    print("Título:", row['titulo'])
                    print("Autor:", row['autor'])
                    print("ISBN:", row['isbn'])
                    print("Genero:", row['genero'])
                    print("Ano publicação:", row['ano_publicacao'])
                    print("Quantidade Disponível:", row['quantidade_disponivel'])
                    livro_encontrado = True
                    break
            if not livro_encontrado:
                cabecalho = Cabecalho()
                cabecalho.imprimir()
                print("\n\nLivro não encontrado...\n\n\n")  

            while True: 
                final = input("\n\n\nDeseja continuar (Y/N): ")
                if final.lower() == "y":
                    self.imprimir()  # Retorna ao menu principal
                elif final.lower() == "n":
                    MenuPrincipal()
                else:
                    print('Opção Inválida!')
                    
    def pesquisar_usuario(self, nome):
        with open('usuarios.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            usuario_encontrado = False
            # Nome,Telefone,email,ID do aluno
            for row in reader:
                if row['nome'].lower() == nome.lower() or row['id_aluno'] == nome.lower():
                    print("\nAluno encontrado:")
                    print("Nome:", row['nome'])
                    print("Telefone:", row['telefone'])
                    print("E-mail:", row['email'])
                    print("ID do Aluno:", row['id_aluno'])
                    print()
                    usuario_encontrado = True
                    break
            if not usuario_encontrado:
                print("\n\Aluno não encontrado...\n\n\n")  

            while True: 
                final = input("\nDeseja continuar (Y/N): ")
                if final.lower() == "y":
                    self.imprimir()  # Retorna ao menu principal
                elif final.lower() == "n":
                    MenuPrincipal()
                else:
                    print('Opção Inválida!')  

class CadastroLivro:

    def __init__(self) -> None:
        self.arquivo = "livros.csv"  # Nome do arquivo de livros
        self.lista_livros = []  # Inicializa a lista de livros vazia

    def imprimir(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho = Cabecalho()
        cabecalho.imprimir()
        print("CADASTRO DE LIVROS".center(80))
        print("[1] Cadastrar novo livro\n"
              "[0] Voltar ao menu principal\n")
        opcao = input("Digite o número e clique em enter: ")

        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho = Cabecalho()
            cabecalho.imprimir()
            self.cadastrar_livros()  # Chamar o método para cadastrar novos livros
        elif opcao == "0":
            MenuPrincipal()  # Voltar ao menu principal
        else:
            print("Opção inválida! Digite novamente o número correspondente.")
            self.imprimir()  # Se a opção for inválida, imprimir novamente o menu

    def carregar_livros(self):
        # Verifica se o arquivo existe
        if os.path.exists(self.arquivo):
            with open(self.arquivo, mode='r+', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                # Carrega os dados existentes para a lista de livros
                self.lista_livros = [row for row in reader]
        else:
            self.lista_livros = []

    def adicionar_livro(self):
        livro = {
            'titulo': input("Digite o título do livro: "),
            'autor': input("Digite o nome do autor: "),
            'isbn': input('Digite o número ISBN: '),
            'genero': input('Digite o gênero do livro: '),
            'ano_publicacao': input("Digite o ano de publicação: "),
            'quantidade_disponivel': input("Digite a quantidade de livros disponíveis: ")
        }
        
        self.lista_livros.append(livro)

    def _salvar_arquivo(self):
        with open(self.arquivo, mode='r+', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['titulo', 'autor', 'isbn', 'genero', 'ano_publicacao', 'quantidade_disponivel'])
            if os.path.getsize(self.arquivo) == 0:
                writer.writeheader()
            writer.writerow(self.lista_livros[-1])  # Escreve apenas o último livro adicionado

    def cadastrar_livros(self):
        while True:
            self.adicionar_livro()
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho = Cabecalho()
            cabecalho.imprimir()
            print("CADASTRO DE LIVROS".center(80))
            print("Livro cadastrado:")
            for chave, valor in self.lista_livros[-1].items():
                print(f"{chave.capitalize()}: {valor}")

            final = input("\nAs informações digitadas estão corretas? [1] Sim [2] Não [0] Sair: ")
            if final == "0":
                MenuPrincipal()
            elif final == "1":
                self._salvar_arquivo()  # Salva o livro apenas quando as informações estiverem corretas
                cabecalho = Cabecalho()
                cabecalho.imprimir()
                print("\n\n\nLivro cadastrado com sucesso!\n")
                time.sleep(2)
            elif final == "2":
                cabecalho = Cabecalho()
                cabecalho.imprimir()
                print("\n\n\nCadastre o livro novamente!\n")
                time.sleep(2)
            else:
                cabecalho = Cabecalho()
                cabecalho.imprimir()
                print("\n\n\nOpção Inválida!\n")
                time.sleep(2)

            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho = Cabecalho()
            cabecalho.imprimir()
            print("CADASTRO DE LIVROS".center(80))
            cadastrar_outro = input("\nDeseja cadastrar outro livro? [1] Sim [0] Não: ")
            if cadastrar_outro == "0":
                MenuPrincipal()
            
class CadastroUsuario:
    def __init__(self):
        self.arquivo = "usuarios.csv"  # Nome do arquivo de usuários
        self.lista_usuarios = []  # Inicializa a lista de usuários vazia

    def imprimir(self):
        cabecalho = Cabecalho()
        cabecalho.imprimir()
        print("CADASTRO DE USUÁRIOS".center(80))
        self.carregar_usuarios()
        self.cadastrar_usuario()

    def carregar_usuarios(self):
        # Verifica se o arquivo existe
        if os.path.exists(self.arquivo):
            with open(self.arquivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                # Carrega os dados existentes para a lista de usuários
                self.lista_usuarios = [row for row in reader]
        else:
            self.lista_usuarios = []

    def adicionar_usuario(self):
        usuario = {
            'nome': input("Digite o nome do usuário: "),
            'telefone': input("Digite o telefone do usuário: "),
            'email': input("Digite o email do usuário: "),
            'id_aluno': input("Digite o ID do aluno: ")
        }
        
        # Verifica se todas as chaves estão presentes e adiciona valores padrão caso contrário
        for chave in ['nome', 'telefone', 'email', 'id_aluno']:
            if chave not in usuario:
                usuario[chave] = ''

        self.lista_usuarios.append(usuario)

    def salvar_arquivo(self):
        with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['nome', 'telefone', 'email', 'id_aluno'])
            writer.writeheader()
            writer.writerows(self.lista_usuarios)

    def cadastrar_usuario(self):
        while True:
            self.adicionar_usuario()

            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho = Cabecalho()
            cabecalho.imprimir()
            print("CADASTRO DE USUÁRIOS".center(80))
            print("Usuário cadastrado:")
            for chave, valor in self.lista_usuarios[-1].items():
                print(f"{chave.capitalize()}: {valor}")

            final = input("\nAs informações digitadas estão corretas? [1] Sim [2] Não [0] Sair: ")
            if final == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                MenuPrincipal()
            elif final == "1":
                self.salvar_arquivo()  # Salva o usuário apenas quando as informações estiverem corretas
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho.imprimir()
                print("\n\n\nUsuário cadastrado com sucesso!\n")
                time.sleep(2)
            elif final == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho.imprimir()
                print("\n\n\nCadastre o usuário novamente!\n")
                time.sleep(2)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho = Cabecalho()
                cabecalho.imprimir()
                print("\n\n\nOpção Inválida!\n")
                time.sleep(2)

            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho = Cabecalho()
            cabecalho.imprimir()
            print("CADASTRO DE USUÁRIOS".center(80))
            cadastrar_outro = input("\nDeseja cadastrar outro usuário? [1] Sim [0] Não: ")
            if cadastrar_outro == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                MenuPrincipal()  # Retorna ao menu principal

class Emprestimo:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.arquivo = "LivrosEmprestados.csv"  # Nome do arquivo de usuários
        self.lista_livros = []  # Inicializa a lista de usuários vazia
    
    def exibir_menu(self):
        cabecalho = Cabecalho()
        cabecalho.imprimir()
        print("EMPRÉSTIMO DE LIVRO".center(80))
        # Receba o título do livro como entrada
        titulo_livro = input("Digite o título ou ISBN do livro que deseja emprestar: ")
        nome_aluno = input("Digite o Nome ou ID do Aluno: ")
        self.verificar_usuario(nome_aluno)
        self.realizar_emprestimo(titulo_livro, nome_aluno)  # Passando nome_aluno como argumento

    def realizar_emprestimo(self, titulo, nome_aluno):  # Adicionando nome_aluno como parâmetro
        # Verifica se o livro está disponível para empréstimo
        livro_encontrado = False
        with open('livros.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['titulo'].lower() == titulo.lower() or row['isbn'] == titulo.lower():
                    print("\nLivro encontrado:")
                    print("Título:", row['titulo'])
                    print("Autor:", row['autor'])
                    print("ISBN:", row['isbn'])
                    print("Genero:", row['genero'])
                    print("Ano publicação:", row['ano_publicacao'])
                    print("Quantidade Disponível:", row['quantidade_disponivel'])
                    livro_encontrado = True
                    confirmacao = input("\nDeseja emprestar este livro? [1] Sim [2] Não: ")
                    if confirmacao == '1':
                        # Atualiza o arquivo CSV para refletir o empréstimo
                        quantidade_disponivel = int(row['quantidade_disponivel'])
                        if quantidade_disponivel < 1:
                            print("Erro: Não há livros disponíveis para empréstimo.")
                            return
                        quantidade_disponivel -= 1    
                        row['quantidade_disponivel'] = str(quantidade_disponivel)
                        with open('livros.csv', mode='r+', newline='', encoding='utf-8') as file_write:
                            writer = csv.DictWriter(file_write, fieldnames=reader.fieldnames)
                            writer.writeheader()
                            writer.writerow(row)
                        
                            print("Empréstimo do livro realizado com sucesso!")
                            with open('LivrosEmprestados.csv', mode='a', newline='', encoding='utf-8') as file_emprestados:
                                writer_emprestados = csv.writer(file_emprestados)
                                writer_emprestados.writerow([row['titulo'], row['isbn'], nome_aluno, row['autor'], row['genero']])

                            emprestimo_outro = input("\nDeseja realizar outro empréstimo? S/N: ").upper()
                            if emprestimo_outro == "S":
                                Emprestimo()
                            elif emprestimo_outro == "N":
                                MenuPrincipal()
                            else:
                                print("Opção Inválida!")
                                MenuPrincipal()
                      
                    elif confirmacao == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        cabecalho = Cabecalho()
                        cabecalho.imprimir()
                        print("EMPRÉSTIMO DE LIVRO".center(80))
                        MenuPrincipal()
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        cabecalho = Cabecalho()
                        cabecalho.imprimir()
                        print("EMPRÉSTIMO DE LIVRO".center(80))
                        print("\n\n\nOpção inválida!")
                        time.sleep(2)
                        cabecalho = Cabecalho()
                        cabecalho.imprimir()
                        Emprestimo()
            if not livro_encontrado:
                print("\nLivro não encontrado.\n")
                print("Não foi possível realizar o empréstimo do livro. Tente Novamente.")
                animacao = ""
                for _ in range(10):  # Definindo 10 iterações para a animação
                    animacao += "."  # Adiciona um ponto à string
                    print(animacao, end="\r")  # Imprime a string sem nova linha
                    time.sleep(0.5)  # Aguardar 0.5 segundos entre cada ponto
                print()  # Adicionar nova linha após a animação
                Emprestimo()

    def verificar_usuario(self, nome):
        usuario_encontrado = False
        with open('usuarios.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Nome,Telefone,email,ID do aluno
            for row in reader:
                if row['nome'].lower() == nome.lower() or row['id_aluno'] == nome.lower():
                    print("\nAluno encontrado:")
                    print("Nome:", row['nome'])
                    print("Telefone:", row['telefone'])
                    print("E-mail:", row['email'])
                    print("ID do Aluno:", row['id_aluno'])
                    usuario_encontrado = True
                    
            if not usuario_encontrado:
                print("\nAluno não encontrado...\n") 
                print("Não foi possível realizar o empréstimo do livro. Tente Novamente.")
                animacao = ""
                for _ in range(10):  # Definindo 10 iterações para a animação
                    animacao += "."  # Adiciona um ponto à string
                    print(animacao, end="\r")  # Imprime a string sem nova linha
                    time.sleep(0.5)  # Aguardar 0.5 segundos entre cada ponto
                print()  # Adicionar nova linha após a animação
                Emprestimo()

class Devolucao:

    def imprimir(self):
        cabecalho = Cabecalho()
        cabecalho.imprimir()
        print("DEVOLUÇÃO DE LIVRO".center(80))
        # Receba o título do livro como entrada
        titulo_livro = input("Digite o título ou ISBN do livro que deseja devolver: ")
        self.realizar_devolucao(titulo_livro)

    def realizar_devolucao(self, titulo):
        # Verifica se o livro está emprestado
        livro_emprestado = False
        livros_emprestados = []
        with open('LivrosEmprestados.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == titulo.lower() or row[1] == titulo.lower():
                    livro_emprestado = True
                else:
                    livros_emprestados.append(row)
        
        if livro_emprestado:
            with open('LivrosEmprestados.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(livros_emprestados)
            print("Devolução do livro realizada com sucesso!")
            time.sleep(2)
            with open('home.py', 'r', encoding='utf-8') as arquivo:
                # Lendo o conteúdo do arquivo
                codigo = arquivo.read()
                # Executando o código lido do arquivo
                exec(codigo)
            os.system('cls' if os.name == 'nt' else 'clear')
            # Incrementa a quantidade disponível na planilha livros.csv
            with open('livros.csv', mode='r+', newline='', encoding='utf-8') as file_livros:
                reader_livros = csv.DictReader(file_livros)
                livros = list(reader_livros)
                for row in livros:
                    if row['titulo'].lower() == titulo.lower() or row['isbn'] == titulo.lower():
                        row['quantidade_disponivel'] = str(int(row['quantidade_disponivel']) + 1)
                        break
                file_livros.seek(0)
                writer_livros = csv.DictWriter(file_livros, fieldnames=reader_livros.fieldnames)
                writer_livros.writeheader()
                writer_livros.writerows(livros)
            outra_devolucao = input('Deseja fazer outra devolução? S/N: ').upper()
            if outra_devolucao == "S":
                with open('DevolucaoLivro.py', 'r', encoding='utf-8') as arquivo:
                    # Lendo o conteúdo do arquivo
                    codigo = arquivo.read()
                    # Executando o código lido do arquivo
                    exec(codigo)
            elif outra_devolucao == "N":
                with open('home.py', 'r', encoding='utf-8') as arquivo:
                    # Lendo o conteúdo do arquivo
                    codigo = arquivo.read()
                    # Executando o código lido do arquivo
                    exec(codigo)
        else:
            print("Livro não está emprestado ou não foi encontrado na lista de empréstimos.")

class Relatorio:
    
    def imprimir(self):
        cabecalho = Cabecalho()
        cabecalho.imprimir()
        print("RELATÓRIO".center(80))
        print("\n[1] Usuário Cadastrados")
        print("[2] Livros Disponíveis")
        print("[3] Livro Emprestados")
        print("[0] Retornar ao menu prinipal\n")
        
        
        opcao = (input("Digite para o número acessar a planilha: "))
        print()
        if opcao == "0":
            MenuPrincipal()
        elif opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho = Cabecalho()
            cabecalho.imprimir()
            self.exibir_planilha('usuarios.csv')
            voltar = input('\n\n[1] Retornar ao menu anterior\n[2] Sair\n\nDigite um numero: ')
            if voltar == '1':
                relatorio = Relatorio()  # Instancie a classe Relatorio
                relatorio.imprimir()  # Chame o método para exibir o menu
            elif voltar == '2':
                MenuPrincipal()
            else:
                print("Opção Inválida!")
                relatorio = Relatorio()  # Instancie a classe Relatorio
                relatorio.imprimir()  # Chame o método para exibir o menu
                print()
        elif opcao == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.exibir_planilha('livros.csv')
            voltar = input('\n\n[1] Retornar ao menu anterior\n[2] Sair\n\nDigite um numero: ')
            if voltar == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                relatorio = Relatorio()  # Instancie a classe Relatorio
                relatorio.imprimir()  # Chame o método para exibir o menu
                print()
            elif voltar == '2':
                os.system('cls' if os.name == 'nt' else 'clear')

                MenuPrincipal()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção Inválida!")
                relatorio = Relatorio()  # Instancie a classe Relatorio
                relatorio.imprimir()  # Chame o método para exibir o menu
                print()            
        elif opcao == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.exibir_planilha('LivrosEmprestados.csv')
            voltar = input('\n\n[1] Retornar ao menu anterior\n[2] Sair\n\nDigite um numero: ')
            if voltar == '1':
                relatorio = Relatorio()  # Instancie a classe Relatorio
                relatorio.imprimir()  # Chame o método para exibir o menu
                print()
            elif voltar == '2':
                MenuPrincipal()
            else:
                print("Opção Inválida!")
                relatorio = Relatorio()  # Instancie a classe Relatorio
                relatorio.imprimir()  # Chame o método para exibir o menu
                print()
        else:
            print("Opção Inválida!")
            relatorio = Relatorio()  # Instancie a classe Relatorio
            relatorio.imprimir()  # Chame o método para exibir o menu

    def exibir_planilha(self, nome_arquivo):
        # Abrir o arquivo CSV
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

class MenuPrincipal:
    def __init__(self):
        cabecalho = Cabecalho()
        cabecalho.imprimir()
        print("início".center(80))
        print(
            "[1] Pesquisa\n"
            "[2] Cadastrar Livros\n"
            "[3] Cadastrar Usuário\n"
            "[4] Empréstimo de Livros\n"
            "[5] Devolução de Livros\n"
            "[6] Relatório\n[0] Sair\n"
        )

        opcao = input("Digite o número e clique em enter: ")
        if opcao == "1":
            pesquisa = Pesquisa()
            pesquisa.imprimir()
        elif opcao == "2":
            livro = CadastroLivro()  # Instanciar a classe CadastroLivro
            livro.imprimir()  # Chamar o método imprimir de CadastroLivro
        elif opcao == "3":
            usuario = CadastroUsuario()
            usuario.imprimir()
        elif opcao == "4":  # Adicione esta parte para iniciar o menu de empréstimo
            emprestimo = Emprestimo()
            emprestimo.imprimir()
        elif opcao == "5":
            devolucao = Devolucao()
            devolucao.imprimir()
        elif opcao == "6":
            relatorio = Relatorio()
            relatorio.imprimir()
        elif opcao == "0":
            encerramento = Encerramento()
            encerramento.encerrar()
MenuPrincipal()
