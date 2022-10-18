qt_add_library(secondlib
    secondlib.cpp secondlib.h
    secondlib_global.h
)
target_include_directories(secondlib PUBLIC
    ../firstlib
)

target_compile_definitions(secondlib PUBLIC
    QT_DEPRECATED_WARNINGS
    SECONDLIB_LIBRARY
)

target_link_libraries(secondlib PUBLIC
    Qt::Core
)

target_compile_options(secondlib
    -Wno-deprecated-copy
)

install(TARGETS secondlib
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    FRAMEWORK DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
