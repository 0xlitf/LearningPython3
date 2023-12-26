from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtWidgets import QGraphicsView,QGraphicsScene,QGraphicsPixmapItem,QGraphicsItem

class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(self.AnchorUnderMouse)

        self.scene = QGraphicsScene()  # 创建画布
        self.setScene(self.scene)  # 把画布添加到窗口

    def load(self,img):
        # 清除scene残留
        self.scene.clear()
        item = QGraphicsPixmapItem(img)
        item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(item)
        # # 平滑缩放，平滑后看不到像素点块
        # item.setTransformationMode(Qt.SmoothTransformation)
        # 让image填充显示窗口
        self.fitInView(item, Qt.KeepAspectRatio)

    def wheelEvent(self, e: QWheelEvent):
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        if e.angleDelta().y() > 0:
            self.scale(1.1, 1.1)
        else:
            self.scale(1 / 1.1, 1 / 1.1)
        self.setTransformationAnchor(self.AnchorUnderMouse)