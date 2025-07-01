from scrape_funciones import validar_url, obtener_datos, parse_info
import csv

archivo_urls = "urls.txt"
archivo_salida = "resultados.csv"

with open(archivo_urls, "r", encoding="utf-8") as archivo:
    urls = archivo.read().splitlines()
    
resultados = [ ]    

for url in urls:
    if validar_url(url):
        html = obtener_datos(url)
        datos = parse_info(html)
        fila = {"url": url,
        "titulo": datos["titulo"],
        "parrafos": datos["parrafos"]
        }
        resultados.append(fila)
        print(f"[Procesada] {url}")
    else:
        print(f"[Invalida] {url}")

with open(archivo_salida, "a", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo,fieldnames=["url", "titulo", "parrafos"])
    for fila in resultados:
        escritor.writerow(fila)

print(f"\n Proceso finalizado. Resultados guardados en: {archivo_salida}")