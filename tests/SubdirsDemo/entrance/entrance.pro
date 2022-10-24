TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
#CONFIG -= qt

SOURCES += main.cpp

INCLUDEPATH += \
    $$PWD/../firstlib \
    $$PWD/../secondlib \
    $$PWD/../include

LIBS += -lsecondlib -lfirstlib
LIBS += -L$$PWD/../lib -ljson11

CONFIG(debug, debug|release) {
    LIBS += -L$$PWD/../build/debug
    DESTDIR = $$PWD/../build/debug
} else {
    LIBS += -L$$PWD/../build/release
    DESTDIR = $$PWD/../build/release
}
