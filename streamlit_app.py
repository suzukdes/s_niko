import streamlit as st
import math

def calculate_pi(num_digits):
    return round(math.pi, num_digits)

def main():
    st.title("円周率（π）の計算")

    num_digits = st.slider("小数点以下の桁数を選択してください:", 1, 20, 5)

    pi_value = calculate_pi(num_digits)

    st.write(f"円周率（π）の値は {pi_value} です。")

if __name__ == "__main__":
    main()
