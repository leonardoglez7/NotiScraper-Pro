![Foto del scraper](banner.png)
notiScraper-Pro

notiScraper-Pro es una herramienta de scraping modular desarrollada en Python. Su objetivo es extraer de forma automática los títulos y los primeros párrafos de una lista de páginas web, validando previamente la accesibilidad de las URLs, y almacenando los resultados en un archivo CSV estructurado. El proyecto está diseñado para ser educativo, escalable y adaptable a distintos entornos de scraping básico.

Características

- Lectura de múltiples URLs desde un archivo de texto externo
- Validación del estado HTTP de cada enlace antes del scraping
- Extracción del título de la página y los tres primeros párrafos
- Almacenamiento automático de los resultados en un archivo CSV
- Separación de responsabilidades mediante módulos reutilizables
- Compatible con Pydroid, entornos virtuales o sistemas de escritorio

Requisitos

- Python 3.x
- requests
- beautifulsoup4

