
import streamlit as st
from datetime import date, time
from urllib.parse import quote

# WhatsApp number that should receive the message
# Include country code, without + or spaces.
WHATSAPP_RECEIVER = "919440882425"

st.title("Booking Form")

with st.form("booking_form"):
    name = st.text_input("Name")
    selected_date = st.date_input("Date", value=date.today())
    selected_time = st.time_input("Time", value=time(10, 0))
    contact = st.text_input("Contact Number")

    submitted = st.form_submit_button("Submit")

if submitted:
    if not name.strip() or not contact.strip():
        st.error("Please enter your name and contact number.")
    elif not contact.strip().replace("+", "").replace(" ", "").isdigit():
        st.error("Please enter a valid contact number.")
    elif len(contact.strip().replace("+", "").replace(" ", "")) < 10:
        st.error("Contact number must contain at least 10 digits.")
    elif "X" in WHATSAPP_RECEIVER:
        st.error("Please configure your WhatsApp receiver number in app.py.")
    else:
        message = (
            "New Booking Details\n\n"
            f"Name: {name.strip()}\n"
            f"Date: {selected_date.strftime('%d-%m-%Y')}\n"
            f"Time: {selected_time.strftime('%I:%M %p')}\n"
            f"Contact Number: {contact.strip()}"
        )

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_RECEIVER}"
            f"?text={quote(message)}"
        )

        st.success("Details submitted successfully!")
        st.link_button("Send WhatsApp Message", whatsapp_url)
