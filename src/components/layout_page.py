import streamlit as st

from .i_render import IRender
from .default_header import DefaultHeader
from .default_footer import DefaultFooter


class LayoutPage(IRender):
    def __init__(
        self,
        header: IRender = DefaultHeader(),
        body: IRender = None,
        footer: IRender = DefaultFooter(),
    ):
        self.header = header
        self.body = body
        self.footer = footer

    def render(self):
        self.header.render()
        if self.body is not None:
            self.body.render()
        self.footer.render()
