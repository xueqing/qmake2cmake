TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
#CONFIG -= qt

SOURCES += main.cpp

INCLUDEPATH += \
    $$PWD/../firstlib \
    $$PWD/../secondlib

LIBS += -lsecondlib -lfirstlib

CONFIG(debug, debug|release) {
    LIBS += -L$$PWD/../build/debug
    DESTDIR = $$PWD/../build/debug
} else {
    LIBS += -L$$PWD/../build/release
    DESTDIR = $$PWD/../build/release
}
