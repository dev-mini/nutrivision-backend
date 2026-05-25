from ollama import chat
import json

def analyze(foods):

    prompt=f"""
    Detected foods:

    {foods}

    Estimate nutritional values and recommendations.

    Rules:
    - Numeric values only for nutrition data
    - Recommendations must be concise
    - Generate 3 recommendations per food
    - Do not include explanations
    - Return only valid JSON
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