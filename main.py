from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from rembg import remove
import io
from PIL import Image

app = FastAPI()

# Mount static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_index():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/remove-background/")
async def remove_background(file: UploadFile = File(...)):
    input_image = await file.read()
    
    # Remove background
    output_image = remove(input_image)

    # Save the output image in memory as a PNG file
    output_io = io.BytesIO(output_image)
    output_io.seek(0)

    # Return the output image to the user
    return FileResponse(output_io, media_type="image/png", filename="output.png")
