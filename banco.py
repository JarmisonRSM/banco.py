class Conta:

    cliente = "Jarmison Ramos"
    agencia = "0069"
    conta = "45789"
    cpf = "130.730.704-28"
    profissao = "Policial Militar"
    saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        self.extrato(valor)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.saque(-valor)
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato(-valor)
        else:
            print("Saldo insuficiente.")

    def pagar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato(-valor)
        else:
            print("Saldo insuficiente.")

    def especial(self, valor):
        self.saldo += valor
        self.extrato(valor)

    def menu(self):
        print('-' * 30)
        print(f"     BANCO COCADA")
        print(f"     MENU DO CAIXA")
        print(f"CLIENTE: {self.cliente}")
        print(f"CPF: {self.cpf}")
        print(f"PROFISSÃO: {self.profissao}")
        print(f"AGÊNCIA:{self.agencia} CONTA:{self.conta}", -2)
        print("-" * 30)
        print("Opções:")
        print("1 - Extrato")
        print("2 - Depósito")
        print("3 - Saque")
        print("4 - Transferencia")
        print("5 - Pagar")
        print("6 - Crédito especial")
        print("7 - Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            self.extrato()

        elif opcao == "2":
            valor = float(input("Digite o valor que deseja depositar R$: "))
            print("-" * 34)
            print("DEPÓSITO REALIZADO COM SUCESSO")
            print("-" * 34)
            self.depositar(valor)

        elif opcao == "3":
            valor = float(input("Qual a quantia do saque: "))
            print("Valor total do saque é de R$: ", valor)
            self.sacar(valor)

        elif opcao == "4":
            print('1 - TRANFERÊNCIA ENTRE CONTAS CORRENTES ')
            print('2 - TRANSFERÊNCIA ENTRE CONTA CORRENTE E POUPANÇA')
            print('3 - TRANFERÊNCIA ENTRE CONTAS POUPANÇAS')
            contas = input('Insira o modelo de transferência desejado: ')

            if contas == '1':
                print('TRANFERÊNCIA ENTRE CONTAS CORRENTES')
                valor = float(input("Digite o valor da transferência: "))
                banco = input("qual o Banco que deseja Transferir COD: ")
                agencia = int(input("Digite a Agência:  "))
                conta = int(input("Digite a conta: "))
                digito = int(input("digite o digito da conta: "))

                print("-" * 34)
                print(f"     DADOS DA TRANSFERÊNCIA")
                print("-" * 34)
                print("Agencia: ", agencia)
                print("Conta: ", conta)
                print("Digito: ", digito)
                print("Valor: ", valor)
                print("-" * 34)
                print("TRANSFERENCIA REALIZADA COM SUCESSO!")
                print("-" * 34)
                self.transferir(valor)

            elif contas == '2':
                print('TRANSFERÊNCIA ENTRE CONTA CORRENTE E POUPANÇA')
                valor = float(input("Digite o valor da transferência: "))
                banco = input("qual o Banco que deseja Transferir COD: ")
                agencia = int(input("Digite a Agência:  "))
                conta = int(input("Digite a conta: "))
                digito = int(input("digite o digito da conta: "))

                print("-" * 34)
                print(f"     DADOS DA TRANSFERÊNCIA")
                print("-" * 34)
                print("Agencia: ", agencia)
                print("Conta: ", conta)
                print("Digito: ", digito)
                print("Valor: ", valor)
                print("\n\nAnalisando a transação....")
                print("-" * 34)
                print("TRANSFERENCIA REALIZADA COM SUCESSO!!!!!!")
                print("-" * 34)
                self.transferir(valor)
            elif contas == '3':
                print('TRANFERÊNCIA ENTRE CONTAS POUPANÇAS')
                valor = float(input("Digite o valor da transferência: "))
                banco = input("qual o Banco que deseja Transferir COD: ")
                agencia = int(input("Digite a Agência:  "))
                conta = int(input("Digite a conta: "))
                digito = int(input("digite o digito da conta: "))

                print("-" * 34)
                print(f"     DADOS DA TRANSFERÊNCIA")
                print("-" * 34)
                print("Agencia: ", agencia)
                print("Conta: ", conta)
                print("Digito: ", digito)
                print("Valor: ", valor)
                print("\n\nAnalisando a transação....")
                print("-" * 34)
                print("TRANSFERENCIA REALIZADA COM SUCESSO!!!!!!")
                print("-" * 34)
                self.transferir(valor)

        elif opcao == "5":
            valor = float(input("Digite o valor do pagamento: "))
            print("\n\nAnalisando a transação....")
            print("-[ Lendo Código de Barras ]-")
            print("Valor total do Pagamento é de R$: ", valor)
            print("-" * 34)
            print("PAGAMENTO REALIZADO COM SUCESSO!")
            print("-" * 34)
            self.pagar(valor)
        elif opcao == "6":
            print("Bem vindo Jarmison, crédito especial pre-aprovado")
            valor = int(
                input("Digite o Valor do crédito especial desejado R$"))
            print("Crédito especial concedido")
            print("-" * 34)
            print(f"     DADOS DO CRÉDITO ESPECIAL")
            print("-" * 34)
            print("Valor Atual", valor)
            print("-" * 34)
            print("Volte sempre ao BANCO COCADA!")
            print("-" * 34)
            self.especial(valor)

        elif opcao == "7":
            exit()

    def extrato(self, ultimo=0):
        print()
        print("-" * 40)
        print(f"       BANCO COCADA")
        print(f"                EXTRATO           ")
        print("-" * 40)
        print(f"CLIENTE: {self.cliente}")
        print(f"AGÊNCIA:{self.agencia}:CONTA {self.conta}", -2)
        print("-" * 40)
        print("LANÇAMENTOS")
        if ultimo > 0:
            print(f" DEPÓSITO ATM |     CRÉDITO {ultimo:.2F} ")
        print("              |                |")
        print("              |                |")
        print("-" * 40)
        print(f"                        SALDO: R$ {self.saldo:.2F}")
        print("-" * 40)
        print("             FIM DO EXTRATO				  ")
        print('-' * 40)
        aperte = input("Aperte ENTER para retornar ao MENU ou (X) para sair: ")
        if aperte == "X" or aperte == "x":
            exit()
        else:
            self.menu()

    def saque(self, ultimo=0):
        print()
        print("-" * 40)
        print(f"       BANCO COCADA")
        print(f"                SAQUE           ")
        print("-" * 40)
        print(f"CLIENTE: {self.cliente}")
        print(f"AGÊNCIA:{self.agencia}:CONTA {self.conta}", -2)
        print("-" * 40)
        print("LANÇAMENTOS")
        if ultimo > 0:
            print(f" DEPÓSITO ATM |     SAQUE {ultimo:.3F} ")
        print("              |                |")
        print("              |                |")
        print("-" * 40)
        print(f"                  SALDO: R$ {self.saldo:.2F}")
        print("-" * 40)
        print("     SAQUE REALIZADO COM SUCESSO             ")
        print("-" * 40)
        aperte = input("Aperte ENTER para retornar ao MENU ou (X) para sair: ")
        if aperte == "X" or aperte == "x":
            exit()
        else:
            self.menu()

    def transferencia(self, ultimo=0):
        print()
        print("-" * 40)
        print(f"       BANCO COCADA")
        print(f"                TRANSFERÊNCIA           ")
        print("-" * 40)
        print(f"CLIENTE: {self.cliente}")
        print(f"AGÊNCIA:{self.agencia}:CONTA {self.conta}", -2)
        print("-" * 40)
        print("LANÇAMENTOS")
        if ultimo > 0:
            print(f" DEPÓSITO ATM |     SAQUE {ultimo:.3F} ")
        print("              |                |")
        print("              |                |")
        print("-" * 40)
        print(f"                  SALDO: R$ {self.saldo:.2F}")
        print("-" * 40)
        print("     TRANSFERÊNCIA REALIZADA COM SUCESSO             ")
        print("-" * 40)
        aperte = input("Aperte ENTER para retornar ao MENU ou (X) para sair: ")
        if aperte == "X" or aperte == "x":
            exit()
        else:
            self.menu()

    def pagamento(self, ultimo=0):
        print()
        print("-" * 40)
        print(f"       BANCO COCADA")
        print(f"                PAGAMENTO           ")
        print("-" * 40)
        print(f"CLIENTE: {self.cliente}")
        print(f"AGÊNCIA:{self.agencia}:CONTA {self.conta}", -2)
        print("-" * 40)
        print("LANÇAMENTOS")
        if ultimo > 0:
            print(f" DEPÓSITO ATM |     SAQUE {ultimo:.3F} ")
        print("              |                |")
        print("              |                |")
        print("-" * 40)
        print(f"                  SALDO: R$ {self.saldo:.2F}")
        print("-" * 40)
        print("     PAGAMENTO REALIZADO COM SUCESSO             ")
        print("-" * 40)
        aperte = input("ENTER para MENU ou (X) para sair: ")
        if aperte == "X" or aperte == "x":
            exit()
        else:
            self.menu()

    def especial(self, ultimo=0):
        print()
        print("-" * 40)
        print(f"       BANCO COCADA")
        print(f"                EXTRATO           ")
        print("-" * 40)
        print(f"CLIENTE: {self.cliente}")
        print(f"AGÊNCIA:{self.agencia}:CONTA {self.conta}", -2)
        print("-" * 40)
        print("LANÇAMENTOS")
        if ultimo > 0:
            print(f" DEPÓSITO ATM |     CRÉDITO {ultimo:.2F} ")
        print("              |                |")
        print("              |                |")
        print("-" * 40)
        print(f"                        SALDO: R$ {self.saldo:.2F}")
        print("-" * 40)
        print("             FIM DO EXTRATO				  ")
        print('-' * 40)
        aperte = input("Aperte ENTER para retornar ao MENU ou (X) para sair: ")
        if aperte == "X" or aperte == "x":
            exit()
        else:
            self.menu()


pessoa = Conta()

while True:
    pessoa.menu()
