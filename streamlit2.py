import streamlit as st

def find_largest_number(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

def main():
    st.title("TDS W8 Largest Number")
    st.write("Enter 3 numbers.")

    num1 = st.number_input("first number:")
    num2 = st.number_input("second number:")
    num3 = st.number_input("third number:")

    if st.button("find largest number"):
        largest = find_largest_number(num1, num2, num3)
        st.success(f"largest is: {largest}")

if __name__ == "__main__":
    main()
