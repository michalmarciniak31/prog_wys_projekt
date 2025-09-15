import streamlit as st
from database.db import Database, DatabaseConfig
from task import TaskRepository

db = Database(DatabaseConfig.from_env())
db.ensure_schema()

st.set_page_config(page_title="Lista zadan", layout="centered")
st.title("Lista zadan")
st.subheader("Dodaj zadanie")

repo = TaskRepository(db)

with st.form("add_form", clear_on_submit=True):
    title = st.text_input("Tytuł", placeholder="np. Tutaj wpisz zadanie")
    ok = st.form_submit_button("Dodaj", use_container_width=True)
    if ok and title:
        repo.add(title)
        st.rerun()

st.subheader("Twoje zadania:")
rows = repo.list()
if not rows:
    st.info("Brak zadan")
else:
    for task_id, title, done in rows:
        col_chk, col_title, col_toggle, col_del = st.columns([0.08, 0.52, 0.20, 0.20])

        with col_chk:
            st.checkbox("", value=done, key=f"chk_{task_id}", disabled=True)

        with col_title:
            st.write(title)

        with col_toggle:
            if not done:
                if st.button("Zaznacz", key=f"done_{task_id}", use_container_width=True):
                    repo.set_done(task_id, True)
                    st.rerun()
            else:
                if st.button("Odznacz", key=f"undo_{task_id}", use_container_width=True):
                    repo.set_done(task_id, False)
                    st.rerun()

        with col_del:
            if st.button("Usuń", key=f"del_{task_id}", use_container_width=True):
                repo.delete(task_id)
                st.rerun()