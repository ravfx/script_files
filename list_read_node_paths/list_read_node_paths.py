import nuke
from PySide2 import QtWidgets

def list_read_node_paths():
    # Readノードを取得
    read_nodes = [node for node in nuke.allNodes() if node.Class() == "Read"]
    if not read_nodes:
        nuke.message("No Read nodes found in the script.")
        return

    # ファイルパスを取得
    file_paths = [node["file"].value() for node in read_nodes]
    
    # 重複を排除するためにsetを使用
    unique_paths = set(file_paths)
    
    # フォルダ名でアルファベット順にソート
    sorted_paths = sorted(unique_paths, key=lambda path: path.rsplit("/", 1)[0])
    
    # Qtウィジェットを作成してスクロール可能なリストを表示
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])
    
    dialog = QtWidgets.QDialog()
    dialog.setWindowTitle("Read Node File Paths")
    dialog.setMinimumSize(600, 400)
    
    layout = QtWidgets.QVBoxLayout()
    dialog.setLayout(layout)
    
    # スクロールエリアを設定
    scroll_area = QtWidgets.QScrollArea()
    scroll_area.setWidgetResizable(True)
    layout.addWidget(scroll_area)
    
    # 表示内容を構築
    content_widget = QtWidgets.QWidget()
    content_layout = QtWidgets.QVBoxLayout()
    content_widget.setLayout(content_layout)
    
    for path in sorted_paths:
        # パスをフォルダとファイル名に分割
        folder, file_name = path.rsplit("/", 1)
        label = QtWidgets.QLabel(f"<b>Folder:</b> {folder}<br><b>File:</b> {file_name}<br>")
        label.setWordWrap(True)
        content_layout.addWidget(label)
    
    scroll_area.setWidget(content_widget)
    
    # 閉じるボタン
    close_button = QtWidgets.QPushButton("Close")
    close_button.clicked.connect(dialog.accept)
    layout.addWidget(close_button)
    
    dialog.exec_()

# 実行
list_read_node_paths()