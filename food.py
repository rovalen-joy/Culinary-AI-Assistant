import streamlit as st
import openai

from openai import AsyncOpenAI
from openai import OpenAI

# Set up the async OpenAI client
client = AsyncOpenAI(api_key=st.secrets["API_key"])

async def generate_response(question, context):
    model = "gpt-3.5-turbo"

    completion = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question},
                  {"role": "system", "content": context}]
    )
    return completion.choices[0].message.content

async def app():
    st.title("Chefmate: A Culinary AI Assistant")

    st.write(
        """
        Welcome to Chefmate! Tell me what you're craving, any dietary preferences or restrictions, and I'll suggest the perfect recipe just for you. 
        Dive into a world of flavors tailored to your taste and nutritional needs.
        """
    )

    st.markdown ("""
    **Submitted By:**
    - Name: Rovalen Joy U. Calaguing
    - Course/Year/Section: BSCS 3A AI
    - Subject: Intelligent Systems (CCS 229)
    """, unsafe_allow_html=True)

    # Collecting user input for the AI to process
    craving = st.text_input("What are you craving? (e.g., 'something sweet')")
    calories = st.number_input("Calorie limit", min_value=0, step=10, format="%d")
    ingredients = st.text_input("Preferred ingredients (comma-separated)")
    allergies = st.text_input("Any allergies?")
    nutritional_goals = st.text_input("Nutritional goals (e.g., low-carb, high-protein)")
    skill_level = st.selectbox("Your cooking skill level", ['Beginner', 'Intermediate', 'Advanced'])

    # Context for AI generation based on the user's input
    context = f"Generate a recipe suggestion based on craving: {craving}, calorie limit: {calories}, " \
              f"ingredients: {ingredients}, allergies: {allergies}, nutritional goals: {nutritional_goals}, " \
              f"skill level: {skill_level}."
    question = "What should I cook?"

    # Button to generate response
    if st.button("Find Recipe"):
        if question and context:
            response = await generate_response(question, context)
            st.write("Suggested Recipe:")
            st.write(response)
        else:
            st.error("Please enter both craving and details.")

# Run the app
if __name__ == "__main__":
    import asyncio
    asyncio.run(app())
