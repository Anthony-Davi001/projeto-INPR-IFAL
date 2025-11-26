def criar_banco_de_frases_pokemon() -> list[dict]:
    """retorna um banco de questões em uma lista de dicionarios"""
    # Estrutura dos dicionarios: {sujeito, verbo_base, complemento, resposta_correta, ataque}
    return [
        # ----------------------------------------------------
        # GRUPO 1: verbos na base (I, You, We, They) - 10 Opções
        # ----------------------------------------------------
        {"sujeito": "I", "verbo_base": "use", "complemento": "Tackle on the opponent.", "resposta_correta": "use", "ataque": "Tackle"},
        {"sujeito": "We", "verbo_base": "launch", "complemento": "a combined attack.", "resposta_correta": "launch", "ataque": "Double Team"},
        {"sujeito": "They", "verbo_base": "strike", "complemento": "the foe with force.", "resposta_correta": "strike", "ataque": "Quick Attack"},
        {"sujeito": "You", "verbo_base": "block", "complemento": "the enemy's punch.", "resposta_correta": "block", "ataque": "Protect"},
        {"sujeito": "I", "verbo_base": "wait", "complemento": "for the perfect moment to attack.", "resposta_correta": "wait", "ataque": "Focus"},
        {"sujeito": "We", "verbo_base": "fire", "complemento": "a strong beam of energy.", "resposta_correta": "fire", "ataque": "Hyper Beam"},
        {"sujeito": "The Pokémons", "verbo_base": "retreat", "complemento": "before the explosion.", "resposta_correta": "retreat", "ataque": "Defense Curl"},
        {"sujeito": "You", "verbo_base": "hit", "complemento": "the target with a Water Pulse.", "resposta_correta": "hit", "ataque": "Water Pulse"},
        {"sujeito": "The allies", "verbo_base": "defend", "complemento": "against the incoming move.", "resposta_correta": "defend", "ataque": "Bide"},
        {"sujeito": "I", "verbo_base": "charge", "complemento": "my energy for the next turn.", "resposta_correta": "charge", "ataque": "Charge"},

        # ----------------------------------------------------
        # GRUPO 2: regra geral -S (He, She, It) - 15 Opções
        # ----------------------------------------------------
        {"sujeito": "Pikachu", "verbo_base": "use", "complemento": "Thunderbolt on the foe.", "resposta_correta": "uses", "ataque": "Thunderbolt"},
        {"sujeito": "The rival", "verbo_base": "call", "complemento": "back his Pokémon.", "resposta_correta": "calls", "ataque": "Recall"},
        {"sujeito": "Squirtle", "verbo_base": "hit", "complemento": "the opponent with Water Gun.", "resposta_correta": "hits", "ataque": "Water Gun"},
        {"sujeito": "Jigglypuff", "verbo_base": "sing", "complemento": "a powerful, sleepy song.", "resposta_correta": "sings", "ataque": "Sing"},
        {"sujeito": "The creature", "verbo_base": "jump", "complemento": "over the incoming attack.", "resposta_correta": "jumps", "ataque": "Agility"},
        {"sujeito": "Bulbasaur", "verbo_base": "throw", "complemento": "a bundle of vines.", "resposta_correta": "throws", "ataque": "Vine Whip"},
        {"sujeito": "Charizard", "verbo_base": "release", "complemento": "a stream of fire.", "resposta_correta": "releases", "ataque": "Flamethrower"},
        {"sujeito": "Gastly", "verbo_base": "float", "complemento": "closer to the rival.", "resposta_correta": "floats", "ataque": "Levitate"},
        {"sujeito": "Mewtwo", "verbo_base": "launch", "complemento": "a devastating psychic attack.", "resposta_correta": "launches", "ataque": "Psychic"},
        {"sujeito": "It", "verbo_base": "need", "complemento": "to heal quickly.", "resposta_correta": "needs", "ataque": "Recover"},
        {"sujeito": "The enemy Pokémon", "verbo_base": "start", "complemento": "its counter-attack.", "resposta_correta": "starts", "ataque": "Counter"},
        {"sujeito": "Gyarados", "verbo_base": "strike", "complemento": "the water with its tail.", "resposta_correta": "strikes", "ataque": "Aqua Tail"},
        {"sujeito": "Snorlax", "verbo_base": "sleep", "complemento": "in the middle of the battle.", "resposta_correta": "sleeps", "ataque": "Rest"},
        {"sujeito": "He", "verbo_base": "command", "complemento": "the final blow.", "resposta_correta": "commands", "ataque": "Final Command"},
        {"sujeito": "She", "verbo_base": "dodge", "complemento": "the rock slide.", "resposta_correta": "dodges", "ataque": "Evade"},


        # ----------------------------------------------------
        # GRUPO 3: regra especial -ES (O, S, SS, SH, CH, X) - 10 Opções
        # ----------------------------------------------------
        {"sujeito": "The enemy", "verbo_base": "miss", "complemento": "the great punch.", "resposta_correta": "misses", "ataque": "Dynamic Punch"},
        {"sujeito": "The ghost Pokémon", "verbo_base": "go", "complemento": "through the opponent.", "resposta_correta": "goes", "ataque": "Shadow Sneak"}, # -o
        {"sujeito": "The opponent", "verbo_base": "finish", "complemento": "the turn with a blast.", "resposta_correta": "finishes", "ataque": "Giga Impact"}, # -sh
        {"sujeito": "Eve", "verbo_base": "catch", "complemento": "the thrown item.", "resposta_correta": "catches", "ataque": "Retrieve"}, # -ch
        {"sujeito": "Charizard", "verbo_base": "do", "complemento": "a powerful fire attack.", "resposta_correta": "does", "ataque": "Dragon Breath"}, # -o
        {"sujeito": "The attack", "verbo_base": "pass", "complemento": "straight through the shield.", "resposta_correta": "passes", "ataque": "Phasing Attack"}, # -ss
        {"sujeito": "The foe", "verbo_base": "push", "complemento": "our team back with strength.", "resposta_correta": "pushes", "ataque": "Force Push"}, # -sh
        {"sujeito": "The Pokémon", "verbo_base": "mix", "complemento": "energy and plasma.", "resposta_correta": "mixes", "ataque": "Plasma Mix"}, # -x
        {"sujeito": "It", "verbo_base": "bless", "complemento": "the allied team with power.", "resposta_correta": "blesses", "ataque": "Aura Blessing"}, # -ss
        {"sujeito": "The enemy", "verbo_base": "watch", "complemento": "our moves carefully.", "resposta_correta": "watches", "ataque": "Scout"}, # -ch
        
        # ----------------------------------------------------
        # GRUPO 4: regra especial -IES (Consoante + Y) - 5 Opções
        # ----------------------------------------------------
        {"sujeito": "The Pokémon", "verbo_base": "fly", "complemento": "into the sky for the attack.", "resposta_correta": "flies", "ataque": "Fly"}, # consoante + y -> -ies
        {"sujeito": "The Pokémon", "verbo_base": "cry", "complemento": "to lower the rival's defense.", "resposta_correta": "cries", "ataque": "Tearful Look"}, # consoante + y -> -ies
        {"sujeito": "The Pokémon", "verbo_base": "try", "complemento": "to learn the new technique.", "resposta_correta": "tries", "ataque": "Attempt"}, # consoante + y -> -ies
        {"sujeito": "The opponent", "verbo_base": "reply", "complemento": "with a stronger counter.", "resposta_correta": "replies", "ataque": "Counter Attack"}, # consoante + y -> -ies
        {"sujeito": "The Legendary", "verbo_base": "destroy", "complemento": "the battlefield with a blast.", "resposta_correta": "destroys", "ataque": "Cataclysm"}, # Vogal + Y = -s (para incluir um caso de exceção)
    ]