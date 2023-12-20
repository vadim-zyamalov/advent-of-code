import graphviz as gv

G = gv.Digraph()
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        src, dests = line.split(" -> ")
        dests = [el.strip() for el in dests.split(",")]
        nsrc = src[1:] if src[0] in "&%" else src
        for dest in dests:
            G.edge(nsrc, dest)
        G.node(nsrc, src)

G.format = "png"
G.render("Graph", view=True)
