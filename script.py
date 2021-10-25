usuarios = []


def get_nome(usuarios):
    return usuarios.get("nome")


def get_id(usuarios):
    return usuarios.get("id")


def forEachUsuariosCondicao(condicao, tipo):
    length = len(usuarios)

    for index in range(length):
        if usuarios[index][tipo] == condicao:
            print("\n\nUsuario escolhido foi {}:\n".format(condicao))
            print("Nome: {}".format(usuarios[index]["nome"]))
            print("\nE-mail: {} \n\n\n".format(usuarios[index]["email"]))

            return index

    return -1


def forEachUsuariosPrintar(lista):
    for usuario in lista:
        print("Nome: {}:\n".format(usuario["nome"]))
        print("E-mail: {}\n\n".format(usuario["email"]))


def procurarUsuarioEmail(email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return True

    return False


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

    usuarioEncontrado = procurarUsuarioEmail(dadosDoUsuario[1])
    if usuarioEncontrado:
        print("\nERRO!")
        print("Esse email ja foi utilizado digite outro se quiser criar um usuario\n")
        return

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


def listar():
    sair = False

    while not (sair):
        escolhaDeFiltro = inputsLista()

        if escolhaDeFiltro == 1:
            ordemDeCriacaoUsuarios = usuarios
            ordemDeCriacaoUsuarios.sort(key=get_id)

            print("\n\nUsuarios: \n")
            forEachUsuariosPrintar(ordemDeCriacaoUsuarios)

        if escolhaDeFiltro == 2:
            sortedUsuarios = usuarios
            sortedUsuarios.sort(key=get_nome)

            print("\n\nUsuarios em ordem alfabetica: \n")

            forEachUsuariosPrintar(sortedUsuarios)

        if escolhaDeFiltro == 3:
            print("Digite um nome")
            nome = input()

            indexUsuario = forEachUsuariosCondicao(nome, "nome")

            if indexUsuario == -1:
                print("\n\nERROR")
                print("USUARIO NAO ENCONTRADO!\n")

        if escolhaDeFiltro == 4:
            sair = True


def inputsRemover():
    print("\nDigite o nome do usuario que deseja remover\n")
    return input()


def remover():
    nomedoUsuario = inputsRemover()

    usuarioIndex = forEachUsuariosCondicao(nomedoUsuario, "nome")
    usuarios.pop(usuarioIndex)
    print("\nUsuario removido com sucesso!")


def editar():
    print("Digite o E-mail")
    email = input()

    usuarioIndex = forEachUsuariosCondicao(email, "email")

    if usuarioIndex == -1:
        print("\nERRO!")
        print("USUARIO NAO ENCONTRADO\n\n")
        return

    print("Digite o novo nome: \n")
    nome = input()
    usuarios[usuarioIndex]["nome"] = nome

    print("\nNome alterado com sucesso!! \n\n")


def intercaoInicial():
    print("\nQual processo vc deseja fazer: \n")
    print("[1] - Cadastrar usuario")
    print("[2] - Exibir usuario")
    print("[3] - Remover usuario")
    print("[4] - Editar usuario por e-mail")
    print("[5] - Sair\n")

    return int(input())


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
            remover()

        if tarefaEscolhida == 4:
            editar()

        if tarefaEscolhida == 5:
            print("\n\nVoce saiu do sistema!!\n\n")
            sair = True

        countId = +1


if __name__ == "__main__":
    main()
