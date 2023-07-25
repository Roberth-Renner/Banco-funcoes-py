import textwrap


# FUNÇÃO MENU 

def funcao_menu():
     
     menu = f"""
     ==============Menu===============
     [a]\tSaque
     [b]\tDepositar
     [c]\tExtrato
     [d]\tCriar Usuário
     [e]\tCriar conta
     [f]\tListar contas
     [g]\tsair
     =================================\n"""

     return input(textwrap.dedent(menu))


# FUNÇÃO DE SAQUE 

def funcao_saque(*,valorSaque, extrato, saldo, quantSaques, limiteDeSaques, limiteValorSaque):
        

        if valorSaque <= limiteValorSaque and len(quantSaques) < limiteDeSaques and saldo > 0 and valorSaque > 0 and valorSaque <= saldo:

            saldo -= valorSaque
            quantSaques += [range(3)]
            extrato += f"Saque:\tR$ {valorSaque:.2f}\n"

            print(len(quantSaques))

            print("\nSaque realizado com sucesso!")
            
            return saldo, extrato
        
        else:
            
            print("\nDesculpe interação nao permitida, fique atento ao limite de saques diarios, limite de valor de saque e ao seu saldo.")

            return saldo, extrato


# FUNÇÃO DE DEPÓSITO 

def funcao_deposito(valorDeposito, extrato, saldo, /):
     
     if valorDeposito > 0 :
          
          saldo += valorDeposito
          extrato += f"Deposito:\tR$ {valorDeposito:.2f}\n"

          print("\nDepósito realizado com sucesso!")

          return saldo, extrato
     
     else:
          
          print("\nDesculpe mas ocorreu um erro, verifique se o valor é negativo.")
          return saldo, extrato

    
# FUNÇÃO HISTÓRICO DE EXTRATO

def funcao_extrato(saldo, /, *, extrato):
     
     print("\n---------------- EXTRATO ----------------")
     print("Ainda não foram realizadas movimentações.\n" if not extrato else extrato)
     print(f"\nSaldo:\t\tR$ {saldo:.2f}")
     print("-----------------------------------------\n")


     return saldo, extrato


# FUNÇÃO PARA CADASTRAR UM USÚARIO

def funcao_usuario(usuarios_cadastrados): 

    usuario_cpf = input("\nDigite seu cpf (somente número): ")
    filtro = filtrar_usuarios(usuario_cpf, usuarios_cadastrados)

    if filtro:
        print("\n@@@ Já existe usuário com este CPF! @@@\n")
        return
    
    usuario_nome = input("\nDigite seu nome completo: ")
    usuario_data = input("\nDigite sua data de nascimento(dd-mm-aaaa): ")
    usuario_endereco = input("\nDigite seu endereco (logradouro, nro - bairro - cidade/sigSla estado): ")

    usuarios_cadastrados.append({"CPF" : usuario_cpf, "Nome" : usuario_nome, "Data de nascimento" : usuario_data, "Endereço" : usuario_endereco})
    
    print("\n@@@ Usuário cadastrado com sucesso! @@@\n")


# FILTRAR USUARIOS POR CPF ÚNICO

def filtrar_usuarios(cpf, usuarios_cadastrados):

     usuarios_filtrados = [usuario for usuario in usuarios_cadastrados if usuario["CPF"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None


# CRIAR CONTAS

def criar_conta(numero_conta, usuarios, angencia):

     cpf = input("\nInforme o seu cpf: ")
     usuario = filtrar_usuarios(cpf, usuarios)

     if usuario:

          print("\n@@@ Conta registrada com sucesso! @@@")

          return {"angencia" : angencia, "numero da conta" : numero_conta, "usuario" : usuario}
     
     print("\n@@@ Conta já cadastrada por um usuario, ou ainda não cadastrou um usuario ! @@@")


# LISTANDO USUARIOS COM "FOR"

def listar_contas(contas):
     
     if len(contas) == 0:
          
          print("\nNão há contas para listarmos!")

     else:
          
          for conta in contas:
               
               informacoes = f"""
               Agência:\t{conta["angencia"]}
               C/c:    \t{conta["numero da conta"]}
               Titular:\t{conta["usuario"]}
               """
               print("=" * 150)
               print(textwrap.dedent(informacoes))


# MAIN PROGAMA

def main():
     LIMITE_SAQUES = 3
     AGENCIA = "0001"

     saldo = 0
     limite = 500
     extrato = ""
     quantSaques = []
     opcao = ""
     usuarios = []
     contas = []

     while opcao != "g":

          opcao = funcao_menu()

          if opcao == "a":

               valor = float(input("\nDigite o valor de saque : "))
               saldo, extrato = funcao_saque(
                    valorSaque= valor,
                    extrato= extrato,
                    saldo= saldo,
                    quantSaques= quantSaques,
                    limiteDeSaques= LIMITE_SAQUES,
                    limiteValorSaque= limite
               )

          elif opcao == "b":

               valor = float(input("\nDigite o valor do depósito : "))
               saldo, extrato = funcao_deposito(
                     valor,
                    extrato,
                    saldo
               )

          elif opcao == "c":

               saldo, extrato = funcao_extrato(
                    saldo,
                    extrato= extrato
               )

          elif opcao == "d":

               funcao_usuario(usuarios)

          elif opcao == "e":

               numero_conta = len(contas) + 1

               conta = criar_conta(numero_conta , usuarios, AGENCIA)

               if conta:

                    contas.append(conta)

          elif opcao == "f":

               listar_contas(contas)

          elif opcao == "g":

               print("\nTchau, obrigado pelo contato!")

          else :

               print("\nQualquer outro caractere que não esteja no menu irá ocasionar este erro!")


main()









