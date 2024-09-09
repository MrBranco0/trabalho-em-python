while True:  # Inicia um loop infinito
    idade = int(input("Digite sua idade: "))  # Solicita e lê a idade do usuário
    
    if idade >= 18 and idade < 20:  # Verifica se a idade está entre 18 e 19 anos
        print("Você é adolescente")  # Mensagem para adolescentes
    elif idade >= 20 and idade < 30:  # Verifica se a idade está entre 20 e 29 anos
        print("Você é um jovem adulto")  # Mensagem para jovens adultos
    elif idade >= 30 and idade < 400:  # Verifica se a idade está entre 30 e 399 anos
        print("Você é um adulto")  # Mensagem para adultos
    else:  # Caso a idade não se encaixe em nenhuma das faixas anteriores
        print("Erro: valor não encontrado...")  # Mensagem de erro
    
    # Pergunta ao usuário se deseja continuar ou sair
    continuar = input("Deseja continuar? (s/n): ").strip().lower()  # Lê a resposta do usuário, removendo espaços em branco e convertendo para minúsculas
    if continuar != 's':  # Se a resposta não for 's' (sim), encerra o loop
        print("Programa encerrado.")  # Mensagem indicando que o programa está sendo encerrado
        break  # Sai do loop infinito
