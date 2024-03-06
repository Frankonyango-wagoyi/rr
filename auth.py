import streamlit as st

def register():
    st.title("User Registration")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if password != confirm_password:
        st.error("Passwords do not match.")
        return

    if st.button("Register"):
        # Add your registration logic here (e.g., storing user data in a database)
        st.success("Registration successful. Please log in.")

def login():
    st.title("User Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Simulating authentication
        if username == "example_user" and password == "password":
            st.success("Login successful!")
            # Set a session variable to indicate the user is logged in
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password.")

def main():
    st.title("Welcome to RuralConnect")

    # Check if the user is already logged in
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.write("You are already logged in.")
    else:
        register_or_login = st.radio("Choose an option:", ("Register", "Login"))

        if register_or_login == "Register":
            register()
        elif register_or_login == "Login":
            login()

if __name__ == "__main__":
    main()
