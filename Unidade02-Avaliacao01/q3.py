import random  # Importa o módulo random, que permite escolher elementos aleatórios

#Lista de palavras válidas que podem ser sorteadas ou usadas como palpite. Tupla contendo palavras válidas de 5 letras. O jogador só pode digitar palavras que estejam aqui.
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

#Códigos ANSI para colorir o texto no terminal:
VERDE = '\033[42m\033[30m'    #Fundo verde com letra preta → letra correta no lugar certo.
AMARELO = '\033[43m\033[30m'  #Fundo amarelo com letra preta → letra correta no lugar errado.
CINZA = '\033[47m\033[30m'    #Fundo branco (cinza claro) com letra preta → letra errada.
RESET = '\033[0m'             #Código para resetar as cores após cada letra.

#Função para pintar o palpite com base na comparação com a palavra correta.
def pintar(palpite, alvo):
    resultado = [""] * 5         #Cria uma lista com 5 posições vazias para guardar os resultados coloridos.
    usado = [False] * 5          #Controla quais letras da palavra "alvo" já foram usadas na comparação (evita marcar duas vezes).

    #Primeiro, verifica letras certas no lugar certo (cor verde)
    for i in range(5):
        if palpite[i] == alvo[i]:                   #Se a letra está correta e na posição certa.
            resultado[i] = VERDE + palpite[i] + RESET
            usado[i] = True                          #Marca que essa letra da palavra correta já foi usada.
        else:
            resultado[i] = None                     # Temporariamente marca como "ainda não definida cor para sua posição.

    #Depois, verifica letras certas no lugar errado (amarelo) e letras erradas (cinza).
    for i in range(5):
        if resultado[i] is not None:                #Se já está colorido (verde), pula.
            continue
        achou = False                               #Variável de controle para saber se encontrou a letra.
        for j in range(5):
            if not usado[j] and palpite[i] == alvo[j]:  #Se ainda não usou essa posição e a letra do palpite está na palavra correta.
                achou = True                          #Marca que encontrou.
                usado[j] = True                      #Marca que essa posição foi usada.
                break
        if achou:
            resultado[i] = AMARELO + palpite[i] + RESET  #Letra certa no lugar errado.
        else:
            resultado[i] = CINZA + palpite[i] + RESET    #Letra não está na palavra.

    return ''.join(resultado)  #Junta a lista de letras coloridas em uma única string e retorna.

#Sorteia aleatoriamente duas palavras diferentes da lista.
resposta1, resposta2 = random.sample(palavras, 2)

#Cria um conjunto vazio para armazenar as palavras que o jogador acertar.
descobertas = set()

#Define o número máximo de tentativas.
tentativas = 7

#Mostra mensagem inicial do jogo.
print("Bem-vindo ao Termo Dueto!")
print("Descubra as 2 palavras de 5 letras. Você tem 7 tentativas!\n")

#Início do laço principal do jogo (de 1 até 7), que controla as rodadas de tentativas.
for rodada in range(1, tentativas + 1):
    #Início do bloco de tratamento de erros.
    try:
        # Solicita que o usuário digite um palpite. Recebe a palavra do jogador e coloca em maiúsculo.
        palpite = input(f"Tentativa {rodada}: ").strip().upper()

        # Verifica se a palavra tem 5 letras e está na lista de palavras permitidas.
        if len(palpite) != 5 or palpite not in palavras:
            print(" Palavra inválida. Tente novamente.\n")   #Mensagem de erro.
            continue  #Volta ao início da próxima rodada sem gastar tentativa.

        #Verifica se a palavra digitada é uma das palavras sorteadas.
        if palpite == resposta1 or palpite == resposta2:
            if palpite not in descobertas:  #Verifica se já foi descoberta.
                descobertas.add(palpite)    #Adiciona ao conjunto de descobertas.
                print("Você acertou uma palavra:", palpite)  #Informa acerto ao jogador.
            else:
                print("Palavra já descoberta.\n")  #Informa que a palavra já foi descoberta anteriormente.
        else:
            #Se o palpite estiver errado, mostra dicas coloridas comparando com as duas palavras corretas.
            print(" Palavra 1:", pintar(palpite, resposta1))
            print(" Palavra 2:", pintar(palpite, resposta2))
            print()

        #Se as duas palavras forem descobertas, o jogo termina com parabéns.
        if len(descobertas) == 2:
            print("Parabéns! Você descobriu as duas palavras!")
            break  # Encerra o laço de tentativas
    except Exception as e:     #Captura qualquer erro que acontecer durante a execução.
       
        print("Ocorreu um erro:", e, "Tente novamente.")  #Mostra o erro sem travar o programa.

#Se o jogador não acertou as duas palavras após 7 tentativas, mostra o fim de jogo.
else:
    print("Suas tentativas acabaram.")
    print("As palavras corretas eram:", resposta1, "e", resposta2)
