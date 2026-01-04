from flask import Flask, render_template

app = Flask(__name__)

# Proyectos (solo sube tus archivos a /static/img o /static/video)
projects = [
    {
        "title": "App de Análisis de Datos Clínicos",
        "description": "Dashboard en Python para análisis estadístico y visualización de datos en salud mental.",
        "media": "video/data_app_demo.mp4",
        "type": "video",
        "tech": ["Python", "Pandas", "Flask"]
    },
    {
        "title": "Plataforma Web Segura con JWT",
        "description": "Aplicación web con autenticación, roles y base de datos.",
        "media": "img/proyectos/flask_jwt.png",
        "type": "image",
        "tech": ["Flask", "PostgreSQL", "JWT"]
    },
    {
        "title": "Security Lab OWASP",
        "description": "Análisis de vulnerabilidades y pruebas de seguridad.",
        "media": "video/owasp_lab.mp4",
        "type": "video",
        "tech": ["Kali Linux", "OWASP", "Wireshark"]
    }
]

@app.route("/")
def index():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
