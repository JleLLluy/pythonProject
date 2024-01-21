def run(self):
    name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                            "Как тебя зовут?")
    if ok_pressed:
        self.info_btn.setText(name)