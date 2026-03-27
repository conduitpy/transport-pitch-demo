import streamlit as st
import pandas as pd
import logic


@st.cache_data
def load_data():
    try:
        return pd.read_excel('transport_database.xlsx')
    except FileNotFoundError:
        return None

df = load_data()

st.title("🚗 Smart Transport Allocator")
st.write("Demonstrating modular software architecture (Logic separated from UI).")
st.write("---")

if df is None:
    st.error("🚨 **System Error:** Could not find `transport_database.xlsx`. Please ensure the Excel file is in the same folder as this application.")
    st.stop()

persons = st.number_input("Enter number of persons:", min_value=0, value=3, step=1)

if st.button("Find Transport", type="primary"):
    st.subheader("Allocation Results")
    result = logic.determine_vehicle(df, persons)
    
    if result["found"] == True:
        st.info(f"**Input (A):** You have **{result['input_a']}** persons.")
        st.success(f"**Database Match (B):** Next suitable capacity is **{result['match_b']}** persons.")
        st.success(f"**Final Output (C):** You need a **{result['output_c']}**.")
        
    else:
        st.error(f"**Error:** {result['error_msg']}")
