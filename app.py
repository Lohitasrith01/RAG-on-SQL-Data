import streamlit as st
from services.llm_service import generate_sql
from services.db_service import execute_sql

st.title("SQL-Based RAG System")
st.subheader("Ask questions about student data in plain English!")

user_query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    try:
        sql_query = generate_sql(user_query)
        st.write("Generated SQL Query:", sql_query)

        results = execute_sql(sql_query)
        if results:
            st.write("Query Results:")
            for row in results:
                st.write(row)
        else:
            st.write("No results found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
