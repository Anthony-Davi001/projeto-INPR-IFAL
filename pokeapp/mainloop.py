import os
from .ui import mostrar_menu_escolha, explicar_presente_simples
from .utils import limpar_console
from .pokeapp import iniciar_jogo_pokemon
from .detetiveapp import iniciar_jogo_detetive

def mainloop() -> None:
    while True:
        escolha = mostrar_menu_escolha()
        match escolha:
            case 1:
                explicar_presente_simples()
            case 2:
                iniciar_jogo_pokemon()
            case 3: 
                iniciar_jogo_detetive()
            case 4:
                break
            case _: 
                pass
        limpar_console()

