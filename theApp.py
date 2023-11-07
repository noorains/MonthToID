import streamlit as st
from datetime import datetime, timedelta

# Define a dictionary to map month names to their corresponding numbers
month_name_to_number = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

def month_year_to_id(month, year, base_year=1980):
    try:
        # Convert the selected month and year to a date
        selected_date = datetime(int(year), month_name_to_number[month], 1)

        # Calculate the month ID
        base_date = datetime(base_year, 1, 1)
        month_id = ((selected_date.year - base_date.year) * 12) + (selected_date.month - base_date.month) + 1

        return month_id
    except (ValueError, KeyError):
        return None

def id_to_month_year(month_id, base_year=1980):
    # Calculate the target year and month based on the month ID
    target_year = base_year + (month_id - 1) // 12
    target_month = ((month_id - 1) % 12) + 1

    # Construct the target date
    target_date = datetime(target_year, target_month, 1)

    return target_date.strftime("%B %Y")

st.title("Month Converter")

conversion_option = st.sidebar.radio("Select Conversion:", ["Month Name to Month ID", "Month ID to Month Name"])

if conversion_option == "Month Name to Month ID":
    st.header("Convert Month Name to Month ID")
    # Create drop-down menus for month and year
    selected_month = st.selectbox("Select a month:", list(month_name_to_number.keys()), index=0)
    selected_year = st.selectbox("Select a year:", list(range(1980, 2051)), index=0)

    # Convert selected month and year to month ID
    month_id = month_year_to_id(selected_month, selected_year)

    if month_id is not None:
        if st.button("Convert"):
            st.markdown(f"<p style='font-size:24px;'><b>For {selected_month} {selected_year}, the corresponding month ID is {month_id}</b></p>", unsafe_allow_html=True)
    else:
        st.error("Please select a valid month and year.")
else:
    st.header("Convert Month ID to Month Name")
    month_id = st.number_input("Enter the month ID (1 = January 1980, 2 = February 1980, and so on):", min_value=1, value=1)

    if month_id is not None:
        if st.button("Convert"):
            result = id_to_month_year(month_id)
            st.markdown(f"<p style='font-size:24px;'><b>For month ID {month_id}, the corresponding month is {result}</b></p>", unsafe_allow_html=True)
    else:
        st.error("Please enter a valid month ID.")

st.write("Note: 1 = January 1980, 2 = February 1980, and so on.")