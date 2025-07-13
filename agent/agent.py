from google.adk.agents import Agent
import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()
# GEMINI_KEY = os.getenv("API_KEY")

# Initialize Gemini model
# genai.configure(api_key="YOUR_GEMINI_API_KEY")


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

# Register tools with agent
# agent.register(recipe_suggester)
# agent.register(recommend_items)
# agent.register(budget_alert)

# --- Run demo session ---


def run_demo():
    print("Welcome to Wally (demo mode) 👋")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = root_agent(user_input)
        print(f"Wally: {response.text}")


root_agent = Agent(
    name="shopping_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to enhance shopping experience for users."
    ),
    instruction=(
        "You are a helpful shopping agent who can answer user questions about recipes, recommend items based on past purchases and issue budget alerts to users."
    ),
    tools=[recipe_suggester, recommend_items, budget_alert]
)
