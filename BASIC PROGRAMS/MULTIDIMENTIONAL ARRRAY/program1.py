def chatbot(user_message):
    lang = detect_language(user_message)
    normalized = preprocess(user_message, lang)

    intent, intent_conf = classify_intent(normalized)
    answer, retrieval_score = retrieve_from_docs(normalized)

    confidence = combine(intent_conf, retrieval_score)

    if confidence > 0.7:
        reply = translate(answer, lang)
    elif confidence > 0.4:
        reply = ask_clarification(intent, lang)
    else:
        reply = escalate_to_human(user_message, lang)

    log_interaction(user_message, reply, lang, confidence)
    return reply