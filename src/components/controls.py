import datetime

import streamlit as st
from streamlit.elements.widgets.time_widgets import DateValue, SingleDateValue

def select_start_date(
    label: str = None,
    value: DateValue = None,
    min_value: SingleDateValue = None,
    max_value: SingleDateValue = None,
):
    # Set default values
    if label is None:
        label = "Start Date"
    if value is None:
        value = datetime.date.today() - datetime.timedelta(days=7)
    if min_value is None:
        min_value = datetime.date.today() - datetime.timedelta(days=1095)
    if max_value is None:
        max_value = datetime.date.today()

    # Create a date input
    startDate = st.date_input(
        label=label, value=value, min_value=min_value, max_value=max_value
    )

    return startDate


def select_end_date(
    label: str = None,
    value: DateValue = None,
    min_value: SingleDateValue = None,
    max_value: SingleDateValue = None,
):
    # Set default values
    if label is None:
        label = "End Date"
    if value is None:
        value = datetime.date.today()
    if min_value is None:
        min_value = datetime.date.today() - datetime.timedelta(days=365)
    if max_value is None:
        max_value = datetime.date.today()

    # Create a date input
    endDate = st.date_input(
        label=label, value=value, min_value=min_value, max_value=max_value
    )

    return endDate
