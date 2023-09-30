from string import Template
import streamlit as st
import config as config
from template_loader import render_template
from authz import authorization
from streamlit_javascript import st_javascript

def set_page_config(page_title: str = config.site_name):
    st.set_page_config(page_title=page_title, page_icon=None, layout='wide', initial_sidebar_state='collapsed',
                    menu_items={
            'About': f'{config.site_description}\nVersion: {config.version}\nLogged in as: {authorization.get_current_user().username}',
        })
    _add_custom_client_code(config.site_name)


def _add_custom_client_code(title: str):

    template_string = f"""
        <style>
            [data-testid="stSidebarNav"]::before {{
                content: "{title}";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 30px;
            }}
            .main > div:first-child {{
                padding-top: 0px;
            }}
        </style>
        """

    # get Jinja template
    #script = render_template("script.js")
    #st_javascript(script, key="chatwoot")

    st.markdown(template_string, unsafe_allow_html=True)
