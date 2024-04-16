import streamlit as st
import time

# ハノイの塔の解を計算する再帰関数
def hanoi_tower(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        time.sleep(1)  # アニメーションのために1秒待機
        return
    hanoi_tower(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    time.sleep(1)  # アニメーションのために1秒待機
    hanoi_tower(n-1, auxiliary, target, source)

def main():
    st.title("ハノイの塔アプリケーション")

    # ディスクの数を選択
    num_disks = st.slider("ディスクの数を選択してください:", 1, 10, 3)

    if st.button("ハノイの塔を解く"):
        st.write("ハノイの塔の解決手順:")
        hanoi_tower(num_disks, 'A', 'C', 'B')
        st.write("ハノイの塔の解決が完了しました！")

if __name__ == "__main__":
    main()
