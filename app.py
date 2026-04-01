import streamlit as st
from db_setup import load_data
from llm_engine import generate_sql, generate_insight
from query_engine import run_query

st.title("🍹 Beverage AI Assistant")

conn = load_data("data/beverages.xlsx")

question = st.text_input("Ask your question:")

if st.button("Run"):
    if question:

        # --- Generate SQL ---
        sql = generate_sql(question)

        st.subheader("Generated SQL")
        st.code(sql)

        # --- Run Query ---
        df, error = run_query(conn, sql)

        if error:
            st.error(error)
        else:
            st.subheader("Results")
            st.dataframe(df)

            st.subheader("Insights")
            st.write(generate_insight(df, question))