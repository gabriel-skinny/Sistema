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

  usuarioModelo = {
    "id": id,
    "nome": "",
    "email": "",
    "senha": ""
  }

  usuarioModelo["nome"] = dadosDoUsuario[0]
  usuarioModelo["email"] = dadosDoUsuario[1]
  usuarioModelo["senha"] = dadosDoUsuario[2]

  usuarios.append(usuarioModelo)


def main():
  sair = False
  countId = 0

  while(not(sair)):
    tarefaEscolhida = intercaoInicial()

    

    if (tarefaEscolhida == 1) :
      print("função de cadastro")

    if (tarefaEscolhida == 2) :
      print("função de cadastro")

    if (tarefaEscolhida == 3) :
      print("função de cadastro")
    if (tarefaEscolhida == 4) :
      print("função de cadastro")
    if (tarefaEscolhida == 5):
      print("\n\nVoce saiu do sistema!!\n\n")
      sair = True
    
    countId =+ 1


if __name__ == "__main__":
  main()
