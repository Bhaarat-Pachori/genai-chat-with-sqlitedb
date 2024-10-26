from dotenv import load_dotenv

## load all the environment variables
load_dotenv()

import streamlit as st
import os

import google.generativeai as gen

from import_csv_to_sqlite import SqliteConnect
from prompt import prompt, carrier, origin, destination


sql = SqliteConnect()
sql.make_connection(db_name='flights.db')
connection, cursor = sql.get_connect_n_cursor()


# Configure Genai Key
gen.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def natural_lang_to_query(question, prompt):
    model=gen.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


def query_db(query: str, db_name: str):
    rows = cursor.execute(query)
    chunk_size = 100  # Adjust this based on your needs
    while True:
        rows = cursor.fetchmany(chunk_size)
        if not rows:
            break  # No more rows to fetch

        for row in rows:
            # Process each row in the chunk (e.g., print, analyze, etc.)
            yield row


## Streamlit App
st.set_page_config(page_title="2013 Flights Data made easy!!")
st.header("Ask a question")

with st.sidebar:
    image = "ap.png"
    st.sidebar.image(image, use_column_width=True)
    st.header("Flights Meta-Info")
    with st.sidebar.expander("Carrier"):
        for item in carrier:
            st.write(f"- {item}")
    with st.sidebar.expander("Origin Airport"):
        for item in origin:
            st.write(f"- {item}")
    with st.sidebar.expander("Destination Airport"):
        for item in destination:
            st.write(f"- {item}")

question=st.text_input("Input: ",key="input")
submit=st.button("Answer")

# if submit is clicked
if submit:
    query = natural_lang_to_query(question, prompt)
    # print(query)
    response = query_db(query, 'flights.db')
    st.subheader('Equivalent SQL query')
    st.write(query)
    st.subheader("Insights about your query")
    # Create a scrollable container
    with st.container():
        st.markdown(
            """
            <div style="height:25px; overflow-y: auto;">
            """,
            unsafe_allow_html=True,
        )
        # Add your expanders within the container
        with st.expander("Show Detailed Response"):
            for row in response:
                st.write(row)

        st.markdown("</div>", unsafe_allow_html=True)
