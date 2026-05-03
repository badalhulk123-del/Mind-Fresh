import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Love Game",
    page_icon="💖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #7f1d1d);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: white;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #f1f5f9;
    margin-bottom: 30px;
}

.box {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.15);
}

.win {
    text-align: center;
    font-size: 70px;
    color: #ff4b6e;
    font-weight: bold;
    animation: pulse 1s infinite;
}

@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.1);}
    100% {transform: scale(1);}
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- GAME UI ----------------

st.markdown('<div class="title">🎮 Love Guess Game</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Guess the secret number between 1 and 10 💖</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="box">', unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------

if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# ---------------- INPUT ----------------

guess = st.number_input(
    "Enter Your Guess",
    min_value=1,
    max_value=10,
    step=1
)

# ---------------- BUTTONS ----------------

col1, col2 = st.columns(2)

with col1:
    play = st.button("🎯 Submit Guess", use_container_width=True)

with col2:
    restart = st.button("🔄 Restart Game", use_container_width=True)

# ---------------- RESTART ----------------

if restart:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.success("Game Restarted!")

# ---------------- GAME LOGIC ----------------

if play:

    st.session_state.attempts += 1

    if guess == st.session_state.secret_number:

        st.balloons()
        st.snow()

        st.success("🎉 Congratulations! You Won!")

        st.markdown(
            '<div class="win">💖 I Like You 💖</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <h3 style='text-align:center;color:white;'>
            You guessed it in {st.session_state.attempts} attempts!
            </h3>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2 style='text-align:center;'>❤️ ❤️ ❤️ ❤️ ❤️</h2>",
            unsafe_allow_html=True
        )

        # Reset game
        st.session_state.secret_number = random.randint(1, 10)
        st.session_state.attempts = 0

    elif guess < st.session_state.secret_number:
        st.warning("📉 Too Low! Try Higher")

    else:
        st.warning("📈 Too High! Try Lower")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown(
    '<div class="footer">Made with ❤️ using Streamlit</div>',
    unsafe_allow_html=True
)
