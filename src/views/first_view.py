def introduction_page():
    message = ''' 
        Sistema Cadastral

        * Cadastrsar Pessoa - 1
        * Buscar Pessoa por nome - 2
        * Sair - 5
    '''

    print(message)
    command = input('Comando: ')

    return command