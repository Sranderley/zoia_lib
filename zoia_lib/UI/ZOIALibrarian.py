# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ZOIALibrarian.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1695, 1123)
        MainWindow.setFocusPolicy(Qt.StrongFocus)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-color: white;\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionSpecify_SD_Card_Location = QAction(MainWindow)
        self.actionSpecify_SD_Card_Location.setObjectName(u"actionSpecify_SD_Card_Location")
        self.actionSpecify_SD_Card_Location.setShortcutVisibleInContextMenu(True)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_title_A_Z = QAction(MainWindow)
        self.actionSort_by_title_A_Z.setObjectName(u"actionSort_by_title_A_Z")
        self.actionSort_by_title_A_Z.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_title_Z_A = QAction(MainWindow)
        self.actionSort_by_title_Z_A.setObjectName(u"actionSort_by_title_Z_A")
        self.actionSort_by_title_Z_A.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_date_new_old = QAction(MainWindow)
        self.actionSort_by_date_new_old.setObjectName(u"actionSort_by_date_new_old")
        self.actionSort_by_date_new_old.setShortcutContext(Qt.WindowShortcut)
        self.actionSort_by_date_new_old.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_date_old_new = QAction(MainWindow)
        self.actionSort_by_date_old_new.setObjectName(u"actionSort_by_date_old_new")
        self.actionSort_by_date_old_new.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_likes_high_low = QAction(MainWindow)
        self.actionSort_by_likes_high_low.setObjectName(u"actionSort_by_likes_high_low")
        self.actionSort_by_likes_high_low.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_likes_low_high = QAction(MainWindow)
        self.actionSort_by_likes_low_high.setObjectName(u"actionSort_by_likes_low_high")
        self.actionSort_by_likes_low_high.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_views_high_low = QAction(MainWindow)
        self.actionSort_by_views_high_low.setObjectName(u"actionSort_by_views_high_low")
        self.actionSort_by_views_high_low.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_views_low_high = QAction(MainWindow)
        self.actionSort_by_views_low_high.setObjectName(u"actionSort_by_views_low_high")
        self.actionSort_by_views_low_high.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_downloads_high_low = QAction(MainWindow)
        self.actionSort_by_downloads_high_low.setObjectName(u"actionSort_by_downloads_high_low")
        self.actionSort_by_downloads_high_low.setShortcutVisibleInContextMenu(True)
        self.actionSort_by_downloads_low_high = QAction(MainWindow)
        self.actionSort_by_downloads_low_high.setObjectName(u"actionSort_by_downloads_low_high")
        self.actionSort_by_downloads_low_high.setShortcutVisibleInContextMenu(True)
        self.actionZOIA_Librarian_Help = QAction(MainWindow)
        self.actionZOIA_Librarian_Help.setObjectName(u"actionZOIA_Librarian_Help")
        self.actionAlternating_Row_Colours = QAction(MainWindow)
        self.actionAlternating_Row_Colours.setObjectName(u"actionAlternating_Row_Colours")
        self.actionAlternating_Row_Colours.setShortcutVisibleInContextMenu(True)
        self.actionImport_A_Patch = QAction(MainWindow)
        self.actionImport_A_Patch.setObjectName(u"actionImport_A_Patch")
        self.actionImport_A_Patch.setShortcutVisibleInContextMenu(True)
        self.actionToggle_Dark_Mode = QAction(MainWindow)
        self.actionToggle_Dark_Mode.setObjectName(u"actionToggle_Dark_Mode")
        self.actionImport_Multiple_Patches = QAction(MainWindow)
        self.actionImport_Multiple_Patches.setObjectName(u"actionImport_Multiple_Patches")
        self.actionImport_Multiple_Patches.setShortcutVisibleInContextMenu(True)
        self.actionArial = QAction(MainWindow)
        self.actionArial.setObjectName(u"actionArial")
        font = QFont()
        font.setFamily(u"Arial")
        self.actionArial.setFont(font)
        self.actionArial_Black = QAction(MainWindow)
        self.actionArial_Black.setObjectName(u"actionArial_Black")
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setBold(True)
        font1.setWeight(75)
        self.actionArial_Black.setFont(font1)
        self.actionComic_Sans_MS = QAction(MainWindow)
        self.actionComic_Sans_MS.setObjectName(u"actionComic_Sans_MS")
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        self.actionComic_Sans_MS.setFont(font2)
        self.actionCourier_New = QAction(MainWindow)
        self.actionCourier_New.setObjectName(u"actionCourier_New")
        font3 = QFont()
        font3.setFamily(u"Courier New")
        self.actionCourier_New.setFont(font3)
        self.actionGeorgia = QAction(MainWindow)
        self.actionGeorgia.setObjectName(u"actionGeorgia")
        font4 = QFont()
        font4.setFamily(u"Georgia")
        self.actionGeorgia.setFont(font4)
        self.actionLucida_Console = QAction(MainWindow)
        self.actionLucida_Console.setObjectName(u"actionLucida_Console")
        font5 = QFont()
        font5.setFamily(u"Lucida Console")
        self.actionLucida_Console.setFont(font5)
        self.actionLucida_Sans_Unicode = QAction(MainWindow)
        self.actionLucida_Sans_Unicode.setObjectName(u"actionLucida_Sans_Unicode")
        font6 = QFont()
        font6.setFamily(u"Lucida Sans Unicode")
        self.actionLucida_Sans_Unicode.setFont(font6)
        self.actionPalatino_Linotype = QAction(MainWindow)
        self.actionPalatino_Linotype.setObjectName(u"actionPalatino_Linotype")
        font7 = QFont()
        font7.setFamily(u"Palatino Linotype")
        self.actionPalatino_Linotype.setFont(font7)
        self.actionTahoma = QAction(MainWindow)
        self.actionTahoma.setObjectName(u"actionTahoma")
        font8 = QFont()
        font8.setFamily(u"Tahoma")
        self.actionTahoma.setFont(font8)
        self.actionTimes_New_Roman = QAction(MainWindow)
        self.actionTimes_New_Roman.setObjectName(u"actionTimes_New_Roman")
        font9 = QFont()
        font9.setFamily(u"Times New Roman")
        self.actionTimes_New_Roman.setFont(font9)
        self.actionTrebuchet_MS = QAction(MainWindow)
        self.actionTrebuchet_MS.setObjectName(u"actionTrebuchet_MS")
        font10 = QFont()
        font10.setFamily(u"Trebuchet MS")
        self.actionTrebuchet_MS.setFont(font10)
        self.actionVerdana = QAction(MainWindow)
        self.actionVerdana.setObjectName(u"actionVerdana")
        font11 = QFont()
        font11.setFamily(u"Verdana")
        self.actionVerdana.setFont(font11)
        self.actionPapyrus = QAction(MainWindow)
        self.actionPapyrus.setObjectName(u"actionPapyrus")
        font12 = QFont()
        font12.setFamily(u"Papyrus")
        self.actionPapyrus.setFont(font12)
        self.actionWingdings = QAction(MainWindow)
        self.actionWingdings.setObjectName(u"actionWingdings")
        self.actionWingdings.setFont(font11)
        self.actionIncrease_Font_Size = QAction(MainWindow)
        self.actionIncrease_Font_Size.setObjectName(u"actionIncrease_Font_Size")
        self.actionIncrease_Font_Size.setShortcutVisibleInContextMenu(True)
        self.actionDecrease_Font_Size = QAction(MainWindow)
        self.actionDecrease_Font_Size.setObjectName(u"actionDecrease_Font_Size")
        self.actionDecrease_Font_Size.setShortcutVisibleInContextMenu(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setStyleSheet(u"QTabBar::tab:selected{\n"
"background-color: rgb(216, 255, 223);\n"
"border: 1px solid black;\n"
"border-bottom: 0px;\n"
"padding: 5px, 5px, 5px, 5px;\n"
"width: 200%;\n"
"font: bold;\n"
"}\n"
"QTabBar::tab:!selected{\n"
"border: 1px solid gray;\n"
"border-bottom: 0px;\n"
"padding: 5px, 5px, 5px, 5px;\n"
"width: 200%;\n"
"}\n"
"QTabBar {\n"
"background-color: white;\n"
"}\n"
"QTabWidget::tab-bar { \n"
"background-color: white;\n"
"border-bottom: 1px  solid white;\n"
"}\n"
"QTabWidget::pane { \n"
"position: absolute; \n"
"}")
        self.tabs.setTabShape(QTabWidget.Rounded)
        self.tabs.setMovable(False)
        self.tabs.setTabBarAutoHide(False)
        self.tab_ps = QWidget()
        self.tab_ps.setObjectName(u"tab_ps")
        self.tab_ps.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.tab_ps)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.widget_5 = QWidget(self.tab_ps)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.splitter_PS = QSplitter(self.widget_7)
        self.splitter_PS.setObjectName(u"splitter_PS")
        self.splitter_PS.setOrientation(Qt.Horizontal)
        self.splitter_PS.setHandleWidth(10)
        self.layoutWidget_4 = QWidget(self.splitter_PS)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.searchbar_PS = QLineEdit(self.layoutWidget_4)
        self.searchbar_PS.setObjectName(u"searchbar_PS")
        self.searchbar_PS.setStyleSheet(u"QLineEdit{\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"}")

        self.horizontalLayout_5.addWidget(self.searchbar_PS)

        self.refresh_pch_btn = QPushButton(self.layoutWidget_4)
        self.refresh_pch_btn.setObjectName(u"refresh_pch_btn")
        self.refresh_pch_btn.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 5px 2px 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.horizontalLayout_5.addWidget(self.refresh_pch_btn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.table_PS = QTableWidget(self.layoutWidget_4)
        if (self.table_PS.columnCount() < 5):
            self.table_PS.setColumnCount(5)
        if (self.table_PS.rowCount() < 1):
            self.table_PS.setRowCount(1)
        self.table_PS.setObjectName(u"table_PS")
        self.table_PS.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.table_PS.setStyleSheet(u"")
        self.table_PS.setFrameShape(QFrame.StyledPanel)
        self.table_PS.setFrameShadow(QFrame.Plain)
        self.table_PS.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_PS.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_PS.setAlternatingRowColors(False)
        self.table_PS.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_PS.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_PS.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_PS.setGridStyle(Qt.SolidLine)
        self.table_PS.setRowCount(1)
        self.table_PS.setColumnCount(5)
        self.table_PS.horizontalHeader().setCascadingSectionResizes(True)
        self.table_PS.horizontalHeader().setStretchLastSection(True)
        self.table_PS.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.table_PS)

        self.splitter_PS.addWidget(self.layoutWidget_4)
        self.text_browser_PS = QTextBrowser(self.splitter_PS)
        self.text_browser_PS.setObjectName(u"text_browser_PS")
        self.text_browser_PS.setStyleSheet(u"")
        self.text_browser_PS.setFrameShadow(QFrame.Plain)
        self.text_browser_PS.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.text_browser_PS.setOpenExternalLinks(True)
        self.text_browser_PS.setOpenLinks(True)
        self.splitter_PS.addWidget(self.text_browser_PS)

        self.horizontalLayout_7.addWidget(self.splitter_PS)


        self.verticalLayout_6.addWidget(self.widget_7)


        self.horizontalLayout_6.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.tabs.addTab(self.tab_ps, "")
        self.tab_ls = QWidget()
        self.tab_ls.setObjectName(u"tab_ls")
        self.verticalLayout_4 = QVBoxLayout(self.tab_ls)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.tab_ls)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.splitter_local = QSplitter(self.widget_9)
        self.splitter_local.setObjectName(u"splitter_local")
        sizePolicy.setHeightForWidth(self.splitter_local.sizePolicy().hasHeightForWidth())
        self.splitter_local.setSizePolicy(sizePolicy)
        self.splitter_local.setOrientation(Qt.Horizontal)
        self.splitter_local.setHandleWidth(10)
        self.layoutWidget = QWidget(self.splitter_local)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.back_btn_local = QPushButton(self.layoutWidget)
        self.back_btn_local.setObjectName(u"back_btn_local")
        self.back_btn_local.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 25px 2px 25px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.horizontalLayout_10.addWidget(self.back_btn_local)

        self.searchbar_local = QLineEdit(self.layoutWidget)
        self.searchbar_local.setObjectName(u"searchbar_local")
        self.searchbar_local.setStyleSheet(u"QLineEdit{\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"}")

        self.horizontalLayout_10.addWidget(self.searchbar_local)

        self.check_for_updates_btn = QPushButton(self.layoutWidget)
        self.check_for_updates_btn.setObjectName(u"check_for_updates_btn")
        self.check_for_updates_btn.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 5px 2px 5px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.horizontalLayout_10.addWidget(self.check_for_updates_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.table_local = QTableWidget(self.layoutWidget)
        if (self.table_local.columnCount() < 6):
            self.table_local.setColumnCount(6)
        if (self.table_local.rowCount() < 1):
            self.table_local.setRowCount(1)
        self.table_local.setObjectName(u"table_local")
        self.table_local.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_local.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table_local.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_local.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_local.setRowCount(1)
        self.table_local.setColumnCount(6)
        self.table_local.horizontalHeader().setCascadingSectionResizes(True)
        self.table_local.horizontalHeader().setStretchLastSection(True)
        self.table_local.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table_local)

        self.splitter_local.addWidget(self.layoutWidget)
        self.layoutWidget_2 = QWidget(self.splitter_local)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.update_patch_notes = QPushButton(self.layoutWidget_2)
        self.update_patch_notes.setObjectName(u"update_patch_notes")
        self.update_patch_notes.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 2px 2px 2px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.verticalLayout_12.addWidget(self.update_patch_notes)

        self.text_browser_local = QTextBrowser(self.layoutWidget_2)
        self.text_browser_local.setObjectName(u"text_browser_local")
        self.text_browser_local.setStyleSheet(u"")
        self.text_browser_local.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextSelectableByMouse)
        self.text_browser_local.setOpenExternalLinks(True)
        self.text_browser_local.setOpenLinks(True)

        self.verticalLayout_12.addWidget(self.text_browser_local)

        self.splitter_local.addWidget(self.layoutWidget_2)

        self.horizontalLayout_8.addWidget(self.splitter_local)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.tabs.addTab(self.tab_ls, "")
        self.tab_sd = QWidget()
        self.tab_sd.setObjectName(u"tab_sd")
        self.horizontalLayout = QHBoxLayout(self.tab_sd)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_sd_vert = QSplitter(self.tab_sd)
        self.splitter_sd_vert.setObjectName(u"splitter_sd_vert")
        sizePolicy.setHeightForWidth(self.splitter_sd_vert.sizePolicy().hasHeightForWidth())
        self.splitter_sd_vert.setSizePolicy(sizePolicy)
        self.splitter_sd_vert.setOrientation(Qt.Vertical)
        self.splitter_sd_vert.setHandleWidth(10)
        self.sd_tree = QTreeView(self.splitter_sd_vert)
        self.sd_tree.setObjectName(u"sd_tree")
        self.sd_tree.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 32), stop:1 rgba(255, 255, 255, 255));")
        self.sd_tree.setLineWidth(10000)
        self.sd_tree.setMidLineWidth(10000)
        self.sd_tree.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.sd_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sd_tree.setProperty("showDropIndicator", False)
        self.sd_tree.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.sd_tree.setIndentation(20)
        self.sd_tree.setRootIsDecorated(True)
        self.sd_tree.setSortingEnabled(False)
        self.sd_tree.setAnimated(True)
        self.sd_tree.setAllColumnsShowFocus(True)
        self.sd_tree.setWordWrap(True)
        self.sd_tree.setHeaderHidden(True)
        self.splitter_sd_vert.addWidget(self.sd_tree)
        self.sd_tree.header().setVisible(False)
        self.layoutWidget_3 = QWidget(self.splitter_sd_vert)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.delete_folder_sd_btn = QPushButton(self.layoutWidget_3)
        self.delete_folder_sd_btn.setObjectName(u"delete_folder_sd_btn")
        self.delete_folder_sd_btn.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 2px 2px 2px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.verticalLayout_11.addWidget(self.delete_folder_sd_btn)

        self.import_all_btn = QPushButton(self.layoutWidget_3)
        self.import_all_btn.setObjectName(u"import_all_btn")
        self.import_all_btn.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 2px 2px 2px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.verticalLayout_11.addWidget(self.import_all_btn)

        self.splitter_sd_hori = QSplitter(self.layoutWidget_3)
        self.splitter_sd_hori.setObjectName(u"splitter_sd_hori")
        self.splitter_sd_hori.setOrientation(Qt.Horizontal)
        self.splitter_sd_hori.setHandleWidth(10)
        self.table_sd_left = QTableWidget(self.splitter_sd_hori)
        if (self.table_sd_left.columnCount() < 3):
            self.table_sd_left.setColumnCount(3)
        if (self.table_sd_left.rowCount() < 32):
            self.table_sd_left.setRowCount(32)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(26, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(27, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(28, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(29, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(30, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_sd_left.setVerticalHeaderItem(31, __qtablewidgetitem31)
        self.table_sd_left.setObjectName(u"table_sd_left")
        self.table_sd_left.setAcceptDrops(True)
        self.table_sd_left.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_sd_left.setDragEnabled(False)
        self.table_sd_left.setDragDropOverwriteMode(True)
        self.table_sd_left.setDragDropMode(QAbstractItemView.DragDrop)
        self.table_sd_left.setDefaultDropAction(Qt.IgnoreAction)
        self.table_sd_left.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_sd_left.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_sd_left.setRowCount(32)
        self.table_sd_left.setColumnCount(3)
        self.splitter_sd_hori.addWidget(self.table_sd_left)
        self.table_sd_left.horizontalHeader().setStretchLastSection(True)
        self.table_sd_right = QTableWidget(self.splitter_sd_hori)
        if (self.table_sd_right.columnCount() < 3):
            self.table_sd_right.setColumnCount(3)
        if (self.table_sd_right.rowCount() < 32):
            self.table_sd_right.setRowCount(32)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(6, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(7, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(8, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(9, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(10, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(11, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(12, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(13, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(14, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(15, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(16, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(17, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(18, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(19, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(20, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(21, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(22, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(23, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(24, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(25, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(26, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(27, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(28, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(29, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(30, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.table_sd_right.setVerticalHeaderItem(31, __qtablewidgetitem63)
        self.table_sd_right.setObjectName(u"table_sd_right")
        self.table_sd_right.setAcceptDrops(True)
        self.table_sd_right.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_sd_right.setDragDropMode(QAbstractItemView.DragDrop)
        self.table_sd_right.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_sd_right.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_sd_right.setRowCount(32)
        self.table_sd_right.setColumnCount(3)
        self.splitter_sd_hori.addWidget(self.table_sd_right)
        self.table_sd_right.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.splitter_sd_hori)

        self.splitter_sd_vert.addWidget(self.layoutWidget_3)

        self.horizontalLayout.addWidget(self.splitter_sd_vert)

        self.tabs.addTab(self.tab_sd, "")
        self.tab_bank = QWidget()
        self.tab_bank.setObjectName(u"tab_bank")
        sizePolicy.setHeightForWidth(self.tab_bank.sizePolicy().hasHeightForWidth())
        self.tab_bank.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.tab_bank)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.splitter_bank = QSplitter(self.tab_bank)
        self.splitter_bank.setObjectName(u"splitter_bank")
        self.splitter_bank.setOrientation(Qt.Horizontal)
        self.splitter_bank.setHandleWidth(10)
        self.layoutWidget_6 = QWidget(self.splitter_bank)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.verticalLayout = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_save_bank = QPushButton(self.layoutWidget_6)
        self.btn_save_bank.setObjectName(u"btn_save_bank")
        self.btn_save_bank.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 25px 2px 25px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_save_bank)

        self.btn_load_bank = QPushButton(self.layoutWidget_6)
        self.btn_load_bank.setObjectName(u"btn_load_bank")
        self.btn_load_bank.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 25px 2px 25px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_load_bank)

        self.btn_export_bank = QPushButton(self.layoutWidget_6)
        self.btn_export_bank.setObjectName(u"btn_export_bank")
        self.btn_export_bank.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 25px 2px 25px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_export_bank)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.splitter_bank_tables = QSplitter(self.layoutWidget_6)
        self.splitter_bank_tables.setObjectName(u"splitter_bank_tables")
        sizePolicy.setHeightForWidth(self.splitter_bank_tables.sizePolicy().hasHeightForWidth())
        self.splitter_bank_tables.setSizePolicy(sizePolicy)
        self.splitter_bank_tables.setOrientation(Qt.Horizontal)
        self.splitter_bank_tables.setHandleWidth(10)
        self.table_bank_left = QTableWidget(self.splitter_bank_tables)
        if (self.table_bank_left.columnCount() < 2):
            self.table_bank_left.setColumnCount(2)
        if (self.table_bank_left.rowCount() < 32):
            self.table_bank_left.setRowCount(32)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(2, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(3, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(4, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(5, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(6, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(7, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(8, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(9, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(10, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(11, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(12, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(13, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(14, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(15, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(16, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(17, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(18, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(19, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(20, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(21, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(22, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(23, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(24, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(25, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(26, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(27, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(28, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(29, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(30, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.table_bank_left.setVerticalHeaderItem(31, __qtablewidgetitem95)
        self.table_bank_left.setObjectName(u"table_bank_left")
        self.table_bank_left.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_bank_left.setDragDropOverwriteMode(True)
        self.table_bank_left.setDragDropMode(QAbstractItemView.DragDrop)
        self.table_bank_left.setDefaultDropAction(Qt.IgnoreAction)
        self.table_bank_left.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_bank_left.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_bank_left.setRowCount(32)
        self.table_bank_left.setColumnCount(2)
        self.splitter_bank_tables.addWidget(self.table_bank_left)
        self.table_bank_left.horizontalHeader().setStretchLastSection(True)
        self.table_bank_right = QTableWidget(self.splitter_bank_tables)
        if (self.table_bank_right.columnCount() < 2):
            self.table_bank_right.setColumnCount(2)
        if (self.table_bank_right.rowCount() < 32):
            self.table_bank_right.setRowCount(32)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(2, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(3, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(4, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(5, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(6, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(7, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(8, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(9, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(10, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(11, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(12, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(13, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(14, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(15, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(16, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(17, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(18, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(19, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(20, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(21, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(22, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(23, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(24, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(25, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(26, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(27, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(28, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(29, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(30, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.table_bank_right.setVerticalHeaderItem(31, __qtablewidgetitem127)
        self.table_bank_right.setObjectName(u"table_bank_right")
        self.table_bank_right.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_bank_right.setDragDropOverwriteMode(True)
        self.table_bank_right.setDragDropMode(QAbstractItemView.DragDrop)
        self.table_bank_right.setDefaultDropAction(Qt.IgnoreAction)
        self.table_bank_right.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_bank_right.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_bank_right.setRowCount(32)
        self.table_bank_right.setColumnCount(2)
        self.splitter_bank_tables.addWidget(self.table_bank_right)
        self.table_bank_right.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.splitter_bank_tables)

        self.splitter_bank.addWidget(self.layoutWidget_6)
        self.layoutWidget_5 = QWidget(self.splitter_bank)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.back_btn_bank = QPushButton(self.layoutWidget_5)
        self.back_btn_bank.setObjectName(u"back_btn_bank")
        self.back_btn_bank.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 2px 25px 2px 25px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(224, 224, 224);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(207, 232, 232);\n"
"}")

        self.horizontalLayout_11.addWidget(self.back_btn_bank)

        self.searchbar_bank = QLineEdit(self.layoutWidget_5)
        self.searchbar_bank.setObjectName(u"searchbar_bank")
        self.searchbar_bank.setStyleSheet(u"QLineEdit{\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"}")

        self.horizontalLayout_11.addWidget(self.searchbar_bank)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.table_bank_local = QTableWidget(self.layoutWidget_5)
        if (self.table_bank_local.columnCount() < 4):
            self.table_bank_local.setColumnCount(4)
        if (self.table_bank_local.rowCount() < 1):
            self.table_bank_local.setRowCount(1)
        self.table_bank_local.setObjectName(u"table_bank_local")
        self.table_bank_local.setStyleSheet(u"")
        self.table_bank_local.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_bank_local.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_bank_local.setDragEnabled(True)
        self.table_bank_local.setDragDropOverwriteMode(False)
        self.table_bank_local.setDragDropMode(QAbstractItemView.DragOnly)
        self.table_bank_local.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_bank_local.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_bank_local.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_bank_local.setRowCount(1)
        self.table_bank_local.setColumnCount(4)
        self.table_bank_local.horizontalHeader().setCascadingSectionResizes(True)
        self.table_bank_local.horizontalHeader().setStretchLastSection(True)
        self.table_bank_local.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.table_bank_local)

        self.splitter_bank.addWidget(self.layoutWidget_5)
        self.text_browser_bank = QTextBrowser(self.splitter_bank)
        self.text_browser_bank.setObjectName(u"text_browser_bank")
        self.text_browser_bank.setStyleSheet(u"")
        self.text_browser_bank.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.text_browser_bank.setOpenExternalLinks(True)
        self.text_browser_bank.setOpenLinks(True)
        self.splitter_bank.addWidget(self.text_browser_bank)

        self.horizontalLayout_4.addWidget(self.splitter_bank)

        self.tabs.addTab(self.tab_bank, "")

        self.horizontalLayout_2.addWidget(self.tabs)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1695, 27))
        self.menubar.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.menubar.setAcceptDrops(False)
        self.menubar.setNativeMenuBar(False)
        self.menuFiel = QMenu(self.menubar)
        self.menuFiel.setObjectName(u"menuFiel")
        self.menuSort = QMenu(self.menubar)
        self.menuSort.setObjectName(u"menuSort")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuChange_Font = QMenu(self.menuOptions)
        self.menuChange_Font.setObjectName(u"menuChange_Font")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFiel.menuAction())
        self.menubar.addAction(self.menuSort.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuFiel.addAction(self.actionSpecify_SD_Card_Location)
        self.menuFiel.addAction(self.actionImport_A_Patch)
        self.menuFiel.addAction(self.actionImport_Multiple_Patches)
        self.menuFiel.addSeparator()
        self.menuFiel.addAction(self.actionQuit)
        self.menuSort.addAction(self.actionSort_by_title_A_Z)
        self.menuSort.addAction(self.actionSort_by_title_Z_A)
        self.menuSort.addAction(self.actionSort_by_date_new_old)
        self.menuSort.addAction(self.actionSort_by_date_old_new)
        self.menuSort.addAction(self.actionSort_by_likes_high_low)
        self.menuSort.addAction(self.actionSort_by_likes_low_high)
        self.menuSort.addAction(self.actionSort_by_views_high_low)
        self.menuSort.addAction(self.actionSort_by_views_low_high)
        self.menuSort.addAction(self.actionSort_by_downloads_high_low)
        self.menuSort.addAction(self.actionSort_by_downloads_low_high)
        self.menuOptions.addAction(self.actionAlternating_Row_Colours)
        self.menuOptions.addAction(self.menuChange_Font.menuAction())
        self.menuOptions.addAction(self.actionIncrease_Font_Size)
        self.menuOptions.addAction(self.actionDecrease_Font_Size)
        self.menuChange_Font.addAction(self.actionArial)
        self.menuChange_Font.addAction(self.actionArial_Black)
        self.menuChange_Font.addAction(self.actionComic_Sans_MS)
        self.menuChange_Font.addAction(self.actionCourier_New)
        self.menuChange_Font.addAction(self.actionGeorgia)
        self.menuChange_Font.addAction(self.actionLucida_Console)
        self.menuChange_Font.addAction(self.actionLucida_Sans_Unicode)
        self.menuChange_Font.addAction(self.actionPalatino_Linotype)
        self.menuChange_Font.addAction(self.actionPapyrus)
        self.menuChange_Font.addAction(self.actionTahoma)
        self.menuChange_Font.addAction(self.actionTimes_New_Roman)
        self.menuChange_Font.addAction(self.actionTrebuchet_MS)
        self.menuChange_Font.addAction(self.actionVerdana)
        self.menuChange_Font.addAction(self.actionWingdings)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ZOIA Librarian -  Beta 2", None))
        self.actionSpecify_SD_Card_Location.setText(QCoreApplication.translate("MainWindow", u"Specify SD Card Location", None))
#if QT_CONFIG(shortcut)
        self.actionSpecify_SD_Card_Location.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_title_A_Z.setText(QCoreApplication.translate("MainWindow", u"Sort by title (A-Z)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_title_A_Z.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_title_Z_A.setText(QCoreApplication.translate("MainWindow", u"Sort by title (Z-A)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_title_Z_A.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_date_new_old.setText(QCoreApplication.translate("MainWindow", u"Sort by date (new-old)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_date_new_old.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+3", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_date_old_new.setText(QCoreApplication.translate("MainWindow", u"Sort by date (old-new)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_date_old_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+4", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_likes_high_low.setText(QCoreApplication.translate("MainWindow", u"Sort by likes (high-low)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_likes_high_low.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+5", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_likes_low_high.setText(QCoreApplication.translate("MainWindow", u"Sort by likes (low-high)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_likes_low_high.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+6", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_views_high_low.setText(QCoreApplication.translate("MainWindow", u"Sort by views (high-low)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_views_high_low.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+7", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_views_low_high.setText(QCoreApplication.translate("MainWindow", u"Sort by views (low-high)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_views_low_high.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+8", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_downloads_high_low.setText(QCoreApplication.translate("MainWindow", u"Sort by downloads (high-low)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_downloads_high_low.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+9", None))
#endif // QT_CONFIG(shortcut)
        self.actionSort_by_downloads_low_high.setText(QCoreApplication.translate("MainWindow", u"Sort by downloads (low-high)", None))
#if QT_CONFIG(shortcut)
        self.actionSort_by_downloads_low_high.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+0", None))
#endif // QT_CONFIG(shortcut)
        self.actionZOIA_Librarian_Help.setText(QCoreApplication.translate("MainWindow", u"ZOIA Librarian Help", None))
        self.actionAlternating_Row_Colours.setText(QCoreApplication.translate("MainWindow", u"Alternating Row Colours", None))
#if QT_CONFIG(shortcut)
        self.actionAlternating_Row_Colours.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionImport_A_Patch.setText(QCoreApplication.translate("MainWindow", u"Import A Patch (.bin)", None))
#if QT_CONFIG(shortcut)
        self.actionImport_A_Patch.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionToggle_Dark_Mode.setText(QCoreApplication.translate("MainWindow", u"Toggle Dark Mode", None))
        self.actionImport_Multiple_Patches.setText(QCoreApplication.translate("MainWindow", u"Import Multiple Patches (directory)", None))
#if QT_CONFIG(shortcut)
        self.actionImport_Multiple_Patches.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionArial.setText(QCoreApplication.translate("MainWindow", u"Arial", None))
        self.actionArial_Black.setText(QCoreApplication.translate("MainWindow", u"Arial Black", None))
        self.actionComic_Sans_MS.setText(QCoreApplication.translate("MainWindow", u"Comic Sans", None))
        self.actionCourier_New.setText(QCoreApplication.translate("MainWindow", u"Courier New", None))
        self.actionGeorgia.setText(QCoreApplication.translate("MainWindow", u"Georgia", None))
        self.actionLucida_Console.setText(QCoreApplication.translate("MainWindow", u"Lucida Console", None))
        self.actionLucida_Sans_Unicode.setText(QCoreApplication.translate("MainWindow", u"Lucida Sans Unicode", None))
        self.actionPalatino_Linotype.setText(QCoreApplication.translate("MainWindow", u"Palatino Linotype", None))
        self.actionTahoma.setText(QCoreApplication.translate("MainWindow", u"Tahoma", None))
        self.actionTimes_New_Roman.setText(QCoreApplication.translate("MainWindow", u"Times New Roman", None))
        self.actionTrebuchet_MS.setText(QCoreApplication.translate("MainWindow", u"Trebuchet MS", None))
        self.actionVerdana.setText(QCoreApplication.translate("MainWindow", u"Verdana (Default)", None))
        self.actionPapyrus.setText(QCoreApplication.translate("MainWindow", u"Papyrus", None))
        self.actionWingdings.setText(QCoreApplication.translate("MainWindow", u"Wingdings (Oh no)", None))
        self.actionIncrease_Font_Size.setText(QCoreApplication.translate("MainWindow", u"Increase Font Size", None))
#if QT_CONFIG(shortcut)
        self.actionIncrease_Font_Size.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+=", None))
#endif // QT_CONFIG(shortcut)
        self.actionDecrease_Font_Size.setText(QCoreApplication.translate("MainWindow", u"Decrease Font Size", None))
#if QT_CONFIG(shortcut)
        self.actionDecrease_Font_Size.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+-", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.tabs.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabs.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.tabs.setAccessibleName(QCoreApplication.translate("MainWindow", u"Tab List", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tabs.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"This list contains four tabs, PatchStorage View, Local Storage View, SD Card View, and Banks. It allows you to switch between tabs to access different features contained with the ZOIA Librarian.", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.tab_ps.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.searchbar_PS.setToolTip(QCoreApplication.translate("MainWindow", u"Type and hit enter/return to search!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.searchbar_PS.setStatusTip(QCoreApplication.translate("MainWindow", u"Type and hit enter/return to search!", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.searchbar_PS.setAccessibleName(QCoreApplication.translate("MainWindow", u"PatchStorage View search bar", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.searchbar_PS.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Searches through the ZOIA patches currently hosted on PatchStorage for any that match what is written in the search query. Hit enter or return to initiate the search.", None))
#endif // QT_CONFIG(accessibility)
        self.searchbar_PS.setInputMask("")
        self.searchbar_PS.setText("")
#if QT_CONFIG(tooltip)
        self.refresh_pch_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to refresh the PatchStorage patch list.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.refresh_pch_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to refresh the PatchStorage patch list.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.refresh_pch_btn.setAccessibleName(QCoreApplication.translate("MainWindow", u"Refresh PatchStorage patch list button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.refresh_pch_btn.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"This button will refresh the data in the PatchStorage patch table with the latest patches on PatchStorage should the list ever become out of sync.", None))
#endif // QT_CONFIG(accessibility)
        self.refresh_pch_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh patches", None))
#if QT_CONFIG(accessibility)
        self.table_PS.setAccessibleName(QCoreApplication.translate("MainWindow", u"PatchStorage Table", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.table_PS.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays all of the ZOIA patches that are currently hosted on PatchStorage.", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(statustip)
        self.text_browser_PS.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.text_browser_PS.setAccessibleName(QCoreApplication.translate("MainWindow", u"Additional Patch Notes Display", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.text_browser_PS.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays additional information for a selected patch. This includes the author's name, the like count, the download count, the view count, and a preview link (if it exists)", None))
#endif // QT_CONFIG(accessibility)
        self.tabs.setTabText(self.tabs.indexOf(self.tab_ps), QCoreApplication.translate("MainWindow", u"PatchStorage View", None))
#if QT_CONFIG(tooltip)
        self.tabs.setTabToolTip(self.tabs.indexOf(self.tab_ps), QCoreApplication.translate("MainWindow", u"Switch to view all ZOIA patches on PatchStorage", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.back_btn_local.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to back to the full patch list.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.back_btn_local.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to back to the full patch list.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.back_btn_local.setAccessibleName(QCoreApplication.translate("MainWindow", u"Back button Local Storage View", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.back_btn_local.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"When clicked, exits out of the Version History for a patch and returns to the full list of patches currently stored in the ZOIA Librarian", None))
#endif // QT_CONFIG(accessibility)
        self.back_btn_local.setText(QCoreApplication.translate("MainWindow", u"Back", None))
#if QT_CONFIG(tooltip)
        self.searchbar_local.setToolTip(QCoreApplication.translate("MainWindow", u"Type and hit enter/return to search!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.searchbar_local.setStatusTip(QCoreApplication.translate("MainWindow", u"Type and hit enter/return to search!", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.searchbar_local.setAccessibleName(QCoreApplication.translate("MainWindow", u"LocalStorage View search bar", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.searchbar_local.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Searches through the ZOIA patches currently saved in the ZOIA Librarian for any that match what is written in the search query. Hit enter or return to initiate the search.", None))
#endif // QT_CONFIG(accessibility)
        self.searchbar_local.setInputMask("")
#if QT_CONFIG(tooltip)
        self.check_for_updates_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to check for updates for all patches listed below.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.check_for_updates_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to check for updates for all patches listed below.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.check_for_updates_btn.setAccessibleName(QCoreApplication.translate("MainWindow", u"Check for updates button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.check_for_updates_btn.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Automatically checks for updates to any patches listed in the Local Storage View table when clicked. Should any be found, a popup will let you know how many patches were updated.", None))
#endif // QT_CONFIG(accessibility)
        self.check_for_updates_btn.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
#if QT_CONFIG(accessibility)
        self.table_local.setAccessibleName(QCoreApplication.translate("MainWindow", u"Local Storage View table", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.table_local.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays all of the patches that have been saved to the ZOIA Librarian", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.update_patch_notes.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to update the patch notes for the currently selected patch.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.update_patch_notes.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to update the patch notes for the currently selected patch.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.update_patch_notes.setAccessibleName(QCoreApplication.translate("MainWindow", u"Update Patch Notes button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.update_patch_notes.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"When clicked, updates the patch notes for the currently selected patch. Patch notes can be add directly below in the Additional Patch Notes Display. ", None))
#endif // QT_CONFIG(accessibility)
        self.update_patch_notes.setText(QCoreApplication.translate("MainWindow", u"Update Patch Notes", None))
#if QT_CONFIG(accessibility)
        self.text_browser_local.setAccessibleName(QCoreApplication.translate("MainWindow", u"Additional Patch Notes Display", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.text_browser_local.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays additional information for a selected patch. This includes the author's name, the like count, the download count, the view count, and a preview link (if it exists)", None))
#endif // QT_CONFIG(accessibility)
        self.tabs.setTabText(self.tabs.indexOf(self.tab_ls), QCoreApplication.translate("MainWindow", u"Local Storage View", None))
#if QT_CONFIG(tooltip)
        self.tabs.setTabToolTip(self.tabs.indexOf(self.tab_ls), QCoreApplication.translate("MainWindow", u"Switch to your locally saved patches", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.sd_tree.setAccessibleName(QCoreApplication.translate("MainWindow", u"SD Card Viewer", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.sd_tree.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Dispalys the contents of the previously specified SD Card (which is specified via the menu bar at File->Specify SD Card path, or by using Alt+S and then specifying that way).", None))
#endif // QT_CONFIG(accessibility)
        self.delete_folder_sd_btn.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Item Above", None))
#if QT_CONFIG(tooltip)
        self.import_all_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to import all patches currently listed below.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.import_all_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to import all patches currently listed below.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.import_all_btn.setAccessibleName(QCoreApplication.translate("MainWindow", u"Import All Patches button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.import_all_btn.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Attempts to import all of the patches listed in the tables below (SD card table left and SD card table right) into the ZOIA Librarian. This requires that a folder is selected from the SD Card Viewer above that contains patches.", None))
#endif // QT_CONFIG(accessibility)
        self.import_all_btn.setText(QCoreApplication.translate("MainWindow", u"Import All Listed Patches Below", None))
        ___qtablewidgetitem = self.table_sd_left.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.table_sd_left.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.table_sd_left.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.table_sd_left.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.table_sd_left.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem5 = self.table_sd_left.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem6 = self.table_sd_left.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem7 = self.table_sd_left.verticalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem8 = self.table_sd_left.verticalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem9 = self.table_sd_left.verticalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem10 = self.table_sd_left.verticalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem11 = self.table_sd_left.verticalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem12 = self.table_sd_left.verticalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem13 = self.table_sd_left.verticalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem14 = self.table_sd_left.verticalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem15 = self.table_sd_left.verticalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem16 = self.table_sd_left.verticalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem17 = self.table_sd_left.verticalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem18 = self.table_sd_left.verticalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem19 = self.table_sd_left.verticalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem20 = self.table_sd_left.verticalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem21 = self.table_sd_left.verticalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem22 = self.table_sd_left.verticalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem23 = self.table_sd_left.verticalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem24 = self.table_sd_left.verticalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"24", None));
        ___qtablewidgetitem25 = self.table_sd_left.verticalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"25", None));
        ___qtablewidgetitem26 = self.table_sd_left.verticalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem27 = self.table_sd_left.verticalHeaderItem(27)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"27", None));
        ___qtablewidgetitem28 = self.table_sd_left.verticalHeaderItem(28)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"28", None));
        ___qtablewidgetitem29 = self.table_sd_left.verticalHeaderItem(29)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"29", None));
        ___qtablewidgetitem30 = self.table_sd_left.verticalHeaderItem(30)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem31 = self.table_sd_left.verticalHeaderItem(31)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"31", None));
#if QT_CONFIG(accessibility)
        self.table_sd_left.setAccessibleName(QCoreApplication.translate("MainWindow", u"SD Card Table left", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.table_sd_left.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays patches that would occupy slots 0-31 on a ZOIA", None))
#endif // QT_CONFIG(accessibility)
        ___qtablewidgetitem32 = self.table_sd_right.verticalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"32", None));
        ___qtablewidgetitem33 = self.table_sd_right.verticalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"33", None));
        ___qtablewidgetitem34 = self.table_sd_right.verticalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"34", None));
        ___qtablewidgetitem35 = self.table_sd_right.verticalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"35", None));
        ___qtablewidgetitem36 = self.table_sd_right.verticalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"36", None));
        ___qtablewidgetitem37 = self.table_sd_right.verticalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"37", None));
        ___qtablewidgetitem38 = self.table_sd_right.verticalHeaderItem(6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"38", None));
        ___qtablewidgetitem39 = self.table_sd_right.verticalHeaderItem(7)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"39", None));
        ___qtablewidgetitem40 = self.table_sd_right.verticalHeaderItem(8)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem41 = self.table_sd_right.verticalHeaderItem(9)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"41", None));
        ___qtablewidgetitem42 = self.table_sd_right.verticalHeaderItem(10)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"42", None));
        ___qtablewidgetitem43 = self.table_sd_right.verticalHeaderItem(11)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem44 = self.table_sd_right.verticalHeaderItem(12)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"44", None));
        ___qtablewidgetitem45 = self.table_sd_right.verticalHeaderItem(13)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"45", None));
        ___qtablewidgetitem46 = self.table_sd_right.verticalHeaderItem(14)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"46", None));
        ___qtablewidgetitem47 = self.table_sd_right.verticalHeaderItem(15)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"47", None));
        ___qtablewidgetitem48 = self.table_sd_right.verticalHeaderItem(16)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"48", None));
        ___qtablewidgetitem49 = self.table_sd_right.verticalHeaderItem(17)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"49", None));
        ___qtablewidgetitem50 = self.table_sd_right.verticalHeaderItem(18)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem51 = self.table_sd_right.verticalHeaderItem(19)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"51", None));
        ___qtablewidgetitem52 = self.table_sd_right.verticalHeaderItem(20)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"52", None));
        ___qtablewidgetitem53 = self.table_sd_right.verticalHeaderItem(21)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"53", None));
        ___qtablewidgetitem54 = self.table_sd_right.verticalHeaderItem(22)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"54", None));
        ___qtablewidgetitem55 = self.table_sd_right.verticalHeaderItem(23)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"55", None));
        ___qtablewidgetitem56 = self.table_sd_right.verticalHeaderItem(24)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"56", None));
        ___qtablewidgetitem57 = self.table_sd_right.verticalHeaderItem(25)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"57", None));
        ___qtablewidgetitem58 = self.table_sd_right.verticalHeaderItem(26)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"58", None));
        ___qtablewidgetitem59 = self.table_sd_right.verticalHeaderItem(27)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"59", None));
        ___qtablewidgetitem60 = self.table_sd_right.verticalHeaderItem(28)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"60", None));
        ___qtablewidgetitem61 = self.table_sd_right.verticalHeaderItem(29)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"61", None));
        ___qtablewidgetitem62 = self.table_sd_right.verticalHeaderItem(30)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"62", None));
        ___qtablewidgetitem63 = self.table_sd_right.verticalHeaderItem(31)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"63", None));
#if QT_CONFIG(accessibility)
        self.table_sd_right.setAccessibleName(QCoreApplication.translate("MainWindow", u"SD Card Table right", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.table_sd_right.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays patches that would occupy slots 32-63 on a ZOIA", None))
#endif // QT_CONFIG(accessibility)
        self.tabs.setTabText(self.tabs.indexOf(self.tab_sd), QCoreApplication.translate("MainWindow", u"SD Card View", None))
#if QT_CONFIG(tooltip)
        self.tabs.setTabToolTip(self.tabs.indexOf(self.tab_sd), QCoreApplication.translate("MainWindow", u"Switch to view your SD card within the ZOIA Librarian", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_save_bank.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to save your Bank.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_save_bank.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to save your Bank.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.btn_save_bank.setAccessibleName(QCoreApplication.translate("MainWindow", u"Save Bank button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_save_bank.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"When clicked, will open a popup asking for a Bank name, which will then be saved such that it can be loaded at a later time.", None))
#endif // QT_CONFIG(accessibility)
        self.btn_save_bank.setText(QCoreApplication.translate("MainWindow", u"Save Bank", None))
#if QT_CONFIG(tooltip)
        self.btn_load_bank.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to load a Bank.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_load_bank.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to load a Bank.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.btn_load_bank.setAccessibleName(QCoreApplication.translate("MainWindow", u"Load Bank button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_load_bank.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"When clicked, you will be prompted to select a Bank to load that has been created in a previous session using the ZOIA Librarian.", None))
#endif // QT_CONFIG(accessibility)
        self.btn_load_bank.setText(QCoreApplication.translate("MainWindow", u"Load Bank", None))
#if QT_CONFIG(tooltip)
        self.btn_export_bank.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to export a Bank as a folder to your SD card.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_export_bank.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to export a Bank as a folder to your SD card.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.btn_export_bank.setAccessibleName(QCoreApplication.translate("MainWindow", u"Export Bank button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_export_bank.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"When clicked, will open a popup asking for a Bank name, which will then be saved such that it can be exported to an SD card, should it have been specified previously.", None))
#endif // QT_CONFIG(accessibility)
        self.btn_export_bank.setText(QCoreApplication.translate("MainWindow", u"Export Bank", None))
        ___qtablewidgetitem64 = self.table_bank_left.verticalHeaderItem(0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem65 = self.table_bank_left.verticalHeaderItem(1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem66 = self.table_bank_left.verticalHeaderItem(2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem67 = self.table_bank_left.verticalHeaderItem(3)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem68 = self.table_bank_left.verticalHeaderItem(4)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem69 = self.table_bank_left.verticalHeaderItem(5)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem70 = self.table_bank_left.verticalHeaderItem(6)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem71 = self.table_bank_left.verticalHeaderItem(7)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem72 = self.table_bank_left.verticalHeaderItem(8)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem73 = self.table_bank_left.verticalHeaderItem(9)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem74 = self.table_bank_left.verticalHeaderItem(10)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem75 = self.table_bank_left.verticalHeaderItem(11)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem76 = self.table_bank_left.verticalHeaderItem(12)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem77 = self.table_bank_left.verticalHeaderItem(13)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem78 = self.table_bank_left.verticalHeaderItem(14)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem79 = self.table_bank_left.verticalHeaderItem(15)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem80 = self.table_bank_left.verticalHeaderItem(16)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem81 = self.table_bank_left.verticalHeaderItem(17)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem82 = self.table_bank_left.verticalHeaderItem(18)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem83 = self.table_bank_left.verticalHeaderItem(19)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem84 = self.table_bank_left.verticalHeaderItem(20)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem85 = self.table_bank_left.verticalHeaderItem(21)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem86 = self.table_bank_left.verticalHeaderItem(22)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem87 = self.table_bank_left.verticalHeaderItem(23)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem88 = self.table_bank_left.verticalHeaderItem(24)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"24", None));
        ___qtablewidgetitem89 = self.table_bank_left.verticalHeaderItem(25)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"25", None));
        ___qtablewidgetitem90 = self.table_bank_left.verticalHeaderItem(26)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem91 = self.table_bank_left.verticalHeaderItem(27)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"27", None));
        ___qtablewidgetitem92 = self.table_bank_left.verticalHeaderItem(28)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"28", None));
        ___qtablewidgetitem93 = self.table_bank_left.verticalHeaderItem(29)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"29", None));
        ___qtablewidgetitem94 = self.table_bank_left.verticalHeaderItem(30)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem95 = self.table_bank_left.verticalHeaderItem(31)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"31", None));
#if QT_CONFIG(tooltip)
        self.table_bank_left.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.table_bank_left.setStatusTip(QCoreApplication.translate("MainWindow", u"Drag and drop a patch here!", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.table_bank_left.setAccessibleName(QCoreApplication.translate("MainWindow", u"Bank Table left", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.table_bank_left.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays patches that would occupy slots 0-31 on a ZOIA", None))
#endif // QT_CONFIG(accessibility)
        ___qtablewidgetitem96 = self.table_bank_right.verticalHeaderItem(0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"32", None));
        ___qtablewidgetitem97 = self.table_bank_right.verticalHeaderItem(1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"33", None));
        ___qtablewidgetitem98 = self.table_bank_right.verticalHeaderItem(2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"34", None));
        ___qtablewidgetitem99 = self.table_bank_right.verticalHeaderItem(3)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"35", None));
        ___qtablewidgetitem100 = self.table_bank_right.verticalHeaderItem(4)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"36", None));
        ___qtablewidgetitem101 = self.table_bank_right.verticalHeaderItem(5)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"37", None));
        ___qtablewidgetitem102 = self.table_bank_right.verticalHeaderItem(6)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"38", None));
        ___qtablewidgetitem103 = self.table_bank_right.verticalHeaderItem(7)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"39", None));
        ___qtablewidgetitem104 = self.table_bank_right.verticalHeaderItem(8)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem105 = self.table_bank_right.verticalHeaderItem(9)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"41", None));
        ___qtablewidgetitem106 = self.table_bank_right.verticalHeaderItem(10)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"42", None));
        ___qtablewidgetitem107 = self.table_bank_right.verticalHeaderItem(11)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem108 = self.table_bank_right.verticalHeaderItem(12)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"44", None));
        ___qtablewidgetitem109 = self.table_bank_right.verticalHeaderItem(13)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"45", None));
        ___qtablewidgetitem110 = self.table_bank_right.verticalHeaderItem(14)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"46", None));
        ___qtablewidgetitem111 = self.table_bank_right.verticalHeaderItem(15)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"47", None));
        ___qtablewidgetitem112 = self.table_bank_right.verticalHeaderItem(16)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"48", None));
        ___qtablewidgetitem113 = self.table_bank_right.verticalHeaderItem(17)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"49", None));
        ___qtablewidgetitem114 = self.table_bank_right.verticalHeaderItem(18)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem115 = self.table_bank_right.verticalHeaderItem(19)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"51", None));
        ___qtablewidgetitem116 = self.table_bank_right.verticalHeaderItem(20)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"52", None));
        ___qtablewidgetitem117 = self.table_bank_right.verticalHeaderItem(21)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"53", None));
        ___qtablewidgetitem118 = self.table_bank_right.verticalHeaderItem(22)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"54", None));
        ___qtablewidgetitem119 = self.table_bank_right.verticalHeaderItem(23)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"55", None));
        ___qtablewidgetitem120 = self.table_bank_right.verticalHeaderItem(24)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"56", None));
        ___qtablewidgetitem121 = self.table_bank_right.verticalHeaderItem(25)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"57", None));
        ___qtablewidgetitem122 = self.table_bank_right.verticalHeaderItem(26)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"58", None));
        ___qtablewidgetitem123 = self.table_bank_right.verticalHeaderItem(27)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"59", None));
        ___qtablewidgetitem124 = self.table_bank_right.verticalHeaderItem(28)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"60", None));
        ___qtablewidgetitem125 = self.table_bank_right.verticalHeaderItem(29)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"61", None));
        ___qtablewidgetitem126 = self.table_bank_right.verticalHeaderItem(30)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"62", None));
        ___qtablewidgetitem127 = self.table_bank_right.verticalHeaderItem(31)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"63", None));
#if QT_CONFIG(tooltip)
        self.table_bank_right.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.table_bank_right.setStatusTip(QCoreApplication.translate("MainWindow", u"Drag and drop a patch here!", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.table_bank_right.setAccessibleName(QCoreApplication.translate("MainWindow", u"Bank table right", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.table_bank_right.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays patches that would occupy slots 32-63 on a ZOIA", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.back_btn_bank.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to back to the full patch list.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.back_btn_bank.setStatusTip(QCoreApplication.translate("MainWindow", u"Click here to back to the full patch list.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.back_btn_bank.setAccessibleName(QCoreApplication.translate("MainWindow", u"Back button Bank", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.back_btn_bank.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"When clicked, exits out of the Version History for a patch and returns to the full list of patches currently stored in the ZOIA Librarian", None))
#endif // QT_CONFIG(accessibility)
        self.back_btn_bank.setText(QCoreApplication.translate("MainWindow", u"Back", None))
#if QT_CONFIG(tooltip)
        self.searchbar_bank.setToolTip(QCoreApplication.translate("MainWindow", u"Type and hit enter/return to search!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.searchbar_bank.setStatusTip(QCoreApplication.translate("MainWindow", u"Type and hit enter/return to search!", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.searchbar_bank.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.searchbar_bank.setAccessibleName(QCoreApplication.translate("MainWindow", u"Banks search bar", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.searchbar_bank.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Searches through the ZOIA patches currently saved in the ZOIA Librarian for any that match what is written in the search query. Hit enter or return to initiate the search.", None))
#endif // QT_CONFIG(accessibility)
        self.searchbar_bank.setInputMask("")
#if QT_CONFIG(tooltip)
        self.table_bank_local.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.table_bank_local.setStatusTip(QCoreApplication.translate("MainWindow", u"Drag a patch to one of the tables on the left!", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.table_bank_local.setAccessibleName(QCoreApplication.translate("MainWindow", u"Banks table", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.table_bank_local.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays all of the patches that have been saved to the ZOIA Librarian", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.text_browser_bank.setAccessibleName(QCoreApplication.translate("MainWindow", u"Additional Patch Notes Display", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.text_browser_bank.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Displays additional information for a selected patch. This includes the author's name, the like count, the download count, the view count, and a preview link (if it exists)", None))
#endif // QT_CONFIG(accessibility)
        self.tabs.setTabText(self.tabs.indexOf(self.tab_bank), QCoreApplication.translate("MainWindow", u"Banks", None))
#if QT_CONFIG(tooltip)
        self.tabs.setTabToolTip(self.tabs.indexOf(self.tab_bank), QCoreApplication.translate("MainWindow", u"Switch to view the Bank creator", None))
#endif // QT_CONFIG(tooltip)
        self.menuFiel.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSort.setTitle(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuChange_Font.setTitle(QCoreApplication.translate("MainWindow", u"Change Font", None))
    # retranslateUi

