import google.generativeai as genai
import os
from cars.models import Car
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


def get_ai_bio(car):
    brand = car.brand.name
    year = car.model_year
    model_car = car.model

    response = model.generate_content(
        f"Atue como um especialista em vendas de carros, e monte uma breve e simples descrição do carro {model_car}, marca {brand}, ano {year}. Com no máixmo 4 linhas"
    )

    return response.text
