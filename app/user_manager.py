def create_user(username: str, email: str) -> dict:
    """Crée un utilisateur fictif et retourne un dictionnaire"""
    if not username or not email:
        raise ValueError("username et email sont obligatoires")
    return {"username": username, "email": email}