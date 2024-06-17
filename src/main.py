import uvicorn
from fastapi import FastAPI

app = FastAPI()

def get_app_description():
    return (
    	"Welcome to the Iris Species Prediction API!"
    	"This API allows you to predict the species of an iris flower based on its sepal and petal measurements."
    	"Use the '/predict/' endpoint with a POST request to make predictions."
    	"Example usage: POST to '/predict/' with JSON data containing sepal_length, sepal_width, petal_length, and petal_width."
	)

@app.get("/")
async def root():
    return {"message": get_app_description()}

if __name__ == "__main__":
    # There are a lot of parameters for uvicorn, you should check the docs
    uvicorn.run(
        "main:app",
        # host=settings.APP_HOST,
        # port=settings.APP_PORT,
        # workers=settings.APP_WORKERS,
        # reload=settings.APP_DEBUG,
    )