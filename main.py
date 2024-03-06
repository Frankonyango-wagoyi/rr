import streamlit as st
from streamlit_option_menu import option_menu

# Import modules for different sections of the app
import auth
import landing_page
import explore
import bookings
import categories
import search
import account
import rural_connect_ai

with st.sidebar:
    selected: str = option_menu("rr ",
                                ['Home', "Explore", "sales", 'Categories', 'Search', "Account"],
                                default_index=0)

# Based on the user's selection, call the appropriate module/function
if selected == 'Home':
    landing_page.landing()
elif selected == 'Explore':
    explore.explore_services()
elif selected == 'Bookings':
    bookings.show_bookings()
elif selected == 'Categories':
    categories.display_categories()
elif selected == 'Search':
    search.perform_search()
elif selected == 'Account':
    auth.authenticate_user()
elif selected == 'Rural Connect AI':
    rural_connect_ai.run_ai_features()
