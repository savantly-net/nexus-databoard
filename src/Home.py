import streamlit as st

from components.layout_page import LayoutPage
from components.default_header import DefaultHeader
from components.i_render import IRender
import config

import page_setup
page_setup.set_page_config()

header = DefaultHeader(config.home_page_header)

class body(IRender):
    def render(self):
        st.markdown("""
Browse the menu on the left to get started.
""")

page = LayoutPage(header=header, body=body())

page.render()
