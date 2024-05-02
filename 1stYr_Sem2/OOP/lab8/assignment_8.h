#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_assignment_8.h"

class assignment_8 : public QMainWindow
{
    Q_OBJECT

public:
    assignment_8(QWidget *parent = nullptr);
    ~assignment_8();

private:
    Ui::assignment_8Class ui;
};
