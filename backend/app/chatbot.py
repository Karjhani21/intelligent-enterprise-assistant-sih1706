def get_response(query: str) -> str:
    q = query.lower()

    # Handle common variations
    if "leave" in q and "casual" in q:
        return "Employees are entitled to 12 casual leaves per year."

    if "password" in q and "reset" in q:
        return "Visit the self-service portal and click 'Reset Password'."

    if "annual" in q and "day" in q:
        return "Annual Day is scheduled for December 15."

    if "maternity" in q:
        return "Eligible employees can avail up to 26 weeks of maternity leave."

    # Search knowledge base
    for _, items in KNOWLEDGE_BASE.items():
        for keyword, answer in items.items():
            if keyword.lower() in q:
                return answer

    return "I couldn't find an exact answer. Please contact HR or IT support."