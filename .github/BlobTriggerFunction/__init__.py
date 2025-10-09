import logging

import azure.functions as func

def main(myblob: func.InputStream):
    logging.info(f"🟢 Blob trigger function ejecutada para el blob: {myblob.name}")
    logging.info(f"Tamaño del blob: {myblob.length} bytes")
