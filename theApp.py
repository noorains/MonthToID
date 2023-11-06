import streamlit as st
from datetime import datetime

def id_to_month_year(month_id, base_year=1980, base_month=1):
    if month_id == 12:
        target_year = base_year + 1
        target_month = 12
    else:
        # Calculate the target year and month based on the month ID
        target_year = base_year + (month_id - 1) // 12
        target_month = (base_month + (month_id - 1) % 12) % 12
        if target_month == 0:
            target_month = 12
            target_year -= 1

    # Construct the target date
    target_date = datetime(target_year, target_month, 1)

    return target_date.strftime("%B %Y")

st.title("VIEWS Month ID to Month-Year Converter")

month_id = st.number_input("Enter the month ID (1 for January 1980, 2 for February 1980, and so on):", min_value=1, value=1)

if st.button("Convert"):
    result = id_to_month_year(month_id)
    st.markdown(f"<p style='font-size:24px;'><b>The corresponding month for id {month_id} is: {result}</b></p>", unsafe_allow_html=True)

st.write("Note: 1 = January 1980, 2 = February 1980, and so on.")
