import os
#import locale
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
114:["Beltrano",13000],
115:["Teste",-1532]
}
while True:
    #os.system('cls')
    #valor = 1768
    #locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
    #valor = locale.currency(valor,grouping=True, symbol=True)
    #print(valor)
    opt=input('''
    Escolha uma opção:
    \033[92m[1]\033[0m Buscar Conta
    \033[92m[2]\033[0m Relatório
    \033[92m[3]\033[0m Inclusão
    \033[92m[4]\033[0m UPDATE         
    \033[92m[5]\033[0m DELETE
    \033[92m[6]\033[0m SAIR
    Opção = ''')
    if opt not in ["1","2","3","4","5","6"]:
        os.system('cls')
        print ("\033[91mOPÇÃO INVÁLIDA\033[0m")
        #input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
        #os.system('cls')
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
          saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')
          if(dados[1] > 0):
           print (f'\nConta:{chave:^5} Nome:{dados[0]:^10} Saldo Conta: \033[92m{saldo_formatado}\033[0m')
          else:
           print (f'\nConta:{chave:^5} Nome:{dados[0]:^10} Saldo Conta: \033[91m{saldo_formatado}\033[0m') 
        else:
          #print(cont)
          cont +=1
          if((cont > len(RP))):
            print('\033[91mConta não encontra ou não existe\033[0m')
     input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
     os.system('cls')
    elif opt=="2":
      os.system('cls')
      for chave,dados in RP.items():
         saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')
         if(dados[1] > 0):
          print (f'Conta:{chave:^5} Nome:{dados[0]:^10} Saldo Conta: \033[92m{saldo_formatado}\033[0m')
         else:
          print (f'Conta:{chave:^5} Nome:{dados[0]:^10} Saldo Conta: \033[91m{saldo_formatado}\033[0m') 
      input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
      os.system('cls')
    elif opt=="3":
      os.system('cls')
      while True:
        ultima_chave = list(RP.items())[-1]
        matr= ultima_chave[0] + 1
        #print(matr)
        matr = int(matr)
        #while True:
        #  matr=input("entre com a matricula: ")
        #  os.system('cls')
        #  if(matr.isdigit()):
        #    matr = int(matr)
        #    break
        #  else:
        #    os.system('cls')
        #    print('\033[91mValor invalido!!\033[0m')
        #    print('Digite novamente !!\n')
        if (matr not in RP ):
        #if (matr.isdigit() and matr not in RP ):
            while True:
                  print(f'{matr:^10}')
                  nome=input("\nentre com o nome: ").strip()
                  os.system('cls')
                  if not nome or not all(part.isalpha() for part in nome.split()):
                    os.system('cls')
                    print('\033[91mValor invalido!!\033[0m')
                    print('Digite novamente\n')
                  else: 
                    break 
            while True:
              #os.system('cls')
              print (f'\n{matr:^10} {nome:^10}')
              sal=input("\nentre com o salario: ")
              os.system('cls')
              # Tente converter nm para um número inteiro
              #os.system('cls')
              try:
                  sal = int(sal)
              except ValueError:
                  pass  # Se falhar, nmN permanece None

              if (type(sal) != int):
                os.system('cls')
                print('\033[91mValor invalido!!\033[0m')
                print('Digite novamente')
              else:
                sal = float(sal) 
                break

            RP[matr]=[nome,sal]
            #print(RP[matr][0])
            saldo_formatado = "R$ {:,.2f}".format(sal).replace('.', 'X').replace(',', '.').replace('X', ',')
            print ('\n\033[92mRegistro Adicionado com sucesso:\033[0m')
            if(sal > 0):
              print (f'Conta:{matr:^5} Nome:{RP[matr][0]:^10} Saldo Conta: \033[92m{saldo_formatado}\033[0m')
            else:
              print (f'Conta:{matr:^5} Nome:{RP[matr][0]:^10} Saldo Conta: \033[91m{saldo_formatado}\033[0m') 
            input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
            os.system('cls')
        else:
          print('\033[93mMatricula já esxite!!\033[0m')
          input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
          break
        break
    
    elif opt=="4":
      os.system('cls')
      nmN = 0
      cont = 1
      print("\033[93mSessão Update\033[0m")
      nm=input("Entre com o nome ou chave a ser pesquisado: ")
      os.system('cls')
      if nm.isdigit():
         nmN = int(nm)
      for chave,dados in RP.items():
         #print(type(chave))
         if (nm in dados[0] or nmN == chave):
           #saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')
           #if(dados[1] > 0):
           # print (f'Conta:{chave:^5} Nome:{dados[0]:^10} Saldo Conta: \033[92m{saldo_formatado}\033[0m')
           #else:
           # print (f'Conta:{chave:^5} Nome:{dados[0]:^10} Saldo Conta: \033[91m{saldo_formatado}\033[0m') 
           while True:
              saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')
              if(dados[1] > 0):
               print (f'Conta:{chave:^5} Nome: {dados[0]:^10} Saldo Conta: \033[92m{saldo_formatado}\033[0m')
              else:
               print (f'Conta:{chave:^5} Nome: {dados[0]:^10} Saldo Conta: \033[91m{saldo_formatado}\033[0m') 
              opt2=input('''
    Oque deseja alterar ?
    [1] Usuário Conta
    [2] Saldo da Conta
    [3] SAIR        
    Opção = ''')
              os.system('cls')
              if opt2 not in ["1","2","3"]:
                os.system('cls')
                print("\033[91mOPÇÃO INVÁLIDA\033[0m")  # Texto amarelo
                #input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
              elif opt2 =="1":
                while True:
                  print(dados[0])
                  nome=input("entre com o novo nome: ").strip()
                  if not nome or not all(part.isalpha() for part in nome.split()):
                    os.system('cls')
                    print('\033[91mValor invalido!!\033[0m')
                    print('Digite novamente\n')
                  else: 
                    break
                print("\n\033[92mTroca do nome realizada de:\033[0m "+dados[0]+" \033[92mpara\033[0m "+nome)
                dados[0] = nome
                input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
                os.system('cls')
              elif opt2 =='2':
                os.system('cls')
                saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')

                if(dados[1] > 0):
                  print (f'Conta:{chave:^5} Nome: {dados[0]:^10} Saldo Conta: \033[92m{saldo_formatado}\033[0m')
                else:
                  print (f'Conta:{chave:^5} Nome: {dados[0]:^10} Saldo Conta: \033[91m{saldo_formatado}\033[0m') 
                while True:
                  saldo= input('Digite o novo Saldo: ')
                  # Tente converter nm para um número inteiro
                  try:
                      saldo = int(saldo)
                  except ValueError:
                      pass  # Se falhar, nmN permanece None
                    
                  if (type(saldo) != int):
                    os.system('cls')
                    print('\033[91mValor invalido!!\033[0m')
                    print('Digite novamente\n')
                  else:
                    saldo = float(saldo) 
                    break

                mostrar = str("R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ','))
                mostrarSaldo = str("R$ {:,.2f}".format(saldo).replace('.', 'X').replace(',', '.').replace('X', ','))
                
                print("\033[92mTroca do saldo realizada de:\033[0m "+mostrar+" para "+mostrarSaldo)
                dados[1] = saldo
                input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
                os.system('cls')
              elif opt2 =="3":
                print('\n\033[91mOperação cancelada!!\033[0m')
                input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
                break
         else:
           cont +=1
           if((cont > len(RP))):
             print('Conta não encontra ou não existe')
             input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
      os.system('cls')
    elif opt =='5':
      os.system('cls')
      print("\033[91mSessão DELETE\033[0m")
      while True:
          nx= input('Entre com a \033[93mchave\033[0m a ser pesquisado: ')
          os.system('cls')
          # Tente converter nm para um número inteiro
          try:
              nx = int(nx)
          except ValueError:
              pass  # Se falhar, nmN permanece None
            
          if (type(nx) != int):
            os.system('cls')
            print('\033[91mValor invalido!!\033[0m')
            print('Digite novamente\n')
          else:
            nx = (nx) 
            break
      chaveDel = []
      contx = 1   
      for chave,dados in RP.items():
         #print(type(chave))
         if (nx == chave):
           saldo_formatado = "R$ {:,.2f}".format(dados[1]).replace('.', 'X').replace(',', '.').replace('X', ',')
           
           while saldo_formatado != '':
            if(dados[1] > 0):
              print (f'Conta:{chave:^5} Nome:{dados[0]:^10} Saldo Conta: \033[92m{saldo_formatado}\033[0m')
            else:
             print (f'Conta:{chave:^5} Nome:{dados[0]:^10} Saldo Conta: \033[91m{saldo_formatado}\033[0m') 
            #print (f'{chave:^10} {dados[0]:^10} \033[92m{saldo_formatado:^10}\033[0m')
            print('\nDeseja deletar os dados acima ?')
            opt = input('Digite: S (PARA DELETAR) ou N (PARA CANCELAR): ') 
            if opt not in ["s","S","n","N"]:
                os.system('cls')
                print("\033[91mVALOR INVÁLIDA\033[0m\n")  # Texto amarelo
                #input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')
            elif opt in['s','S']:
              chaveDel.append(chave)
              #print(chaveDel)
              print('\n\033[91mDados deletados com sucesso!!\033[0m')
              input ("\033[93mPressione Enter para Finalizar\033[0m")
              os.system('cls')
              break
            elif opt in['N','n']:
               print('\n\033[91mOperação cancelada!!\033[0m')
               input ("\033[93mPressione Enter para Finalizar\033[0m")
               os.system('cls')
               break
         else:
            contx +=1
            if((contx > len(RP))):
              print('\n\033[91mConta não encontra ou não existe\033[0m')
              input ("\033[93mPressione Enter para Finalizar\033[0m")
              os.system('cls')
      # Deletar as chaves após a iteração
      for chave in chaveDel:
          del RP[chave]
       
      #input ('\n\033[93mPRESSIONE ENTER PARA VOLTAR AO MENU\033[0m')         
    elif opt=="6":
      input ("\033[93mPressione Enter para Finalizar\033[0m")
      os.system('cls')
      break