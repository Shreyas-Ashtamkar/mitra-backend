from mainapp import create_app

app = create_app()

print(app.config.get("SECRET_KEY"))
