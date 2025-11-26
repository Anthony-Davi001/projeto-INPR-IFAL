def criar_banco_questoes():
    """Cria o banco de dados de perguntas (QUESTION) com distrações, focado no interrogatório."""
    # Estrutura: {tipo, sujeito, verbo_base, complemento, tema, resposta_correta, resposta_suspeito}
    return [
        # perguntas e respostas
        {"tipo": "QUESTION", "sujeito": "you", "verbo_base": "live", "complemento": "alone in that house?", "tema": "Suspeito", "resposta_correta": "Do you live alone in that house?", "resposta_suspeito": "No, I live with my cat, Mittens."},
        {"tipo": "QUESTION", "sujeito": "Mr. Smith", "verbo_base": "work", "complemento": "on weekends?", "tema": "Rotina", "resposta_correta": "Does Mr. Smith work on weekends?", "resposta_suspeito": "Yes, he always works on Saturday mornings."},
        {"tipo": "QUESTION", "sujeito": "the children", "verbo_base": "know", "complemento": "anything about the event?", "tema": "Testemunhas", "resposta_correta": "Do the children know anything about the event?", "resposta_suspeito": "I think they do, they were playing nearby."},
        {"tipo": "QUESTION", "sujeito": "she", "verbo_base": "tell", "complemento": "you where she went?", "tema": "Relacionamento", "resposta_correta": "Does she tell you where she went?", "resposta_suspeito": "No, she never tells me her plans."},
        {"tipo": "QUESTION", "sujeito": "it", "verbo_base": "happen", "complemento": "every night?", "tema": "Frequência", "resposta_correta": "Does it happen every night?", "resposta_suspeito": "No, only on Tuesdays and Thursdays."},
        {"tipo": "QUESTION", "sujeito": "they", "verbo_base": "need", "complemento": "a lawyer?", "tema": "Procedimento", "resposta_correta": "Do they need a lawyer?", "resposta_suspeito": "Absolutely, they asked for one immediately."},
        {"tipo": "QUESTION", "sujeito": "the car", "verbo_base": "have", "complemento": "any damage?", "tema": "Veículo", "resposta_correta": "Does the car have any damage?", "resposta_suspeito": "Yes, it has a dent on the passenger side."},
        {"tipo": "QUESTION", "sujeito": "your sister", "verbo_base": "see", "complemento": "anyone suspicious?", "tema": "Testemunha", "resposta_correta": "Does your sister see anyone suspicious?", "resposta_suspeito": "She saw a man running across the street."},
        {"tipo": "QUESTION", "sujeito": "the security cameras", "verbo_base": "record", "complemento": "the entrance?", "tema": "Segurança", "resposta_correta": "Do the security cameras record the entrance?", "resposta_suspeito": "Unfortunately, they don't record the back door."},
        {"tipo": "QUESTION", "sujeito": "the suspect", "verbo_base": "have", "complemento": "a weapon?", "tema": "Crime", "resposta_correta": "Does the suspect have a weapon?", "resposta_suspeito": "I think he keeps it hidden in his jacket."},
        {"tipo": "QUESTION", "sujeito": "you", "verbo_base": "know", "complemento": "the victim?", "tema": "Relacionamento", "resposta_correta": "Do you know the victim?", "resposta_suspeito": "I saw him once or twice at the cafe."},
        {"tipo": "QUESTION", "sujeito": "the witnesses", "verbo_base": "say", "complemento": "the same thing?", "tema": "Testemunhas", "resposta_correta": "Do the witnesses say the same thing?", "resposta_suspeito": "No, their stories conflict on the timeline."},
    ]
