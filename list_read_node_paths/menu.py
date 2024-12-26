import list_read_node_paths  # スクリプトのインポート

# カスタムメニューを作成
toolbar = nuke.toolbar("Nodes")
custom_menu = toolbar.addMenu("Custom Tools")
custom_menu.addCommand("List Read Node Paths", "list_read_node_paths.list_read_node_paths()")