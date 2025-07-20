import os
import traceback
from telegram import File
from files.embedder import Embedder

async def transfer_file_to_embeddings(file: File, file_path: str, embedder: Embedder):
    await file.download_to_drive(file_path)
    try:
        await embedder.embed_file(file_path=file_path)
    except Exception as e:
        print(f"Error occured while embedding file {file_path}:\n{e}\n")
        traceback.print_exc()
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
    