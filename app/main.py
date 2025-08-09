from typing import Union
import uvicorn

from fastapi import FastAPI
from docling.document_converter import DocumentConverter


app = FastAPI()

@app.get("/convert")
def convert_document():
    source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
    converter = DocumentConverter()
    result = converter.convert(source)
    print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
