import streamlit as st
import pandas as pd
import logic

# --- LOAD THE DATABASE WITH SAFETY NET ---
@st.cache_data
def load_data():
    try:
        # Try to read the file
        return pd.read_excel('transport_database.xlsx')
    except FileNotFoundError:
        # If the file is missing, return 'None' instead of crashing
        return None

# Load the database
df = load_data()

# --- HEADER ---
st.title("🚗 Smart Transport Allocator")
st.write("Demonstrating modular software architecture (Logic separated from UI).")
st.write("---")

# --- SAFETY CHECK ---
# If 'df' is None, it means the Excel file wasn't found. 
# We show a warning and use st.stop() to halt the rest of the app.
if df is None:
    st.error("🚨 **System Error:** Could not find `transport_database.xlsx`. Please ensure the Excel file is in the same folder as this application.")
    st.stop()

# --- USER INPUT ---
persons = st.number_input("Enter number of persons:", min_value=0, value=3, step=1)

# --- EXECUTE CALCULATION ---
if st.button("Find Transport", type="primary"):
    
    st.subheader("Allocation Results")
    
    # Hand the database and input over to logic.py
    result = logic.determine_vehicle(df, persons)
    
    # If logic.py successfully found a vehicle...
    if result["found"] == True:
        st.info(f"**Input (A):** You have **{result['input_a']}** persons.")
        
        # Since you gave Train a real capacity (720), we don't need the special text anymore.
        # It will just cleanly output "Next suitable capacity is 720 persons."
        st.success(f"**Database Match (B):** Next suitable capacity is **{result['match_b']}** persons.")
        st.success(f"**Final Output (C):** You need a **{result['output_c']}**.")
        
    # If logic.py failed (e.g., user typed 800 people)...
    else:
        st.error(f"**Error:** {result['error_msg']}")

# --- SHOW THE DATABASE ---
#st.write("---")
#st.write("### Live Database Connection")

# Using the exact column names from your image for the display table
# display_df = df[['Group_Size', 'Assigned_Vehicle']]
# st.dataframe(display_df, hide_index=True)