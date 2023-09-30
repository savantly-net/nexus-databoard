import streamlit as st

from .i_render import IRender


class DefaultFooter(IRender):
    def __init__(self, footerContent: IRender = None):
        self.footerContent = footerContent

    def render(self):
        if self.footerContent is not None:
            self.footerContent.render()
        else:
            st.write("")
