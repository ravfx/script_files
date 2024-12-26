import nuke

def list_read_node_paths():
    read_nodes = [node for node in nuke.allNodes() if node.Class() == "Read"]
    if not read_nodes:
        nuke.message("No Read nodes found in the script.")
        return
    
    file_paths = [node["file"].value() for node in read_nodes]
    
    message = "Read Node File Paths:\n\n" + "\n".join(file_paths)
    nuke.message(message)

# 実行
list_read_node_paths()

