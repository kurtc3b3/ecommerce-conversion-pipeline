"""BentoML serving stub — wire promoted MLflow model here."""

def predict(session_id: str, customer_id: str, product_id: str) -> dict:
    return {
        "conversion_probability": 0.0,
        "session_id": session_id,
        "customer_id": customer_id,
        "product_id": product_id,
    }
