import os
#International Bank KeKell 
print("""     
██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██╗         ██████╗  █████╗ ███╗   ██╗██╗  ██╗    ██╗  ██╗███████╗██╗  ██╗███████╗██╗     ██╗     
██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔══██╗██║         ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ██║ ██╔╝██╔════╝██║ ██╔╝██╔════╝██║     ██║     
██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔██╗ ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║███████║██║         ██████╔╝███████║██╔██╗ ██║█████╔╝     █████╔╝ █████╗  █████╔╝ █████╗  ██║     ██║     
██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║██╔══██║██║         ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗     ██╔═██╗ ██╔══╝  ██╔═██╗ ██╔══╝  ██║     ██║     
██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚████║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║██║  ██║███████╗    ██████╔╝██║  ██║██║ ╚████║██║  ██╗    ██║  ██╗███████╗██║  ██╗███████╗███████╗███████╗
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝                                                                                                                                                                                                                                                                                                                                                                                               
""")
### definindo o Dicionário: Matricula: Nome, Salário 
RP={
111:["Luiz",15000],
112:["Fulano",14500],
113:["Sicrano",11000],
114:["Beltrano",13000]
}
while True:
    #os.system('cls')
    opt=input('''
    Escolha uma opção:
    [1] Buscar Conta
    [2] Relatório
    [3] Inclusão
    [4] SAIR
    [5] UPDATE         
    Opção = ''')
    if opt not in ["1","2","3","4","5"]:
        os.system('cls')
        print ("OPÇÃO INVÁLIDA")
        input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
    elif opt=="1":
     os.system('cls')
     nmN = 0
     cont = 1
     nm=input("Entre com o nome a ser pesquisado: ")
     if nm.isdigit():
        nmN = int(nm)
     for chave,dados in RP.items():
        #print(type(chave))
        if (nm in dados[0] or nmN == chave):
          print (f'{chave:^10} {dados[0]:^10} R${dados[1]:^10.2f}')
        else:
          #print(cont)
          cont +=1
          if((cont > len(RP))):
            print('Conta não encontra ou não existe')
     input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
    elif opt=="2":
      os.system('cls')
      for chave,dados in RP.items():
         saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')
         print (f'{chave:^10} {dados[0]:^10} {saldo_formatado}')
      input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
    elif opt=="3":
      os.system('cls')
      while True:
        while True:
          matr=input("entre com a matricula: ")
          if(matr.isdigit()):
            matr = int(matr)
            break
          else:
            os.system('cls')
            print('Valor invalido !!')
            print('Digite novamente !!\n')
        if (matr not in RP ):
        #if (matr.isdigit() and matr not in RP ):
            while True:
              nm=input("entre com o nome: ")
              if nm.isdigit():
                print('Valor invalido!!')
                print('Digite novamente')
              else: 
                break 
            while True:
              sal=input("entre com o salario: ")
              # Tente converter nm para um número inteiro
              try:
                  sal = int(sal)
              except ValueError:
                  pass  # Se falhar, nmN permanece None

              if (type(sal) != int):
                os.system('cls')
                print('Valor invalido!!')
                print('Digite novamente\n')
              else:
                sal = float(sal) 
                break

            RP[matr]=[nm,sal]
            print ('Registro Adicionado')
            input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
        else:
          print('Matricula já esxite!!')
          input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
          break
        break
    elif opt=="4":
      input ("Pressione Enter para Finalizar")
      break
    
    elif opt=="5":
      os.system('cls')
      nmN = 0
      cont = 1
      print("Sessão Update")
      nm=input("Entre com o nome ou chave a ser pesquisado: ")
      os.system('cls')
      if nm.isdigit():
         nmN = int(nm)
      for chave,dados in RP.items():
         #print(type(chave))
         if (nm in dados[0] or nmN == chave):
           saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')
           print (f'{chave:^10} {dados[0]:^10} {saldo_formatado}')
           while True:
              opt2=input('''
    Oque deseja alterar ?
    [1] Usuário Conta
    [2] Saldo da Conta
    [3] SAIR        
    Opção = ''')
              if opt2 not in ["1","2","3"]:
                os.system('cls')
                print ("OPÇÃO INVÁLIDA")
                input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
              elif opt2 =="1":
                os.system('cls')
                print(dados[0])
                nome= input('Digite novo nome do usuário: ')
                print("Troca do nome realizada de: "+dados[0]+" para "+nome)
                dados[0] = nome
                input ('\nPRESSIONE ENTER PARA VOLTAR AO MENU')
              elif opt2 =='2':
                os.system('cls')
                saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')
                print (f'{chave:^10} {dados[0]:^10} {saldo_formatado}\n')

                while True:
                  saldo= input('Digite o novo Saldo: ')
                  # Tente converter nm para um número inteiro
                  try:
                      saldo = int(saldo)
                  except ValueError:
                      pass  # Se falhar, nmN permanece None
                    
                  if (type(saldo) != int):
                    os.system('cls')
                    print('Valor invalido!!')
                    print('Digite novamente\n')
                  else:
                    saldo = float(saldo) 
                    break

                mostrar = str("R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ','))
                mostrarSaldo = str("R$ {:,.2f}".format(saldo).replace('.', 'X').replace(',', '.').replace('X', ','))
                print("Troca do saldo realizada de: "+mostrar+" para "+mostrarSaldo)
                dados[1] = saldo
                input ('\nPRESSIONE ENTER PARA VOLTAR AO MENU')
              elif opt2 =="3":
                #input ("Pressione Enter para Finalizar")
                break
         else:
           cont +=1
           if((cont > len(RP))):
             print('Conta não encontra ou não existe')

      input ('PRESSIONE ENTER PARA VOLTAR AO MENU')
      os.system('cls')
