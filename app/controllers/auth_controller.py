from app.services.auth_service import AuthService

def register_user(data):
    email = data.get("email")
    password = data.get("password")
    
    return AuthService.register(email, password)
    
def login_user(data):
    email = data.get("email")
    password = data.get("password")
    
    return AuthService.login(email, password)