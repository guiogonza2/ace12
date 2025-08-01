import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Recupera la clave
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def test_openai_api():
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": "Dime solo 'API funcionando' en español"}
            ],
            max_tokens=10
        )
        
        print("✅ Respuesta de la API:", response.choices[0].message.content)
        return True
        
    except Exception as e:
        print("❌ Error al conectar con la API:")
        print(str(e))
        return False

if __name__ == "__main__":
    print("Probando conexión con OpenAI API...")
    if test_openai_api():
        print("🎉 ¡La API está funcionando correctamente!")
    else:
        print("🔴 Revisa tu API Key y conexión a internet")
