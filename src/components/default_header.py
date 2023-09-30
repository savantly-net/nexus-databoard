from string import Template
import streamlit as st
from config import site_name

from .i_render import IRender

def _hide_streamlit_footer():
    hide_streamlit_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

class DefaultHeader(IRender):
    def __init__(self, headline: str = "# " + site_name):
        self.headline = headline

    def render(self):
        _hide_streamlit_footer()
        if self.headline is not None:
            st.markdown(self.headline)
