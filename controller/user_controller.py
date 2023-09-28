from app import app
from model.user_model import user_model

obj=user_model()
@app.route("/sign")
def sign():
    return obj.user_sign_model()


