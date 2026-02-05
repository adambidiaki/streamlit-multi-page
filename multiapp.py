"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from streamlit_option_menu import option_menu
from screens import data, home, model 

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    # def run(self):
    #     app = st.sidebar.radio(
    #     # app = st.selectbox(
    #         'Navigation',
    #         self.apps,
    #         format_func=lambda app: app['title'])

    #     app['function']()

    def run(self):
    # app = st.sidebar(
        with st.sidebar:     
            app = option_menu(
                menu_title='Pondering',
                options=['Home','Model','Data'],
                icons=['house-fill','person-circle','trophy-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                    })
                
        if app == "Home":
            home.app()
        if app == "Model":
            model.app()    
        if app == "Data":
            data.app()  
        