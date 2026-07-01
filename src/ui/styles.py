import streamlit as st


def load_css():
    """
    Loads custom CSS for the QA AI Assistant.
    """

    st.markdown(
        """
<style>

/* ===========================
Main App
=========================== */

.main {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}


/* ===========================
Hide Streamlit Branding
=========================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* ===========================
Sidebar
=========================== */

[data-testid="stSidebar"]{
    background-color:#f8f9fa;
}

[data-testid="stSidebar"] h1{
    color:#1f2937;
}

[data-testid="stSidebar"] button{
    width:100%;
    border-radius:10px;
}


/* ===========================
Chat Input
=========================== */

.stChatInput{
    position:fixed;
    bottom:15px;
    left:23%;
    width:70%;
}


/* ===========================
Buttons
=========================== */

.stButton>button{

    border-radius:10px;

    height:45px;

    font-weight:600;

}


/* ===========================
Metrics
=========================== */

[data-testid="metric-container"]{

    border-radius:12px;

    border:1px solid #dddddd;

    padding:10px;

}


/* ===========================
Expander
=========================== */

.streamlit-expanderHeader{

    font-weight:bold;

}


/* ===========================
Scrollbar
=========================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#999;

    border-radius:10px;

}


/* ===========================
Code Block
=========================== */

pre{

    border-radius:10px;

}


/* ===========================
Tables
=========================== */

table{

    border-radius:10px;

}


/* ===========================
Markdown
=========================== */

h1,h2,h3{

    color:#1f2937;

}


/* ===========================
Chat Messages
=========================== */

[data-testid="stChatMessage"]{

    padding:15px;

    border-radius:15px;

    margin-bottom:12px;

}

</style>
""",
        unsafe_allow_html=True,
    )