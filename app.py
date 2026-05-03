import streamlit as st
    """
    <style>
    .main {
        background: linear-gradient(to right, #ffdde1, #ee9ca7);
    }

    .title {
        text-align: center;
        font-size: 50px;
        color: white;
        font-weight: bold;
    }

    .message {
        text-align: center;
        font-size: 60px;
        color: red;
        font-weight: bold;
        animation: pulse 1s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="title">🎯 Catch The Number Game</p>', unsafe_allow_html=True)

st.write("---")

# Game instructions
st.subheader("🎮 How To Play")
st.write("Guess the correct number between 1 and 5.")
st.write("If you win... a surprise message appears 💖")

# Generate number
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 5)

# User input
user_guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=5,
    step=1
)

# Play button
if st.button("🎯 Submit Guess"):

    if user_guess == st.session_state.secret_number:
        st.balloons()

        st.success("🎉 You Won The Game!")

        time.sleep(1)

        st.markdown(
            '<p class="message">💖 I Like You 💖</p>',
            unsafe_allow_html=True
        )

        st.snow()

        # Reset game
        st.session_state.secret_number = random.randint(1, 5)

    else:
        st.error("❌ Wrong Guess! Try Again")

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.secret_number = random.randint(1, 5)
    st.success("Game Restarted!")
