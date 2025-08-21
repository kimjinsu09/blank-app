import streamlit as st
import random

# Initializing session state variables
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'result_message' not in st.session_state:
    st.session_state.result_message = ""

def play_game(user_choice):
    """
    Play one round of the game and update the scores.
    """
    choices = ['가위', '바위', '보']
    computer_choice = random.choice(choices)

    st.session_state.result_message = f"나: {user_choice} vs 컴퓨터: {computer_choice}"

    # Determine the winner
    if user_choice == computer_choice:
        st.session_state.result_message += "\n\n**비겼습니다!**"
    elif (user_choice == '가위' and computer_choice == '보') or \
         (user_choice == '바위' and computer_choice == '가위') or \
         (user_choice == '보' and computer_choice == '바위'):
        st.session_state.user_score += 1
        st.session_state.result_message += "\n\n**이겼습니다! 축하합니다!** 🎉"
    else:
        st.session_state.computer_score += 1
        st.session_state.result_message += "\n\n**졌습니다... 다음에 다시 도전하세요!**"

def reset_game():
    """
    Reset the game state (scores and message).
    """
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result_message = ""
    
# Main Streamlit app logic
st.title("가위바위보 게임 ✊✋✌️")

st.markdown("### 🎲 게임 방법")
st.markdown("아래 버튼 중 하나를 눌러 게임을 시작하세요.")

# Columns for buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('가위 ✌️'):
        play_game('가위')
with col2:
    if st.button('바위 ✊'):
        play_game('바위')
with col3:
    if st.button('보 ✋'):
        play_game('보')

st.markdown("---")

# Display results
st.header("결과")
st.markdown(st.session_state.result_message)

st.markdown("---")

# Display current score
st.header("점수")
st.write(f"나: **{st.session_state.user_score}점**")
st.write(f"컴퓨터: **{st.session_state.computer_score}점**")

# Reset button
if st.button('게임 초기화'):
    reset_game()
    st.experimental_rerun()