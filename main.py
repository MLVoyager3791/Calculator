import streamlit as st
import math

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
    elif operation == "Square Root":
        if num1 < 0:
            return "Error: Negative number"
        return math.sqrt(num1)
    elif operation == "Exponentiation":
        return num1 ** num2
    elif operation == "Sine":
        return math.sin(math.radians(num1))
    elif operation == "Cosine":
        return math.cos(math.radians(num1))
    elif operation == "Tangent":
        return math.tan(math.radians(num1))

# Main function to run the Streamlit app
def main():
    st.title("Calculator")

    st.sidebar.title("Calculator Options")

    # Sidebar for selecting the operation
    operation = st.sidebar.selectbox("Operation", [
        "Addition", "Subtraction", "Multiplication", "Division", "Square Root", "Exponentiation", "Sine", "Cosine", "Tangent"
        ])

    # Input fields for the numbers
    num1 = st.number_input("Enter the first number", value=0.0, step=1.0, format="%.2f")
    num2 = 0  # Default value for operations needing one number
    if operation not in ["Square Root", "Sine", "Cosine", "Tangent"]:
        num2 = st.number_input("Enter the second number", value=0.0, step=1.0, format="%.2f")

    # Perform calculation when the button is clicked
    if st.button("Calculate"):
        result = calculate(operation, num1, num2)
        # Checking if result is string or not, if it is string then it will show result as an error message.
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"The result of {operation} is {result:.3f}")

    # Memory functions
    st.sidebar.subheader("Memory Functions")
    if "memory" not in st.session_state:
        st.session_state.memory = 0

    if st.sidebar.button("Store in Memory"):
        # Stores the first number in the memory
        st.session_state.memory = num1
        st.sidebar.success(f"Stored {num1} in memory")

    if st.sidebar.button("Recall from Memory"):
        # Recalling the stored value from memory and displaying it
        st.sidebar.success(f"Recalled {st.session_state.memory} from memory")
        st.write(f"Recalled value from memory: {st.session_state.memory}")

    if st.sidebar.button("Clear Memory"):
        # Clears the memory
        st.session_state.memory = 0
        st.sidebar.success("Cleared memory")

    # Reset function
    if st.button("Reset"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
