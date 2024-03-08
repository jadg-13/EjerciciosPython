# Ejemplo de aprendizaje analógico simple
# Consideraremos un sistema basado en casos para recomendar películas
casos = {
    'Comedia': ['Ace Ventura', 'Superbad', 'The Hangover'],
    'Acción': ['Die Hard', 'The Avengers', 'Mad Max'],
    'Drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather']
}

def recomendar_pelicula(genero):
    if genero in casos:
        return casos[genero][0]  # Devolvemos la primera película del género dado
    else:
        return "Lo siento, no tenemos recomendaciones para ese género."

# Ejemplo de uso
genero = 'Comedia'
print("Te recomendamos ver:", recomendar_pelicula(genero))
