from app import app
import view




if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)