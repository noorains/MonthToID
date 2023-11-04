import streamlit as st
from datetime import datetime, timedelta

def id_to_month_year(month_id, base_year=1990, base_month=1):
    # Calculate the target year and month based on the month ID
    target_year = base_year + (month_id - 1) // 12
    target_month = (base_month + (month_id - 1) % 12) % 12
    if target_month == 0:
        target_month = 12
        target_year -= 1

    # Construct the target date
    target_date = datetime(target_year, target_month, 1)

    return target_date.strftime("%B %Y")

st.title("ID to Month-Year Converter")

month_id = st.number_input("Enter the month ID (1 for January 1990, 2 for February 1990, and so on):", min_value=1, value=1)

if st.button("Convert"):
    result = id_to_month_year(month_id)
    st.write(f"The corresponding date is: {result}")

st.write("Note: 1 = January 1990, 2 = February 1990, and so on.")
