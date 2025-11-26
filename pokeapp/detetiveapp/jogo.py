import random
import sys
from time import sleep 
from .dialogos import criar_banco_questoes

# constantes do Jogo 
MAX_ERROS = 5 
PONTOS_VITORIA = 7
NUM_OPCOES = 4

def gerar_opcoes(frase):
    """Gera 4 opções de múltipla escolha (A, B, C, D) incluindo a correta e 3 distrações."""
    sujeito = frase['sujeito'].capitalize()
    verbo = frase['verbo_base']
    comp = frase['complemento'].replace('?', '') 
    opcoes_invalidas = []
    
    # auxiliar Trocado (DO em vez de DOES, ou vice-versa)
    if 'Does' in frase['resposta_correta']:
        aux_errado = 'Do'
        opcoes_invalidas.append(f"{aux_errado} {sujeito} {verbo} {comp}?")
    else:
        aux_errado = 'Does'
        opcoes_invalidas.append(f"{aux_errado} {sujeito} {verbo} {comp}?")

    # verbo conjugado com 's' (Erro comum: usar o 's' junto com o auxiliar)
    opcoes_invalidas.append(f"{frase['resposta_correta'].split()[0]} {sujeito} {verbo}s {comp}?")

    # erro na forma (omite o auxiliar completamente)
    opcoes_invalidas.append(f"{sujeito} {verbo} {comp}?")

    # Junta a correta com as inválidas e embaralha
    opcoes = opcoes_invalidas[:NUM_OPCOES - 1] + [frase['resposta_correta']]
    random.shuffle(opcoes)

    # formata para exibição e identifica a correta
    opcoes_formatadas = {}
    letras = ['A', 'B', 'C', 'D']
    letra_correta = ''
    
    for i, op in enumerate(opcoes):
        opcoes_formatadas[letras[i]] = op.capitalize().replace('.', '?') 
        if op == frase['resposta_correta']:
            letra_correta = letras[i]
            
    return opcoes_formatadas, letra_correta


def formatar_desafio(frase_dict):
    """Formata o desafio para o Interrogatório."""
    sujeito = frase_dict['sujeito'].capitalize()
    verbo_base = frase_dict['verbo_base']
    complemento = frase_dict['complemento']
    tema = frase_dict['tema']

    print(f"INTERROGATÓRIO ({tema}): Você precisa pressionar o entrevistado.")
    return f"Qual é a PERGUNTA correta para saber sobre: *({sujeito} / {verbo_base} / {complemento}?)*"

# loop principal do jogo
def iniciar_jogo_detetive():
    """Lógica principal do jogo de Múltipla Escolha."""
    # 1. introdução
    print("\n=======================================================")
    print("        DETETIVE ESTRANGEIRO (INTERROGATÓRIO) ")
    print("=======================================================")
    print("Você é um detetive brasileiro, encarregado de interrogar um suspeito americano.")
    sleep(1.5)
    print("Sua tarefa é formular as perguntas corretamente em inglês (Simple Present).")
    sleep(1.5)
    print("Formule a pergunta correta e você receberá uma resposta. Se errar, o suspeito ganha tempo!")
    
    # configuração inicial
    banco_de_frases = criar_banco_questoes()
    random.shuffle(banco_de_frases)
    frases_disponiveis = banco_de_frases.copy()
    
    pontos = 0
    erros = 0
    
    print("\n--- instruções ---")
    print(f"Objetivo: Acerte *{PONTOS_VITORIA}* perguntas para resolver o caso.")
    print(f"Regras: Escolha a opção (A, B, C ou D) que forma a frase INTERROGATIVA correta.")
    print(f"Limite de Erros: *{MAX_ERROS}* (5 chances)\n")

    # 3. LOOP PRINCIPAL
    while pontos < PONTOS_VITORIA and erros < MAX_ERROS:
        frase_atual = frases_disponiveis.pop()
        opcoes_dict, letra_correta = gerar_opcoes(frase_atual)
        
        print(f"\n--- Turno: {pontos + 1}/{PONTOS_VITORIA} | Erros: {erros}/{MAX_ERROS}  ---") 
        print(formatar_desafio(frase_atual))
        
        # Exibe as opções
        print("\n*Opções de Interrogatório:*")
        for letra, opcao in opcoes_dict.items():
            print(f"  {letra}: {opcao}")
        
        # Pede a resposta
        tentativa = input("\nSua Escolha (A/B/C/D): ").strip().upper()

        # 4. VERIFICAÇÃO
        if tentativa == letra_correta:
            pontos += 1
            
            # Exibe a Resposta do Suspeito
            print(f"\n PERGUNTA CORRETA! O suspeito foi pressionado.")
            print(f"> Detetive: {opcoes_dict[letra_correta]}") 
            sleep(0.5)
            print(f" Entrevistado: {frase_atual['resposta_suspeito']}")
            
        else:
            erros += 1
            print("\n ERRO GRAMATICAL! O entrevistado percebeu a falha e está menos cooperativo.")
            print(f"A pergunta correta era: {opcoes_dict[letra_correta]}")
            
            # Dica
            if 'Does' in opcoes_dict[letra_correta]:
                print(" (Dica: O sujeito é singular (He/She/It), o auxiliar deve ser com DOES!)")
            else:
                print(" (Dica: O sujeito é plural (They) ou I/You/We, o auxiliar deve ser com DO!)")

    
    # 5. FIM DO JOGO
    print("\n=======================================================")
    if pontos >= PONTOS_VITORIA:
        print("caso foi resolvido! Você obteve todas as informações e conseguiu concluir quem era o culpado.")
    else:
        print(f"o caso foi arquivado. Você excedeu o limite de {MAX_ERROS} erros. O entrevistado parou de cooperar. Tente novamente!")
    print(f"Pontuação Final: *{pontos} / {PONTOS_VITORIA}* acertos.")
    print("=======================================================")

