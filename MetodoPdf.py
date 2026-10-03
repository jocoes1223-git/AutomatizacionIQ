import re
import pandas as pd

from pathlib import Path
from pypdf import PdfReader

ruta_carpeta = "*\AutomatizacionIQ\CufesDian"

def leer_pdfs_pathlib(ruta_carpeta):
  carpeta = Path(ruta_carpeta)

  if not carpeta.exists():
    return

  for archivo_pdf in carpeta.glob('*.pdf'):
    print(f'\nEjecutando: {archivo_pdf.name}')
    reader = PdfReader(archivo_pdf)
    for i, pagina in enumerate(reader.pages):
      texto = pagina.extract_text()


    num_factura_origen = r"Número de Factura:\s*(.*)"
    fec_emision_origen = r"Fecha de Emisión:\s*(.*)"
    nit_emisor_origen = r"Nit del Emisor:\s*(.*)"
    codigo_origen = r"Código:\s*(.*)"
    descripcion_origen = r"Número de Factura:\s*(.*)"
    cantidad_origen = r"Número de Factura:\s*(.*)"
    precio_origen = r"Número de Factura:\s*(.*)"


    num_factura = re.search(num_factura_origen, texto)
    num_factura = re.search(fec_emision_origen, texto)
    num_factura = re.search(nit_emisor_origen, texto)
    num_factura = re.search(codigo_origen, texto)
    num_factura = re.search(descripcion_origen, texto)
    num_factura = re.search(cantidad_origen, texto)
    num_factura = re.search(precio_origen, texto)




df = pd.DataFrame(datos)
archivo_salida = "*\AutomatizacionIQ\ExcelConsolidado"
df.to_excel(archivo_salida, index=False, engine="openpyxl")