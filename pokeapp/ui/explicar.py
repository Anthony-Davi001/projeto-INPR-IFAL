import os
from time import sleep
from ..utils import limpar_console

def explicar_presente_simples() -> None:
    limpar_console()

    sleep(0.5)
    print("O presente simples em inglês (simple present) é usado para expressar hábitos, rotinas, fatos permanentes e verdades universais.")
    input("pressione ENTER para continuar:")

    print("\nExemplos de uso:")
    sleep(0.8)
    print("  * Rotina/Hábito: I *drink* coffee every morning. (Eu bebo café todas as manhãs.)")
    sleep(0.8)
    print("  * Fato Permanente: They *live* in London. (Eles moram em Londres.)")
    sleep(0.8)
    print("  * Verdade Universal: The sun *rises* in the east. (O sol nasce no leste.)")
    sleep(0.8)
    input("pressione ENTER para continuar:")

    print("\nRegras de Conjugação")
    print("1. Forma Básica (I, You, We, They)")
    sleep(0.8)
    print("  Para a maioria dos sujeitos (I, you, we, they), usamos o verbo na *forma base* (infinitivo sem o 'to').")

    input("pressione ENTER para continuar:")

    sleep(0.8)
    print("\nExemplos:")
    print("  * I *work* every day. (Eu trabalho todos os dias.)")
    sleep(0.8)
    print("  * They *live* in a big city. (Eles moram em uma cidade grande.)")
    sleep(0.8)
    print("  * We *speak* Portuguese. (Nós falamos português.)")
    sleep(0.8)
    input("pressione ENTER para continuar:\n")

    print("\n2. A Regra do 'S' (He, She, It) ⚠️")
    print("Quando o sujeito é a *terceira pessoa do singular* (he, she, it), o verbo deve receber um acréscimo no final:")
    sleep(0.8)
    print("  * Geral: Adiciona-se *-s* (Ex: She *wants* a coffee).")
    sleep(0.8)
    print("  * Verbos em -s, -ss, -sh, -ch, -x, -o: Adiciona-se *-es* (Ex: He *goes* to school; She *watches* TV).")
    sleep(0.8)
    print("  * Verbos em consoante + -y: Troca-se o *-y* por *-ies* (Ex: He *studies* English).")
    
    input("pressione ENTER para continuar:")

    print("\n3. Forma Afirmativa: Estrutura Completa")
    sleep(0.8)
    print("Na forma afirmativa, *NÃO* usamos os auxiliares 'do' ou 'does'. A estrutura é direta:")
    sleep(0.8)
    print("  * Sujeitos (I, You, We, They) + Verbo na Forma Base.")
    sleep(0.8)
    print("  * Sujeitos (He, She, It) + Verbo com -s / -es / -ies.")
    sleep(0.8)

    input("pressione ENTER para continuar:")

    print("\nExemplos de Afirmativa (He, She, It):")
    sleep(0.8)
    print("  * He *teaches* English. (Ele ensina inglês.)")
    sleep(0.8)
    print("  * She *plays* tennis. (Ela joga tênis.)")
    sleep(0.8)
    input("pressione ENTER para continuar:")

    limpar_console()
    print("---" * 15)
    print("    Forma Negativa e Interrogativa")
    print("---" * 15)
    sleep(0.8)

    print("\nNas formas negativa e interrogativa, usamos os verbos auxiliares *do* e *does*.")
    print("O auxiliar *does* é usado apenas para a terceira pessoa do singular (he, she, it).")
    sleep(0.8)
    print("\nRegra Ouro: Quando usamos DO ou DOES, o verbo principal SEMPRE volta à sua *forma base* (sem o '-s'!).")
    input("pressione ENTER para continuar:")

    print("\n4. Forma Negativa")
    print("Usamos: *Sujeito + do/does + not + Verbo na Forma Base*.")
    sleep(0.8)
    print("Exemplos:")
    sleep(0.8)
    print("  * I *do not* *work* here. (Eu não trabalho aqui.)")
    sleep(0.8)
    print("  * She *does not* *like* broccoli. (Ela não gosta de brócolis.)")
    input("pressione ENTER para continuar:")

    print("\n5. Forma Interrogativa")
    print("Usamos: Do/Does + Sujeito + Verbo na Forma Base + ?")
    sleep(0.8)
    print("Exemplos:")
    sleep(0.8)
    print("  * *Do* you *speak* Spanish? (Você fala espanhol?)")
    sleep(0.8)
    print("  * *Does* he *live* nearby? (Ele mora perto?)")
    input("pressione ENTER para finalizar:")

    