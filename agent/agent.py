from google.adk.agents import Agent
import google.generativeai as genai

# --- Tools ---


def recipe_suggester(ingredients: str) -> str:
    """Suggest recipes based on user-provided ingredients."""
    # In real app, you’d query a recipe DB. For now, keep it simple.
    example_prompt = f"Suggest 2 easy recipes using these ingredients: {ingredients}"
    response = genai.GenerativeModel(
        "gemini-2.0-flash").generate_content(example_prompt)
    return response.text


def recommend_items(purchase_history: str) -> str:
    """Recommend items based on past purchases."""
    prompt = f"Based on the following past purchases, suggest 3 useful products the customer may like: {purchase_history}"
    response = genai.GenerativeModel(
        "gemini-2.0-flash").generate_content(prompt)
    return response.text


def budget_alert(cart_items: str, budget: float) -> str:
    """Estimate total and alert if cart exceeds budget."""
    prompt = f"These are the cart items and prices: {cart_items}. The budget is ₹{budget}. Is the total over budget? Suggest cheaper alternatives if needed."
    response = genai.GenerativeModel(
        "gemini-2.0-flash").generate_content(prompt)
    return response.text


root_agent = Agent(
    name="shopping_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to enhance shopping experience for users."
    ),
    instruction=(
        "You are Wally - a helpful shopping agent who can answer user questions about recipes, recommend items based on past purchases and issue budget alerts to users."
    ),
    tools=[recipe_suggester, recommend_items, budget_alert]
)
