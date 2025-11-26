import random
import sys
from time import sleep
from .dialogos import criar_banco_de_frases_pokemon
from ..utils import limpar_console

# --- Constantes do Jogo ---
MAX_VIDAS = 4
PONTOS_VITORIA = 7 

# --- Funções Auxiliares ---

def exibir_guia_rapido():
    print("\n=================================================================")
    print("   GUIA RÁPIDO PARA BATALHA: SIMPLE PRESENT (Regras de Ataque)  ")
    print("=================================================================")
    
    sleep(0.5)
    print("1. Regra Geral (I, You, We, They): O verbo permanece na sua forma base.")
    print("  * Ex: We *use* Tackle; I *hit* the target.")
    
    sleep(0.5)
    print("\n2. A Regra do 'S' (He, She, It)")
    print("Para a 3ª pessoa do singular (o Pokémon!), o verbo recebe um acréscimo:")
    
    sleep(0.5)
    print("  * Geral: Adiciona-se *-s*.")
    sleep(0.5)
    print("  * Verbos em -s, -ss, -sh, -ch, -x, -o: Adiciona-se *-es*.")
    sleep(0.5)
    print("  * Verbos em consoante + -y: Troca-se o *-y* por *-ies*.")
    print("-------------------------------------------------------\n")
    input("pressione enter para continuar: ")


def formatar_frase_batalha(frase_dict) -> str:
    """Formata a frase de batalha a partir do dicionário."""
    sujeito = frase_dict['sujeito']
    verbo_base = frase_dict['verbo_base']
    complemento = frase_dict['complemento']
    ataque = frase_dict['ataque']
    return f"{ataque} : {sujeito} _______ {complemento} ({verbo_base})"


def iniciar_jogo_pokemon() -> None:
    # reordena as frases recebidas (importante para imprevisibilidade)
    banco_de_frases = criar_banco_de_frases_pokemon()
    random.shuffle(banco_de_frases)
    frases_disponiveis = banco_de_frases.copy()
    
    # Status do Jogador
    pontos = 0
    vidas_restantes = MAX_VIDAS

    # exibe um guia rápido para o jogador lembrar das regras princioais
    exibir_guia_rapido() 

    # Inicialização 
    print("POKÉMON BATTLE: SIMPLE PRESENT MASTER")
    
    print(f"Objetivo: Acerte *{PONTOS_VITORIA}* ataques para vencer a Liga Pokémon!")
    print(f"Regras: Complete a frase usando o verbo no **SIMPLE PRESENT**.")
    print(f"Suas Vidas: {vidas_restantes}\n")

    # loop Principal do Jogo
    while pontos < PONTOS_VITORIA and vidas_restantes > 0:    
        frase_atual = frases_disponiveis.pop()
        
        print(f"\n--- TURNO {pontos + 1}/{PONTOS_VITORIA} ---") 
        
        # Formatação
        print(f"O seu time precisa agir! {formatar_frase_batalha(frase_atual)}") 
        
        # Pede a resposta, garantido que difença de maiusculo, minusculo e espaços redundantes afete o resultado 
        tentativa = input("Verbo (Simple Present): ").strip().lower()
        resposta_correta = frase_atual['resposta_correta'] 
        
        # Verifica a resposta
        if tentativa == resposta_correta:
            pontos += 1
            print(f"\n acerto! *{frase_atual['ataque']}* acertou em cheio!")
            print(f"> Frase Correta: {frase_atual['sujeito']} *{resposta_correta}* {frase_atual['complemento']}")
            print(f"Placar: *{pontos}* vitórias | Vidas: *{vidas_restantes}*")
        else:
            vidas_restantes -= 1
            print("\nerrou! O ataque falhou e o Pokémon levou dano.")
            print(f"A resposta correta era: *{resposta_correta}*")
            
            # Dica de Regra do Simple Present (Aprimorada)
            if frases_disponiveis: 
                sujeito = frase_atual['sujeito']

                # Verifica se o sujeito é 3a pessoa (He, She, It)
                if sujeito in ["He", "She", "It"] or (sujeito not in ["I", "We", "You", "They"] and "s" in resposta_correta):
                    print(" (Dica: Lembre-se da regra do 's' (ou -es/-ies) para a 3ª pessoa do singular!)")

            print(f"Placar: *{pontos}* vitórias | Vidas: *{vidas_restantes}*")

        input("continuar: ")
        limpar_console()
    
    # resultados de fim de jogo
    print("\n=======================================================")
    if pontos >= PONTOS_VITORIA:
        print("Você venceu o rival e se tornou um mestre pokemon!")
    else:
        print("Seu time desmaiou. Volte ao Centro Pokémon novamente depois")

    print(f"Pontuação Final: *{pontos} / {PONTOS_VITORIA}* acertos.")
    print("=======================================================")
    input("pressione ENTER para finalizar: ")
