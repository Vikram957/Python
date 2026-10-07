import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="Stone Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# Initialize scores
if "uscore" not in st.session_state:
    st.session_state.uscore = 0

if "cscore" not in st.session_state:
    st.session_state.cscore = 0

if "result" not in st.session_state:
    st.session_state.result = "Choose your move!"

if "user_choice" not in st.session_state:
    st.session_state.user_choice = "-"

if "comp_choice" not in st.session_state:
    st.session_state.comp_choice = "-"


# Game function
def play(user):
    comp = random.randint(1, 3)

    choices = {
        1: "🪨 Stone",
        2: "📄 Paper",
        3: "✂️ Scissors"
    }

    st.session_state.user_choice = choices[user]
    st.session_state.comp_choice = choices[comp]

    if user == 1 and comp == 3:
        st.session_state.result = "🎉 You won this round!"
        st.session_state.uscore += 1

    elif user == 2 and comp == 1:
        st.session_state.result = "🎉 You won this round!"
        st.session_state.uscore += 1

    elif user == 3 and comp == 2:
        st.session_state.result = "🎉 You won this round!"
        st.session_state.uscore += 1

    elif user == comp:
        st.session_state.result = "🤝 Draw!"

    else:
        st.session_state.result = "💻 Computer won this round!"
        st.session_state.cscore += 1


# Reset function
def reset_game():
    st.session_state.uscore = 0
    st.session_state.cscore = 0
    st.session_state.result = "Choose your move!"
    st.session_state.user_choice = "-"
    st.session_state.comp_choice = "-"


# ---------------- UI ----------------

st.title("🪨 📄 ✂️ Stone Paper Scissors")

st.subheader("First player to reach 5 points wins!")

# Score
col1, col2 = st.columns(2)

with col1:
    st.metric("👤 Your Score", st.session_state.uscore)

with col2:
    st.metric("💻 Computer Score", st.session_state.cscore)


st.divider()

# Choices
col1, col2 = st.columns(2)

with col1:
    st.info(f"**Your Choice:**\n\n{st.session_state.user_choice}")

with col2:
    st.warning(f"**Computer Choice:**\n\n{st.session_state.comp_choice}")


# Result
st.subheader(st.session_state.result)


st.divider()

# Check if game is over
game_over = (
    st.session_state.uscore >= 5
    or st.session_state.cscore >= 5
)

# Game buttons
st.write("### Choose your move:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Stone", use_container_width=True, disabled=game_over):
        play(1)
        st.rerun()

with col2:
    if st.button("📄 Paper", use_container_width=True, disabled=game_over):
        play(2)
        st.rerun()

with col3:
    if st.button("✂️ Scissors", use_container_width=True, disabled=game_over):
        play(3)
        st.rerun()


# Winner message
if st.session_state.uscore >= 5:
    st.success("🏆 YOU WON THE GAME!")

elif st.session_state.cscore >= 5:
    st.error("💻 COMPUTER WON THE GAME!")


# Reset button
st.divider()

if st.button("🔄 New Game", use_container_width=True):
    reset_game()
    st.rerun()