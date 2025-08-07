try:
    print ("Este programa mostra a quantidade de números palíndromos entre 10(Dez) e 100.000(Cem mil).")
    print("")
    #Define o início do intervalo. 
    inicio = 10
    #Ocfim do intervalo.
    fim = 100000
    #Começa com uma variável para contar os números palíndromos encontrados. Inicializando por 0.
    contador = 0
    #Define a variável numero como o valor de início 10. Vamos usar essa variável para iterar pelos números no intervalo.
    numero = inicio

    #Inicia um laço que vai rodar enquanto "numero" for menor ou igual a fim. Ou seja, vai verificar todos os números de 10 a 100000.
    while numero <= fim:
        #Armazena o número atual, para comparação no final.
        original = numero
        #Variável que irá guardar o número ao contrário (ex: de 121 para 121, de 123 para 321).
        invertido = 0
        #Variável auxiliar usada para separar o número dígito por dígito.
        sep_digito = numero
    
        #Um laço que roda enquanto sep_digito for maior que zero.
        while sep_digito > 0:
            #Extrai o último dígito do número.
            digito = sep_digito % 10
            #Adiciona esse dígito ao final do número invertido.
            invertido = invertido * 10 + digito
            #Remove o último dígito de "sep_digito".
            sep_digito = sep_digito // 10

        #Após inverter o número, comparamos se ele é igual ao original.
        if original == invertido:
            #Se for palíndromo, soma 1 ao contador.
            contador = contador + 1
        #Incrementa a variável numero em 1, para verificar o próximo número no próximo ciclo do while.
        numero = numero + 1
    #Exibe a quantidade de números palíndromos.
    print("Quantidade de números palíndromos entre", inicio, "e", fim,"são: ",contador)

#Caso ocorra algum erro durante a execução de qualquer parte do código acima.
except Exception as e:
    #Imprime uma mensagem de erro mostrando o que aconteceu.
    print("Ocorreu um erro durante a execução:", e)
