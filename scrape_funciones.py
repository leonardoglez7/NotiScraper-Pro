import requests as r 
from bs4 import BeautifulSoup as BS 

def validar_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        respuesta = r.get(url, headers=headers)
        if respuesta.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        
def obtener_datos(url):
    try:
        headers = {"User-Agent":"Mozilla/5.0"}
        respuesta = r.get(url, headers=headers) 
        respuesta.encoding = "utf-8"
        return respuesta.text
    except Exception as e:
        print(f"Error: {e}")

def parse_info(info): 
    try:
        soup = BS(info , "html.parser")
        titulo = soup.find("title").get_text()
        parrafos = soup.find_all("p")
        parrafos_texto = [p.get_text(strip=True) for p in parrafos[0:3]]
        
        return { "titulo"  : titulo,
        "parrafos" : " ".join(parrafos_texto).replace("\n", " ").strip()}
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    url = "https://es.wikipedia.org/wiki/Inteligencia_artificial"
    if validar_url(url):
        response = obtener_datos(url)   
        resultado = parse_info(response)   
        print(resultado["parrafos"])            