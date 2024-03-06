# explore.py

import streamlit as st


# Function to display available services for exploration
def explore_services():
    st.title("Explore Services")

    # Dummy data for available services
    services = [
        {"name": "Plumbing Services", "description": "Professional plumbing solutions for your home or business."},
        {"name": "Electrical Services",
         "description": "Expert electrical services including installations and repairs."},
        {"name": "Medical Services",
         "description": "Access to healthcare professionals for medical consultations and treatments."},
        # Add more services as needed
    ]

    st.subheader("Available Services")

    # Display each service in a card format
    for service in services:
        st.write(f"**{service['name']}**")
        st.write(service['description'])
        st.write("---")
