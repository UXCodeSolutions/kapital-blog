import urllib.request
import json

url = "http://localhost:8000/articles"
data = {
    "category": "Inteligencia Artificial",
    "title": "Cómo la IA está transformando las finanzas personales (Prueba postAI)",
    "description": "Descubre las nuevas herramientas de inteligencia artificial que te ayudan a automatizar tu ahorro, mejorar tus inversiones y mantener tu presupuesto bajo control sin esfuerzo.",
    "date": "2026-03-11",
    "readTime": "4 min"
}

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            print("¡Éxito! Artículo publicado correctamente.")
            response_body = response.read().decode('utf-8')
            print("Respuesta del servidor:")
            print(json.dumps(json.loads(response_body), indent=2))
        else:
            print(f"Error {response.status}: {response.read().decode('utf-8')}")
except Exception as e:
    print(f"Error en la petición al servidor: {e}")
