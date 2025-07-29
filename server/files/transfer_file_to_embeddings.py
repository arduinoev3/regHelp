import os
import traceback
from files.file_embedder import FileEmbedder
await file.download_to_drive(file_path)
    
async def transfer_file_to_embeddings(file_path: str):
    embedder = FileEmbedder()

    try:
        await embedder.embed_file(file_path=file_path)
    except Exception as e:
        print(f"Error occured while embedding file {file_path}:\n{e}\n")
        traceback.print_exc()
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)