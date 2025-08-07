#Dicionário para guardar os dados: CPF e lista de MACs.
cadastro = {}  #Armazena todos os dados cadastrados (CPF como chave, lista de MACs como valor).

#Função para limpar CPF, removendo pontos e traços.
def limpar_cpf(cpf):
    return cpf.replace(".", "").replace("-", "")  #Remove "." e "-" do CPF para manter apenas os números.

#Função para validar se o CPF tem 11 números.
def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()  #Verifica se o CPF tem 11 dígitos e se todos são números.

#Função para validar MAC Address no formato XX:XX:XX:XX:XX:XX
def validar_mac(mac):
    partes = mac.upper().split(":")  # Transforma em maiúsculo e divide o MAC pelos ":".
    # Verifica se tem 6 partes e se cada parte tem 2 caracteres válidos (0-9 ou A-F).
    return len(partes) == 6 and all(len(p) == 2 and all(c in "0123456789ABCDEF" for c in p) for p in partes)

#Função que pede o CPF ao usuário, limpa e valida.
def obter_cpf():
    try:
        cpf = limpar_cpf(input("Digite o CPF: "))  # Pede o CPF e remove pontos e traços.
        if not validar_cpf(cpf):  #Verifica se o CPF é válido.
            raise ValueError("CPF inválido!")  #Se não for, lança um erro.
        return cpf  #Retorna o CPF válido.
    except Exception as e:  #Captura qualquer erro ocorrido.
        print(e)  #Exibe a mensagem de erro.
        return None  #Retorna None caso CPF inválido.

# Função para cadastrar um CPF.
def adicionar_cpf():
    cpf = obter_cpf()  #Pede e valida o CPF.
    if cpf:  # Se CPF válido.
        if cpf in cadastro:  #Verifica se CPF já existe no cadastro.
            print("CPF já cadastrado.")  # Informa que já existe.
        else:
            cadastro[cpf] = []  #Adiciona o CPF com uma lista vazia de MACs.
            print("CPF cadastrado com sucesso.")  # Confirma o cadastro.

#Função para adicionar um MAC Address a um CPF.
def adicionar_mac():
    cpf = obter_cpf()  #Pede e valida o CPF.
    if cpf:  #Se CPF válido.
        try:
            if cpf not in cadastro:  #Se CPF não cadastrado.
                raise KeyError("CPF não encontrado.")  #Lança erro de chave (CPF não encontrado).
            mac = input("Digite o MAC (XX:XX:XX:XX:XX:XX): ").upper()  #Pede o MAC e converte para maiúsculo.
            if not validar_mac(mac):  #Valida o formato do MAC.
                raise ValueError("MAC inválido. Use apenas letras A-F e números.")  #Lança erro se MAC inválido.
            if mac in cadastro[cpf]:  #Verifica se o MAC já foi cadastrado para o CPF.
                print("MAC já cadastrado.")  #Informa que já existe.
            else:
                cadastro[cpf].append(mac)  #Adiciona o MAC na lista do CPF.
                print("MAC cadastrado com sucesso.")  #Confirma o cadastro.
        except (KeyError, ValueError) as e:  #Captura erros de CPF não encontrado ou MAC inválido.
            print(e)  #Exibe o erro.

#Função para remover um MAC de um CPF.
def remover_mac():
    cpf = obter_cpf()  #Pede e valida o CPF.
    if cpf:  #Se CPF válido.
        try:
            if cpf not in cadastro:  #Verifica se o CPF existe.
                raise KeyError("CPF não encontrado.")  #Lança erro de CPF não encontrado.
            mac = input("Digite o MAC a remover: ").upper()  #Pede o MAC e converte para maiúsculo.
            cadastro[cpf].remove(mac)  #Tenta remover o MAC da lista do CPF.
            print("MAC removido.")  #Confirma a remoção.
        except KeyError as e:  #CPF não cadastrado.
            print(e)  #Exibe o erro.
        except ValueError:  #Caso o MAC não esteja na lista.
            print("MAC não encontrado para este CPF.")  #Informa que o MAC não foi achado.

#Função para listar todos os CPFs cadastrados.
def listar_cpfs():
    if cadastro:  #Verifica se há CPFs cadastrados.
        print("CPFs cadastrados:")  #Cabeçalho da lista.
        for cpf in sorted(cadastro):  #Percorre os CPFs em ordem crescente.
            print(cpf)  #Exibe o CPF.
    else:
        print("Nenhum CPF cadastrado.")  # Informa se não houver CPFs.

#Função para listar todos os MACs de um CPF específico.
def listar_macs():
    cpf = obter_cpf()  #Pede e valida o CPF.
    if cpf:  #Se CPF válido.
        try:
            macs = cadastro[cpf]  #Obtém a lista de MACs do CPF.
            if macs:  #Verifica se há MACs cadastrados.
                print(f"MACs do CPF {cpf}:")  # Cabeçalho.
                for mac in macs:  #Percorre e exibe cada MAC.
                    print(mac)
            else:
                print("Nenhum MAC cadastrado para esse CPF.")  #Informa se a lista estiver vazia.
        except KeyError:
            print("CPF não encontrado.")  #Erro caso o CPF não exista.

#Função para buscar se um MAC existe em um CPF.
def buscar_mac():
    cpf = obter_cpf()  #Pede e valida o CPF.
    if cpf:
        try:
            mac = input("Digite o MAC a buscar: ").upper()  #Pede o MAC e converte para maiúsculo.
            if mac in cadastro[cpf]:  #Verifica se o MAC existe na lista do CPF.
                print(f"MAC {mac} está cadastrado para o CPF {cpf}.")  #Informa se achou.
            else:
                print("MAC não encontrado para esse CPF.")  #Informa se não achou.
        except KeyError:
            print("CPF não encontrado.")  #CPF não cadastrado.

#Função para salvar os dados no arquivo.
def salvar_dados():
    try:
        with open("cadastro.txt", "w") as arquivo:  #Abre/cria arquivo "cadastro.txt" para escrita.
            for cpf, macs in cadastro.items():  #Percorre cada CPF e sua lista de MACs.
                arquivo.write(f"{cpf};{','.join(macs)}\n")  #Escreve no formato CPF;MAC1,MAC2,...
        print("Dados salvos.")  #Confirma que os dados foram salvos.
    except Exception as e:  #Captura qualquer erro.
        print(f"Erro ao salvar dados: {e}")  #Exibe a mensagem de erro.

#Função para carregar os dados do arquivo.
def carregar_dados():
    global cadastro  #Declara que vamos alterar a variável global cadastro.
    try:
        with open("cadastro.txt", "r") as arquivo:  #Abre o arquivo para leitura.
            for linha in arquivo:  #Percorre cada linha do arquivo.
                cpf, *macs = linha.strip().split(";")  # Separa o CPF dos MACs.
                #Se houver MACs, separa pela vírgula, senão atribui lista vazia.
                cadastro[cpf] = macs[0].split(",") if macs and macs[0] else []
        print("Dados carregados.")  #Confirma carregamento.
    except FileNotFoundError:
        print("Arquivo de cadastro não encontrado.")  #Informa se o arquivo não existir.
    except Exception as e:  #Qualquer outro erro.
        print(f"Erro ao carregar dados: {e}")

#Função principal do menu do programa.
def menu():
    #Dicionário de opções do menu, ligando as letras às funções correspondentes.
    opcoes = {
        "a": adicionar_cpf,
        "b": adicionar_mac,
        "c": remover_mac,
        "d": listar_cpfs,
        "e": listar_macs,
        "f": buscar_mac,
        "g": salvar_dados,
        "h": carregar_dados,
    }

    while True:  #Loop infinito para exibir o menu até que o usuário escolha sair.
        print("\n--- MENU ---")
        print("a) - Cadastrar CPF")
        print("b) - Adicionar MAC")
        print("c) - Remover MAC")
        print("d) - Listar CPFs")
        print("e) - Listar MACs")
        print("f) - Buscar MAC")
        print("g) - Salvar dados")
        print("h) - Carregar dados")
        print("q) - Sair")  #Opção de sair.

        escolha = input("Escolha uma opção: ").lower()  #Pede escolha e converte para minúsculo.
        try:
            if escolha == "q":  #Se a escolha for "q", encerra o programa.
                print("Saindo do programa.")
                break
            elif escolha in opcoes:  #Se a escolha estiver nas opções disponíveis.
                opcoes[escolha]()  #Executa a função correspondente.
            else:
                raise ValueError("Opção inválida.")  #Se não for válida, lança erro.
        except Exception as e:  #Captura qualquer erro.
            print(e)  #Exibe a mensagem de erro.

menu()  #Inicia o programa chamando a função menu().
 
