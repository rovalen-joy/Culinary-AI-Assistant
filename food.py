import streamlit as st
import openai

client = openai.ChatCompletion.create(
    api_key=st.secrets["API_key"],
)

def generate_response(question, context):
    model = "gpt-3.5-turbo"
    response = client.create(
        model=model,
        messages=[{"role": "user", "content": question},
                  {"role": "system", "content": context}]
    )
    return response.choices[0].message['content']

def app():
    st.title("Culinary AI Assistant")

    # Text area input for the user to specify cravings, calories, etc.
    craving = st.text_input("What are you craving? (e.g., 'something sweet')")
    calories = st.number_input("Calorie limit", min_value=0, step=10, format="%d")
    ingredients = st.text_input("Preferred ingredients (comma-separated)")
    allergies = st.text_input("Any allergies?")
    nutritional_goals = st.text_input("Nutritional goals (e.g., low-carb, high-protein)")
    skill_level = st.selectbox("Your cooking skill level", ['Beginner', 'Intermediate', 'Advanced'])

    # Button to generate response
    if st.button("Find Recipe"):
        context = f"Generate a recipe suggestion based on craving: {craving}, calorie limit: {calories}, " \
                  f"ingredients: {ingredients}, allergies: {allergies}, nutritional goals: {nutritional_goals}, " \
                  f"skill level: {skill_level}."
        question = "What should I cook?"
        response = generate_response(question, context)
        st.write("Suggested Recipe:")
        st.write(response)

# Run the app
if __name__ == "__main__":
    app()
