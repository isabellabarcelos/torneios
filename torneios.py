def proximo():
  mi = input("\n\nO que deseja fazer? \n\n\t1- Voltar ao menu principal \n\t2 - Encerrar programa\n")
    
  if mi.isnumeric:
    mi = int(mi)
    if mi == 1:
      MenuPrincipal()
    elif mi == 2:
      print("\nTenha um bom dia!")
      exit()
    else:
      print("Opção inválida. Por favor digite uma opção válida.")
      proximo()
      
  else:
    print("Opção inválida. Por favor digite uma opção válida.")
    proximo()
def decoracao ():
    print("\n\n---------------------------------------\n\n")
def impdict(d):
 print("\n")
 for key in d:
    print (key + ": " + d[key])
def continuar(objt):
     
    c = input(f"Deseja continuar a {objt}? \n\n 1 - sim \n 2 - não\n\n Escolha uma opção: ")
    
    if c.isnumeric():
        c = int(c)
        if c == 1:
          return True
              
        elif c == 2:
          return False
        
        else: 
          invalid()
          continuar("adicionando faixas")
    else: 
      invalid()
      continuar("adicionando faixas")
def invalid ():
  print("\nOpção inválida. Por favor, digite uma opção válida.")
def MenuPrincipal():

  decoracao()
  print("\tMENU PRINCIPAL")
  decoracao()

  print("\n\t 1 - Menu de torneios")
  print("\n\t 2 - Menu de lutadores")
  print("\n\t 3 - Criar torneio aleatório")
  print("\n\t 4 - Encerrar programa")

  while True:
    
    principal = input("\n\n\t Escolha uma opção: ")
    if principal.isnumeric():

      principal = int(principal)

      if principal == 1:

          MenuDeTorneios()
          break

      elif principal == 2:
          
          MenuDeLutadores()
          break

      elif principal == 3:

          CriarAleatorio()
          break
      elif principal == 4:
          print("Tenha um bom dia!")
          quit()
      
      else:
        invalid()


    else:
        invalid()
def MenuDeTorneios():

  decoracao()
  print("\tMENU DE TORNEIOS")
  decoracao()
  print("\n\t 1 - Criar torneio")
  print("\n\t 2 - Inscrever lutador")
  print("\n\t 3 - Ver torneios existentes")
  print("\n\t 4 - Ver ranking de torneio")
  print("\n\t 5 - Ver lutadores inscritos em torneio ")
  print("\n\t 6 - Realizar luta")
  print("\n\t 7 - Retornar ao menu principal")
  print("\n\t 8 - Encerrar programa")

  while True:
    
    mtorneio = input("\n\n\t Escolha uma opção: ")

    if mtorneio.isnumeric():

      mtorneio = int(mtorneio)

      if  mtorneio == 1:

          CriarTorneio()
          break

      elif mtorneio == 2:

          InscreverLutador()
          break

      elif mtorneio == 3:

        VerTorneios()
        break
          
      elif mtorneio == 4:
          Ranking()
          break

      elif mtorneio == 5:
          LutadoresInscritos()
          break
      
      elif mtorneio == 6:
          RealizarLuta()
          break
      
      elif mtorneio == 7:
          MenuPrincipal()
          break
     
      elif mtorneio == 8:
          print("Tenha um bom dia!")
          quit()

      else:
        invalid()


    else:
        invalid()
def MenuDeLutadores():

  decoracao()
  print("\tMENU DE LUTADORES")
  decoracao()

  print("\n\t 1 - Cadastrar lutador")
  print("\n\t 2 - Ver lutadores")
  print("\n\t 3 - Descrição completa de um lutador")
  print("\n\t 4 - Retornar ao menu principal")
  

  while True:
    
    mlutadores = input("\n\n\t Escolha uma opção: ")

    if mlutadores.isnumeric():

      mlutadores= int(mlutadores)

      if  mlutadores == 1:

          CadastrarLutador()
          break

      elif mlutadores == 2:
          
          VerLutadores();
          break

      elif mlutadores == 3:
          VerDetalhesDoLutador()
      
      elif mlutadores == 4:
        MenuPrincipal()
      
      else:
        invalid()


    else:
        invalid()
def CriarAleatorio():
  decoracao()
  print("\tCRIAR TORNEIO ALEATÓRIO")
  decoracao()
  print("A desenvolver")
  proximo()
def CriarTorneio():

  decoracao()
  print("\tCRIAR TORNEIO")
  decoracao()
  num = 1  
  nome = input("Nome: ")
  artemarcial = input("Arte marcial: ")
  faixas = []
  pesos = []
  print("Insira as faixas que deseja adicionar ao torneio:\n") 
  num = 1
  for i in range(0,11,1):
    print(f"{i+1} - {Faixas[i]}")
  while True:

    faixa1 = input(f"{num}°: faixa:")
    if faixa1.isnumeric():
      faixa1 = int(faixa1)  
      if faixa1 in range(0,10):
        num += 1
        faixas.append(Faixas[faixa1-1])
      else:
        invalid()
    else:
      invalid()

    if not continuar('adicionando faixas'):
      break
    
  num = 1
  print("Insira as categorias de peso que deseja adicionar ao torneio")
  for i in range(0,10,1):
    print(f"{i+1} - {Pesos[i]}")
  while True:

    peso1 = input(f"{num}° categoria: ")
    if peso1.isnumeric():
      peso1 = int(peso1)  
      if peso1 in range(0,9):
        num += 1
        pesos.append(Pesos[peso1-1])

      else:
        invalid()
    else:
      invalid()


    if not continuar('adicionando categorias'):
      break  

  torneio = {"Nome":nome, "Arte marcial":artemarcial, "Faixas":faixas, "Pesos":pesos}
  torneios.append(torneio)
  print("Torneio criado com sucesso!")
 
  proximo()
def CadastrarLutador():
  decoracao()
  print("\tCADASTRAR LUTADOR")
  decoracao()

  nome = input("Nome: ")
  idade = input("Idade: ")
  peso = input("Peso: ")
  forca = input("Força: ")
  faixa = input("Faixa: ")
  artemarcial = input("Arte marcial: ")
  
  lutador = {"Nome": nome, "Idade": idade, "Peso": peso, "forca": forca, "Faixa": faixa, "Arte marcial": artemarcial}
  lutadores.append(lutador)
  print("\nCadastro concluído com sucesso!")
  proximo()
def VerLutadores():

  decoracao()
  print("\tLUTADORES")
  decoracao()

  for y in range(0, len(lutadores), 1):
    print(f"{y+1} - {lutadores[y]['Nome']}")
  if len(lutadores) == 0:
    print("Ainda não exitem lutadores.")
  
  proximo()
def VerDetalhesDoLutador():
  decoracao()
  print("\tDESCRIÇÃO DO LUTADOR")
  decoracao()
  
  d = input("Digite o nome do lutador que deseja a descrição completa: ")
  for i in range(len(lutadores)):
    if d == lutadores[i]["Nome"]:
      impdict(lutadores[i])  
    else:
      print("Lutador não exitente.")
      while True:
        w = input("O que deseja fazer?\n\t1 - Voltar ao menu principal\n\t2 - Tentar novamente\n")
        if w.isnumeric():
          w = int(w)
          if w == 1:
            MenuPrincipal()
            break
          elif w == 2:
            VerDetalhesDoLutador()
            break
          else:
            print("Opção inválida.")
        
        else:
          print("Opção inválida.")
  proximo()
def VerTorneios():
  
  decoracao()
  print("\tTORNEIOS")
  decoracao()

  for y in range(0, len(torneios), 1):
    print(f"{y+1} - {torneios[y]['Nome']}")
  if len(torneios) == 0:
    print("Ainda não exitem torneios.")
        
  proximo()
def InscreverLutador():
  #a terminar
  decoracao()
  print("\tINSCREVER LUTADOR")
  decoracao()
  
  for i in range(len(lutadores)):
      print(f'\t{i+1} - {lutadores[i]["Nome"]}')
  
  b = 0 
  if len(lutadores) == 0:
    print("Ainda não existem lutadores.")
    b= 1;  
  
  elif len(torneios) == 0:
    print("Ainda não existem torneios.")  
    b = 1
    
  else:
    
    w = input("\nSelecione um lutador: ")
    
    if w.isnumeric():
      print(len(lutadores))
      w = int(w)
      if w in range(0, len(lutadores)+1):
        escolhido = [lutadores[w-1]]
        print(f'Você escolheu o {lutadores[w-1]["Nome"]}.')

      else:
        invalid()
        proximo()
        

    else: 
      invalid()
      proximo()

    c = 0
    for i in range(1, len(torneios)+1):
      if torneios[i-1]["Arte marcial"] == lutadores[w-1]["Arte marcial"]:
        print(f'{i+1} - {torneios[i-1]["Nome"]}')
        c+=1
    if c == 0 and b == 0:
      print('Não existem torneios para a arte marcial para a arte marcial do lutador.')
      proximo()

    #else:
    # c = 0
    #  for i in range(1, len(torneios[w-1]['faixas'])+1):
    #    if lutadores[i-1]['Faixa'] == torneios[w-1]["Faixa"]:
    #      c+=1
    #  if c == 0 and b == 0:
    #    print('A faixa não está adequada para este torneio.')
    #    proximo()
    else:
      torneios.append(lutadores[w-1])
      print("Lutador adicionado com sucesso!")

  proximo()    
def RealizarLuta():
  decoracao()
  print("\tLUTA")
  decoracao()
  print("A desenvolver")
  proximo()
def LutadoresInscritos():  
  decoracao()
  print("\tLUTADORES INSCRITOS")
  decoracao()
  #a terminar
  d = input("Digite o nome do torneio que deseja a lista de lutadores: ")
  for i in range(len(torneios)):
    if d == torneios[i]["Nome"]:
        print(torneios[i])
    else:
      print("Torneio não exitente.")
      while True:
        w = input("O que deseja fazer?\n\t1 - Voltar ao menu principal\n\t2 - Tentar novamente\n")
        if w.isnumeric():
          w = int(w)
          if w == 1:
            MenuPrincipal()
            break
          elif w == 2:
            VerDetalhesDoLutador()
            break
          else:
            print("Opção inválida.")
        
        else:
          print("Opção inválida.")
  proximo()


  decoracao()
  print("A desenvolver")
  proximo()
def Ranking():
  decoracao()
  print("\tRANKING")
  decoracao()
  print("A desenvolver")
  proximo()


Pesos = [[40,50], [50, 60], [60,70], [80,90], [90, 100], [100,110], [110,120], [120, 130], [130, 140],[140,150]]
Faixas = ['branca','cinza','amarela','laranja','verde','roxo', 'azul','marrom','vermelha','preta','livre']
torneios = []
lutadores = []
MenuPrincipal()

