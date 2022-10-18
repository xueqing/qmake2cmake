qt_add_library(firstlib
    firstlib.cpp firstlib.h
    firstlib_global.h
)
target_compile_definitions(firstlib PUBLIC
    FIRSTLIB_LIBRARY
    QT_DEPRECATED_WARNINGS
)

target_link_libraries(firstlib PUBLIC
    Qt::Core
)

target_compile_options(firstlib
    -Wno-deprecated-copy
)

install(TARGETS firstlib
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    FRAMEWORK DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
