from ollama import chat
import json

def analyze(foods):

    prompt = f"""
    You are a professional nutritionist and dietitian with expertise in food science, nutritional analysis, and healthy eating recommendations.

    Your task is to analyze the detected foods and provide realistic nutritional estimations based on common serving sizes and nutritional standards.

    Detected foods:

    {foods}

    Instructions:

    - Estimate values using realistic serving portions typically consumed by an adult.
    - Nutrition values must be approximate but as realistic as possible.
    - Consider food preparation methods when appropriate (fried, baked, grilled, processed, etc.).
    - Provide nutritional estimates for:
    - grams
    - calories
    - fat
    - protein
    - carbohydrates
    - Return numeric values only for nutrition fields.
    - Generate exactly 3 concise and actionable healthy recommendations per food.
    - Recommendations must be specific to that food, not generic advice.
    - Recommendations should promote healthier eating habits, portion control, or healthier alternatives.
    - Avoid repetitive recommendations across foods.
    - Do not invent foods not present in the detected list.
    - Use professional nutrition reasoning.
    - If confidence in a food is low, provide a reasonable estimate based on common examples.
    """
    schema = {
        "type": "object",
        "properties": {
            "foods": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "food_name": {
                            "type": "string"
                        },
                        "nutrition_details": {
                            "type": "object",
                            "properties": {
                                "approx_grams": {
                                    "type": "number"
                                },
                                "approx_calories": {
                                    "type": "number"
                                },
                                "approx_fat": {
                                    "type": "number"
                                },
                                "approx_protein": {
                                    "type": "number"
                                },
                                "approx_carbohydrates": {
                                    "type": "number"
                                }
                            },
                            "required": [
                                "approx_grams",
                                "approx_calories",
                                "approx_fat",
                                "approx_protein",
                                "approx_carbohydrates"
                            ]
                        },
                        "recommendations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "text": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "id",
                                    "text"
                                ]
                            }
                        }
                    },
                    "required": [
                        "id",
                        "food_name",
                        "nutrition_details",
                        "recommendations"
                    ]
                }
            }
        },
        "required": ["foods"]
    }

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        format=schema
    )

    content = response.message.content

    try:
        return json.loads(content)

    except:
        return {
            "ollama_response":content
        }