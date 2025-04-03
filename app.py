from app import create_app

app = create_app()  # Llama a la función que inicia la app dentro de /app

if __name__ == "__main__":
    app.run(debug=True)