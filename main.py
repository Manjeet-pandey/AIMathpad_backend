from fastapi import FastAPI, File, UploadFile
from model_load import model_load
from predict import make_prediction
import numpy as np
import cv2

app = FastAPI()


# @app.post("/image")
# async def image(file: UploadFile = File(...)):
#     model_load()
#     image = np.asarray(bytearray(await file.read()),dtype="uint8")
#     image = cv2.imdecode(image,cv2.IMREAD_UNCHANGED)
#     prediction = make_prediction(image)
#     return {"message": prediction}
@app.get("/")
async def root():
    image = cv2.imread("./hello.png")
    result = make_prediction(image)
    # latex_text = unicode_to_latex(result)
    return {"message": result}
