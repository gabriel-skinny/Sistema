usuarios = []


def intercaoInicial():
    print("\nQual processo vc deseja fazer: \n")
    print("[1] - Cadastrar usuario")
    print("[2] - Exibir usuario")
    print("[3] - Remover usuario")
    print("[4] - Editar usuario por e-mail")
    print("[5] - Sair\n")

    return int(input())


def inputsCadastroUsuario():
    print("\n\nCadastro de usuario")
    print("Digite o nome desejado: \n")
    nome = input()
    print("Digite o e-mail desejado: \n")
    email = input()
    print("Digite a senha desejado: \n")
    senha = input()

    return [nome, email, senha]


def cadastro(id):
    dadosDoUsuario = inputsCadastroUsuario()

    usuarioModelo = {"id": id, "nome": "", "email": "", "senha": ""}

    usuarioModelo["nome"] = dadosDoUsuario[0]
    usuarioModelo["email"] = dadosDoUsuario[1]
    usuarioModelo["senha"] = dadosDoUsuario[2]

    usuarios.append(usuarioModelo)

    print("\n\nUSUARIO CADASTRO COM SUCESSO!!\n")


def inputsLista():
    print("\n\n\nVoce deseja listar usuarios usando qual filtro")
    print("[1] - Listar todos por ordem de criacao")
    print("[2] - Listar todos por ordem alfabetica")
    print("[3] - Listar apenas um usuario por nome")
    print("[4] - VOLTAR\n\n")

    return int(input())


def forEachUsuariosPrintar(lista, length):
    for index in range(length):
        print("Nome: {}:\n".format(lista[index]["nome"]))
        print("E-mail: {}\n\n".format(lista[index]["email"]))


def forEachUsuariosCondicao(condicao, tipo):
    length = len(usuarios)

    for index in range(length):
        if usuarios[index][tipo] == condicao:
            print("\n\nUsuario escolhido foi {}:\n".format(condicao))
            print("Nome: {}".format(usuarios[index]["nome"]))
            print("\nE-mail: {} \n\n\n".format(usuarios[index]["email"]))

            return index
        else:
            print("ERRO!!")
            print("NENHUM USUARIO FOI ENCONTRADO")


def listar():
    sair = False

    while not (sair):
        escolhaDeFiltro = inputsLista()

        if escolhaDeFiltro == 1:
            length = len(usuarios)

            print("\n\nUsuarios: \n")
            for index in range(length):
                print("Nome: {}:\n".format(usuarios[index]["nome"]))
                print("E-mail: {}\n\n".format(usuarios[index]["email"]))

        if escolhaDeFiltro == 2:
            sortedUsuarios = usuarios
            sortedUsuarios.sort(key=get_nome)

            length = len(sortedUsuarios)

            print("\n\nUsuarios em ordem alfabetica: \n")
            for index in range(length):
                print("Nome: {}:\n".format(sortedUsuarios[index]["nome"]))
                print("E-mail: {}\n\n".format(sortedUsuarios[index]["email"]))

        if escolhaDeFiltro == 3:
            print("Digite um nome")
            nome = input()
            length = len(usuarios)

            for index in range(length):
                if usuarios[index]["nome"] == nome:
                    print("\n\nUsuario escolhido foi {}:\n".format(nome))
                    print("Nome: {}".format(nome))
                    print("E-mail: {} \n\n\n".format(usuarios[index]["email"]))

        if escolhaDeFiltro == 4:
            sair = True


def main():
    sair = False
    countId = 0

    while not (sair):
        tarefaEscolhida = intercaoInicial()

        if tarefaEscolhida == 1:
            cadastro(countId)

        if tarefaEscolhida == 2:
            listar()

        if tarefaEscolhida == 3:
            print("função de remover")
        if tarefaEscolhida == 4:
            print("função de cadastro")
        if tarefaEscolhida == 5:
            print("\n\nVoce saiu do sistema!!\n\n")
            sair = True

        countId = +1


if __name__ == "__main__":
    main()
