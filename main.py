import streamlit as st

# Function to perform basic arithmetic operations
def calculate(operation, num1, num2=0):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

# Main function to run the Streamlit app
def main():
    st.title("Basic Calculator")

    st.sidebar.title("Calculator Options")

    # Sidebar for selecting the operation
    operation = st.sidebar.selectbox("Operation", [
        "Addition", "Subtraction", "Multiplication", "Division"
        ])

    # Input fields for the numbers
    num1 = st.number_input("Enter the first number", value=0.0, step=1.0, format="%.2f")
    num2 = st.number_input("Enter the second number", value=0.0, step=1.0, format="%.2f")        

    # Perform calculation when the button is clicked
    if st.button("Calculate"):
        result = calculate(operation, num1, num2)
        # Checking if result is string or not, if it is string then it will show result as an error message.
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"The result of {operation} is {result:.3f}")

    # Reset function
    if st.button("Reset"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()