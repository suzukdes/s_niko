import streamlit as st
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分けです！"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "あなたの勝ちです！"
    else:
        return "コンピューターの勝ちです！"

def main():
    st.title("じゃんけんゲーム")
    
    user_choice = st.radio("あなたの選択:", ("rock", "paper", "scissors"))

    computer_choice = random.choice(["rock", "paper", "scissors"])

    if st.button("結果を見る"):
        st.write("あなたの選択:", user_choice)
        st.write("コンピューターの選択:", computer_choice)
        st.write(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
