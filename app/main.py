import os
from typing import Union

import uvicorn
from docling.document_converter import DocumentConverter
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def parse_doc(source: str):
    converter = DocumentConverter()
    result = converter.convert(source)

    os.makedirs("output", exist_ok=True)
    with open("output/output.MD", "w") as f:
        f.write(result.document.export_to_markdown())


@app.get("/convert")
def convert_document(background_tasks: BackgroundTasks):
    source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
    background_tasks.add_task(parse_doc, source)
    return {"message": "Document conversion started in the background"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
