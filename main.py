import joblib
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

# 1. Initialize the FastAPI app
app = FastAPI(
    title="House Price Predictor API",
    description=(
        "A production-grade API serving our saved Scikit-Learn pipeline."
    ),
)

# 2. Load our saved model pipeline into memory once when the server starts
model = joblib.load("house_price_model.pkl")


# 3. Define the expected data structure using Pydantic (ensures safety & validation)
class HouseInput(BaseModel):
  sqft: int
  bedrooms: int
  neighborhood: str


# 4. Create the POST endpoint for predictions
@app.post("/predict")
def predict_price(house: HouseInput):
  # Convert incoming JSON request into a Pandas DataFrame
  input_df = pd.DataFrame([house.model_dump()])

  # Run it through our saved pipeline (which automatically scales and encodes it!)
  prediction = model.predict(input_df)

  # Return the clean prediction back as JSON
  return {"predicted_price": int(prediction[0]), "status": "success"}

