from google.adk.agents import Agent
import google.generativeai as genai
from mongo import find_userdata, find_previously_bought, find_cart_items, find_budget


# --- Tools ---

def recipe_suggester(ingredients: str) -> str:
    """Suggest recipes based on user-provided ingredients."""
    # In real app, you’d query a recipe DB. For now, keep it simple.
    example_prompt = f"Suggest 2 easy recipes using these ingredients: {ingredients}"
    response = genai.GenerativeModel(
        "gemini-2.0-flash").generate_content(example_prompt)
    return response.text


def access_cart_items(name: str) -> str:
    items = find_cart_items(name)
    return items


def recommend_items(name: str) -> str:
    """Recommend items based on past purchases."""
    purchase_history = find_previously_bought(name)
    if not purchase_history:
        return "Could not find any past purchases for this user to recommend based on."

    prompt = f"Based on the following past purchases, suggest one or two more products to the user: {purchase_history}"
    response = genai.GenerativeModel(
        "gemini-2.0-flash").generate_content(prompt)
    return response.text


def budget_alert(name: str) -> str:
    """Estimate total and alert if cart exceeds budget."""
    budget = find_budget(name)
    cart_items = find_cart_items(name)

    prompt = f"These are the cart items and prices: {cart_items}. The budget is ₹{budget}. Is the total over budget?"
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
    tools=[recipe_suggester, access_cart_items, recommend_items, budget_alert]
)
