# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_save_form.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

class Ui_FileSaveForm(object):
    def setupUi(self, FileSaveForm):
        FileSaveForm.setObjectName("FileSaveForm")
        FileSaveForm.resize(850, 539)
        self.verticalLayout = QtGui.QVBoxLayout(FileSaveForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.expand_checkbox = QtGui.QCheckBox(FileSaveForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expand_checkbox.sizePolicy().hasHeightForWidth())
        self.expand_checkbox.setSizePolicy(sizePolicy)
        self.expand_checkbox.setMaximumSize(QtCore.QSize(16777215, 24))
        self.expand_checkbox.setStyleSheet("#expand_checkbox::indicator {\n"
"width: 24;\n"
"height: 24;\n"
"}\n"
"\n"
"#expand_checkbox::indicator::unchecked {\n"
"    image: url(:/tk-multi-workfiles2/save_expand.png);\n"
"\n"
"}\n"
"\n"
"#expand_checkbox::indicator::unchecked::hover {\n"
"    image: url(:/tk-multi-workfiles2/save_expand_hover.png);\n"
"}\n"
"\n"
"#expand_checkbox::indicator::unchecked::pressed {\n"
"    image: url(:/tk-multi-workfiles2/save_expand_pressed.png);\n"
"}\n"
"\n"
"#expand_checkbox::indicator::checked {\n"
"    image: url(:/tk-multi-workfiles2/save_collapse.png);\n"
"}\n"
"\n"
"#expand_checkbox::indicator::checked:hover {\n"
"    image: url(:/tk-multi-workfiles2/save_collapse_hover.png);\n"
"}\n"
"\n"
"#expand_checkbox::indicator::checked:pressed {\n"
"    image: url(:/tk-multi-workfiles2/save_collapse_pressed.png);\n"
"}")
        self.expand_checkbox.setText("")
        self.expand_checkbox.setObjectName("expand_checkbox")
        self.horizontalLayout_3.addWidget(self.expand_checkbox)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.nav = NavigationWidget(FileSaveForm)
        self.nav.setMinimumSize(QtCore.QSize(80, 30))
        self.nav.setStyleSheet("#nav {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.nav.setObjectName("nav")
        self.gridLayout_2.addWidget(self.nav, 0, 1, 1, 1)
        self.breadcrumbs = BreadcrumbWidget(FileSaveForm)
        self.breadcrumbs.setMinimumSize(QtCore.QSize(0, 30))
        self.breadcrumbs.setStyleSheet("#breadcrumbs {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.breadcrumbs.setObjectName("breadcrumbs")
        self.gridLayout_2.addWidget(self.breadcrumbs, 0, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.browser = BrowserForm(FileSaveForm)
        self.browser.setStyleSheet("#browser {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.browser.setObjectName("browser")
        self.verticalLayout_3.addWidget(self.browser)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line = QtGui.QFrame(FileSaveForm)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(12, 4, 12, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.file_controls_grid = QtGui.QGridLayout()
        self.file_controls_grid.setHorizontalSpacing(14)
        self.file_controls_grid.setVerticalSpacing(6)
        self.file_controls_grid.setObjectName("file_controls_grid")
        self.version_label = QtGui.QLabel(FileSaveForm)
        self.version_label.setMinimumSize(QtCore.QSize(0, 0))
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setIndent(-1)
        self.version_label.setObjectName("version_label")
        self.file_controls_grid.addWidget(self.version_label, 1, 0, 1, 1)
        self.name_label = QtGui.QLabel(FileSaveForm)
        self.name_label.setMinimumSize(QtCore.QSize(0, 0))
        self.name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_label.setIndent(-1)
        self.name_label.setObjectName("name_label")
        self.file_controls_grid.addWidget(self.name_label, 0, 0, 1, 1)
        self.file_type_label = QtGui.QLabel(FileSaveForm)
        self.file_type_label.setMinimumSize(QtCore.QSize(0, 0))
        self.file_type_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.file_type_label.setIndent(-1)
        self.file_type_label.setObjectName("file_type_label")
        self.file_controls_grid.addWidget(self.file_type_label, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(-1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.version_spinner = QtGui.QSpinBox(FileSaveForm)
        self.version_spinner.setObjectName("version_spinner")
        self.horizontalLayout_2.addWidget(self.version_spinner)
        self.use_next_available_cb = QtGui.QCheckBox(FileSaveForm)
        self.use_next_available_cb.setObjectName("use_next_available_cb")
        self.horizontalLayout_2.addWidget(self.use_next_available_cb)
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.file_controls_grid.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.file_type_menu = QtGui.QComboBox(FileSaveForm)
        self.file_type_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.file_type_menu.setObjectName("file_type_menu")
        self.horizontalLayout_6.addWidget(self.file_type_menu)
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.file_controls_grid.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.name_edit = QtGui.QLineEdit(FileSaveForm)
        self.name_edit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.name_edit.setFrame(True)
        self.name_edit.setObjectName("name_edit")
        self.horizontalLayout_8.addWidget(self.name_edit)
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_8.setStretch(0, 1)
        self.file_controls_grid.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.file_controls_grid.setColumnMinimumWidth(0, 80)
        self.file_controls_grid.setColumnStretch(1, 1)
        self.verticalLayout_2.addLayout(self.file_controls_grid)
        self.feedback_stacked_widget = QtGui.QStackedWidget(FileSaveForm)
        self.feedback_stacked_widget.setObjectName("feedback_stacked_widget")
        self.preview_page = QtGui.QWidget()
        self.preview_page.setObjectName("preview_page")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.preview_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.preview_grid = QtGui.QGridLayout()
        self.preview_grid.setHorizontalSpacing(14)
        self.preview_grid.setVerticalSpacing(6)
        self.preview_grid.setObjectName("preview_grid")
        self.preview_label = QtGui.QLabel(self.preview_page)
        self.preview_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.preview_label.setIndent(-1)
        self.preview_label.setObjectName("preview_label")
        self.preview_grid.addWidget(self.preview_label, 0, 0, 1, 1)
        self.file_name_preview = QtGui.QLabel(self.preview_page)
        self.file_name_preview.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.file_name_preview.setWordWrap(True)
        self.file_name_preview.setIndent(-1)
        self.file_name_preview.setObjectName("file_name_preview")
        self.preview_grid.addWidget(self.file_name_preview, 0, 1, 1, 1)
        self.work_area_preview = ElidedLabel(self.preview_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_area_preview.sizePolicy().hasHeightForWidth())
        self.work_area_preview.setSizePolicy(sizePolicy)
        self.work_area_preview.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.work_area_preview.setWordWrap(True)
        self.work_area_preview.setIndent(-1)
        self.work_area_preview.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.work_area_preview.setObjectName("work_area_preview")
        self.preview_grid.addWidget(self.work_area_preview, 1, 1, 1, 1)
        self.work_area_label = QtGui.QLabel(self.preview_page)
        self.work_area_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.work_area_label.setIndent(-1)
        self.work_area_label.setObjectName("work_area_label")
        self.preview_grid.addWidget(self.work_area_label, 1, 0, 1, 1)
        self.preview_grid.setColumnMinimumWidth(0, 80)
        self.preview_grid.setColumnStretch(1, 1)
        self.verticalLayout_4.addLayout(self.preview_grid)
        self.feedback_stacked_widget.addWidget(self.preview_page)
        self.warning_page = QtGui.QWidget()
        self.warning_page.setObjectName("warning_page")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.warning_page)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.warning_grid = QtGui.QGridLayout()
        self.warning_grid.setContentsMargins(0, -1, -1, -1)
        self.warning_grid.setHorizontalSpacing(14)
        self.warning_grid.setVerticalSpacing(6)
        self.warning_grid.setObjectName("warning_grid")
        self.warning = QtGui.QLabel(self.warning_page)
        self.warning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.warning.setWordWrap(True)
        self.warning.setMargin(0)
        self.warning.setIndent(-1)
        self.warning.setObjectName("warning")
        self.warning_grid.addWidget(self.warning, 0, 1, 1, 1)
        self.warning_label = QtGui.QLabel(self.warning_page)
        self.warning_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.warning_label.setIndent(-1)
        self.warning_label.setObjectName("warning_label")
        self.warning_grid.addWidget(self.warning_label, 0, 0, 1, 1)
        self.warning_grid.setColumnMinimumWidth(0, 80)
        self.warning_grid.setColumnStretch(1, 1)
        self.horizontalLayout_7.addLayout(self.warning_grid)
        self.feedback_stacked_widget.addWidget(self.warning_page)
        self.verticalLayout_2.addWidget(self.feedback_stacked_widget)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.break_line = QtGui.QFrame(FileSaveForm)
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.break_line.setObjectName("break_line")
        self.verticalLayout.addWidget(self.break_line)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(12, 8, 12, 12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.cancel_btn = QtGui.QPushButton(FileSaveForm)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.save_btn = QtGui.QPushButton(FileSaveForm)
        self.save_btn.setDefault(True)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(FileSaveForm)
        self.feedback_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FileSaveForm)
        FileSaveForm.setTabOrder(self.name_edit, self.version_spinner)
        FileSaveForm.setTabOrder(self.version_spinner, self.use_next_available_cb)
        FileSaveForm.setTabOrder(self.use_next_available_cb, self.file_type_menu)
        FileSaveForm.setTabOrder(self.file_type_menu, self.cancel_btn)
        FileSaveForm.setTabOrder(self.cancel_btn, self.save_btn)
        FileSaveForm.setTabOrder(self.save_btn, self.expand_checkbox)

    def retranslateUi(self, FileSaveForm):
        FileSaveForm.setWindowTitle(QtGui.QApplication.translate("FileSaveForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.expand_checkbox.setToolTip(QtGui.QApplication.translate("FileSaveForm", "Toggle Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.version_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">Version:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">Name:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.file_type_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">File Type:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.use_next_available_cb.setText(QtGui.QApplication.translate("FileSaveForm", "Use Next Available Version Number", None, QtGui.QApplication.UnicodeUTF8))
        self.preview_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600; color:rgb(120, 120, 120)\">Preview:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.file_name_preview.setText(QtGui.QApplication.translate("FileSaveForm", "preview", None, QtGui.QApplication.UnicodeUTF8))
        self.work_area_preview.setText(QtGui.QApplication.translate("FileSaveForm", ".../work/area", None, QtGui.QApplication.UnicodeUTF8))
        self.work_area_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600; color:rgb(120, 120, 120)\">Work Area:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.warning.setText(QtGui.QApplication.translate("FileSaveForm", "warning", None, QtGui.QApplication.UnicodeUTF8))
        self.warning_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600; color:rgb(226, 146, 0)\">Warning:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("FileSaveForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("FileSaveForm", "Save", None, QtGui.QApplication.UnicodeUTF8))

from ..framework_qtwidgets import NavigationWidget, BreadcrumbWidget, ElidedLabel
from ..browser_form import BrowserForm
from . import resources_rc
