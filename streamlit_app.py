
import re
from datetime import date, time, datetime
from urllib.parse import quote

import streamlit as st

WHATSAPP_NUMBER = "919440882425"

START_DATETIME = datetime(2026, 10, 28, 9, 0)
END_DATETIME = datetime(2026, 10, 30, 19, 0)

st.set_page_config(
    page_title="Theja & Swetha Wedding Vehicle Arrangement",
    page_icon="💒",
    layout="centered",
)

st.title("💒 Theja & Swetha Wedding Vehicle Arrangement")

st.write(
    "Welcome! Please provide your details below "
    "if you need transportation for the wedding."
)

st.info(
    "Available travel window: "
    "28 October 2026, 9:00 AM to "
    "30 October 2026, 7:00 PM."
)

st.divider()

with st.form("vehicle_request_form"):
    st.subheader("Guest Details")

    name = st.text_input(
        "Guest Name *",
        placeholder="Enter your full name",
    )

    contact = st.text_input(
        "Contact Number *",
        placeholder="Enter your mobile number",
    )

    st.subheader("Travel Details")

    booking_date = st.date_input(
        "Travel Date *",
        value=date(2026, 10, 28),
        min_value=date(2026, 10, 28),
        max_value=date(2026, 10, 30),
    )

    booking_time = st.time_input(
        "Pickup Time *",
        value=time(9, 0),
        step=300,
    )

    passengers = st.number_input(
        "Number of Passengers",
        min_value=1,
        max_value=100,
        value=2,
        step=1,
    )

    additional_info = st.text_area(
        "Additional Requirements (Optional)",
        placeholder="Enter any additional requirements...",
    )

    submitted = st.form_submit_button(
        "Continue to WhatsApp",
        use_container_width=True,
    )

if submitted:
    name = name.strip()
    contact = contact.strip()

    selected_datetime = datetime.combine(
        booking_date,
        booking_time,
    )

    if not name:
        st.error("Please enter the guest name.")

    elif not re.fullmatch(r"\+?[\d\s()-]{10,20}", contact):
        st.error("Please enter a valid contact number.")

    elif not WHATSAPP_NUMBER.isdigit():
        st.error("Please configure a valid WhatsApp number.")

    elif not START_DATETIME <= selected_datetime <= END_DATETIME:
        st.error(
            "Please select a date and time between "
            "28-10-2026 9:00 AM and 30-10-2026 7:00 PM."
        )

    else:
        message = (
            "💒 THEJA & SWETHA WEDDING VEHICLE REQUIREMENT\n\n"
            f"Guest Name: {name}\n"
            f"Contact Number: {contact}\n"
            f"Travel Date: {booking_date.strftime('%d-%m-%Y')}\n"
            f"Pickup Time: {booking_time.strftime('%I:%M %p')}\n"
            f"Number of Passengers: {passengers}\n"
            f"Additional Requirements: "
            f"{additional_info.strip() or 'None'}"
        )

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}"
            f"?text={quote(message)}"
        )

        st.markdown(
            f"**[Open WhatsApp to send your request]({whatsapp_url})**"
        )

        st.caption(
            "Click the link above, then press Send in WhatsApp."
        )

st.divider()

st.caption(
    "Please submit your transportation requirements in advance. "
    "Vehicle availability will be confirmed separately."
)
