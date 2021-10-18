usuarios = []

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