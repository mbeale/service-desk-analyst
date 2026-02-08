import sys
import collections

def render_graph(dot_content):
    adj = collections.defaultdict(list)
    nodes = set()
    
    for line in dot_content.splitlines():
        if "->" in line:
            parts = line.strip().split("->")
            src = parts[0].strip().strip('"')
            dst = parts[1].strip().strip(';').strip('"')
            adj[src].append(dst)
            nodes.add(src)
            nodes.add(dst)

    print("\n=== Knowledge Map (Adjacency List) ===")
    if not nodes:
        print("No connections found.")
        return

    for node in sorted(nodes):
        links = adj.get(node, [])
        if links:
            print(f" {node}")
            for i, link in enumerate(links):
                char = "└──" if i == len(links) - 1 else "├──"
                print(f"   {char} {link}")
        else:
            # Check if it's a leaf node that is pointed to but has no outgoing
            is_leaf = False
            for src in adj:
                if node in adj[src]:
                    is_leaf = True
                    break
            if not is_leaf:
                print(f" {node} (Isolated)")

if __name__ == "__main__":
    content = sys.stdin.read()
    render_graph(content)

