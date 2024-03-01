filmes = ["Os Vingadores", "Carros", "Shrek 2", "O Jogo da Imitacao"]
series = ["One Piece", "Sillicon Valley", "Breaking Bad", "Avatar Lenda de Aang"]

def catalogo():
    print("""\n-- Escolha qual catalogo deseja visualizar:\n
          1 - Filmes
          2 - Series\n
          0 - Sair """)
    
    escolha = int(input("--> "))
    
    if escolha == 1:
        print("\n-- Catalogo de filmes Disponiveis --\n")
    
        for filme in filmes:
            print("- ", filme)
    
        print('\n')
    elif escolha == 2:
        print("\n-- Catalogo de series Disponiveis --\n")
    
        for serie in series:
            print("- ", serie)
        
        print('\n')
    elif escolha == 0:
        return

def main():
    
    while True:
        print("""\n-- Bem vindo! --
        \n-- Sistema Simplificado de Streaming de Video --\n
        Opções disponiveis:\n
        1 - Visulizar catalogo de filmes e séries
        0 - Finalizar Programa\n
        Digite o número da opção que deseja realizar:\n""")
        
        escolha = int(input("--> "))
        
        if escolha == 1:
            catalogo()
        elif escolha == 0:
            break
        
    
main()