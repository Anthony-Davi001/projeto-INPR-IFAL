def mostrar_menu_escolha() -> int | None:
    """
    mostra o menu de escolha ao usuário e retorna a resposta

    mostra um menu de escolha ao usuário com opções em números inteiros de 1 a 3, caso o usuário não digite um número
    ou o usuário não digite uma opção que esteja no menu, retorna None

    Returns
    -------
    int or None
        a escolha do usuário em um int, se não for válida retorna None

    Notes
    -----
    Essa função já lida com a validação do input, porém deve se lembrar que em caso da escolha ser 
    inválida a função simplemente retorna None, então deve-se ter cuidado para verificar se o retorno foi None
    """
    print("="*40)
    print(" "*10 + "ESCOLHA UMA OPÇÃO")
    print("="*40 + "\n")
    
    print("[1] guia para aprender sobre presente simples (simple present)")
    print("[2] Se tornar um mestre do simple present (jogo: batalha pokemon)")
    print("[3] Interrogar um americano (jogo: detetive estrangeiro)")
    print("[4] encerrar programa\n")

    try:
        escolha = int(input("escolha sua opção: "))

        if not escolha in {1,2,3,4}:
            print("por favor digite um número inteiro de 1 a 4.")
            input("ok: ")
            return None
        else:
            return escolha
    except:
        print("por favor digite um número inteiro de 1 a 4.")
        input("ok: ")
        
