import streamlit as st
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="DSA Learning Platform",
    layout="wide"
)

# -----------------------------
# FUNCTION TO LOAD HTML FILES
# -----------------------------
def load_html(file_name):
    try:
        file_path = os.path.join("templates", file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return f"<h3>{file_name} not found</h3>"

# -----------------------------
# SIDEBAR NAVIGATION (REPLACES ROUTES)
# -----------------------------
st.sidebar.title("📚 DSA Topics")

page = st.sidebar.selectbox("Navigate", [
    "Home",
    "Sorting",
    "Searching",
    "Stack",
    "Queue",
    "Level 3",
    "Level 4",
    "Binary Tree",
    "BST",
    "AVL Tree",
    "Red Black Tree",
    "Min Heap",
    "Max Heap",
    "M-Way Tree",
    "B-Tree",
    "Graph",
    "Hashing",
    "N-Queens",
    "Dynamic Programming",
    "Greedy",
    "TSP"
])

# -----------------------------
# PAGE ROUTING LOGIC
# -----------------------------
if page == "Home":
    st.markdown(load_html("index.html"), unsafe_allow_html=True)

elif page == "Sorting":
    st.markdown(load_html("sorting.html"), unsafe_allow_html=True)

elif page == "Searching":
    st.markdown(load_html("searching.html"), unsafe_allow_html=True)

elif page == "Stack":
    st.markdown(load_html("stack.html"), unsafe_allow_html=True)

elif page == "Queue":
    st.markdown(load_html("queue.html"), unsafe_allow_html=True)

elif page == "Level 3":
    st.markdown(load_html("level3.html"), unsafe_allow_html=True)

elif page == "Level 4":
    st.markdown(load_html("level4.html"), unsafe_allow_html=True)

elif page == "Binary Tree":
    st.markdown(load_html("binary_tree.html"), unsafe_allow_html=True)

elif page == "BST":
    st.markdown(load_html("bst.html"), unsafe_allow_html=True)

elif page == "AVL Tree":
    st.markdown(load_html("avl.html"), unsafe_allow_html=True)

elif page == "Red Black Tree":
    st.markdown(load_html("red_black.html"), unsafe_allow_html=True)

elif page == "Min Heap":
    st.markdown(load_html("min_heap.html"), unsafe_allow_html=True)

elif page == "Max Heap":
    st.markdown(load_html("max_heap.html"), unsafe_allow_html=True)

elif page == "M-Way Tree":
    st.markdown(load_html("m_way.html"), unsafe_allow_html=True)

elif page == "B-Tree":
    st.markdown(load_html("b_tree.html"), unsafe_allow_html=True)

elif page == "Graph":
    st.markdown(load_html("graph.html"), unsafe_allow_html=True)

elif page == "Hashing":
    st.markdown(load_html("hashing.html"), unsafe_allow_html=True)

elif page == "N-Queens":
    st.markdown(load_html("nqueens.html"), unsafe_allow_html=True)

elif page == "Dynamic Programming":
    st.markdown(load_html("dp.html"), unsafe_allow_html=True)

elif page == "Greedy":
    st.markdown(load_html("greedy.html"), unsafe_allow_html=True)

elif page == "TSP":
    st.markdown(load_html("tsp.html"), unsafe_allow_html=True)