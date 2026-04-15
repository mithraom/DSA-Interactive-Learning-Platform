from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sorting")
def sorting():
    return render_template("sorting.html")

@app.route("/searching")
def searching():
    return render_template("searching.html")

# STACK PAGE
@app.route("/stack")
def stack():
    return render_template("stack.html")

# QUEUE PAGE
@app.route("/queue")
def queue():
    return render_template("queue.html")

# LEVEL 3 PAGE
@app.route("/level3")
def level3():
    return render_template("level3.html")

# LEVEL 4 PAGE
@app.route("/level4")
def level4():
    return render_template("level4.html")

# TREES
@app.route("/binary_tree")
def binary_tree():
    return render_template("binary_tree.html")

@app.route("/bst")
def bst():
    return render_template("bst.html")

@app.route("/avl")
def avl():
    return render_template("avl.html")

@app.route("/red_black")
def red_black():
    return render_template("red_black.html")

@app.route("/min_heap")
def min_heap():
    return render_template("min_heap.html")

@app.route("/max_heap")
def max_heap():
    return render_template("max_heap.html")

@app.route("/m_way")
def m_way():
    return render_template("m_way.html")

@app.route('/b_tree')
def b_tree():
    return render_template('b_tree.html')

@app.route("/graph")
def graph():
    return render_template("graph.html")

@app.route("/hashing")
def hashing():
    return render_template("hashing.html")

@app.route("/nqueens")
def nqueens():
    return render_template("nqueens.html")

@app.route("/dp")
def dp():
    return render_template("dp.html")

@app.route("/greedy")
def greedy():
    return render_template("greedy.html")

@app.route("/tsp")
def tsp():
    return render_template("tsp.html")


if __name__ == "__main__":
    app.run(debug=True)