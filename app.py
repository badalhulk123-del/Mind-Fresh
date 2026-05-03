import streamlit as st
)

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

with col1:
    play = st.button("🎯 Submit Guess", use_container_width=True)

with col2:
    restart = st.button("🔄 Restart", use_container_width=True)

# ---------------- RESTART ----------------
if restart:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.success("Game Restarted Successfully!")

# ---------------- GAME LOGIC ----------------
if play:

    st.session_state.attempts += 1

    if guess == st.session_state.secret_number:

        st.balloons()
        st.snow()

        st.success("🎉 Congratulations! You Won!")

        time.sleep(1)

        st.markdown(
            '<div class="win">💖 I Like You 💖</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"<h3 style='text-align:center;color:white;'>You guessed it in {st.session_state.attempts} attempts!</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2 style='text-align:center;'>❤️ ❤️ ❤️ ❤️ ❤️</h2>",
            unsafe_allow_html=True
        )

        # Reset automatically
        st.session_state.secret_number = random.randint(1, 10)
        st.session_state.attempts = 0

    elif guess < st.session_state.secret_number:
        st.warning("📉 Too Low! Try Higher")

    else:
        st.warning("📈 Too High! Try Lower")

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Made with ❤️ using Streamlit</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
