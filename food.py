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
    cuisine_type = st.selectbox("Select a cuisine type", ['Any', 'American', 'Italian', 'Chinese', 'Indian', 'Mexican', 'Japanese', 'French', 'Thai', 'Other'])

    # Display an additional text input field if the user selects 'Other'
    if cuisine_type == 'Other':
        other_cuisine = st.text_input("Please specify the cuisine type")
        if other_cuisine:
            cuisine_type = other_cuisine

    calories = st.number_input("Calorie limit", min_value=0, step=10, format="%d")
    ingredients = st.text_input("Preferred ingredients (comma-separated)")
    allergies = st.text_input("Any allergies?")
    nutritional_goals = st.text_input("Nutritional goals (e.g., low-carb, high-protein)")
    skill_level = st.selectbox("Your cooking skill level", ['Beginner', 'Intermediate', 'Advanced'])

   # Context for AI generation based on the user's input
    context = f"Generate a recipe suggestion based on craving: {craving}, cuisine type: {cuisine_type}, " \
              f"calorie limit: {calories}, ingredients: {ingredients}, allergies: {allergies}, " \
              f"nutritional goals: {nutritional_goals}, skill level: {skill_level}. " \
              "Please include the nutritional information."
    question = "What should I cook?"

    # Button to generate response
    if st.button("Find Recipe"):
    if question and context:
        response = await generate_response(question, context)
        recipe, nutrition = response.split('\n\n', 1)
        st.write("Suggested Recipe:")
        st.write(recipe)
        st.write("Nutritional Information:")
        st.markdown(f"**Nutritional Details:**\n{nutrition.replace(', ', '\n')}", unsafe_allow_html=True)
    else:
        st.error("Please make sure you don't leave any field blank.")

# Run the app
if __name__ == "__main__":
    import asyncio
    asyncio.run(app())
