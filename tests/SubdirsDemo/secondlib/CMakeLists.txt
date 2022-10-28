qt_add_library(secondlib
    secondlib.cpp secondlib.h
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
    PUBLIC -Wno-deprecated-copy
)

if(CMAKE_BUILD_TYPE STREQUAL Debug)
    set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../build/debug)
endif()

if(NOT CMAKE_BUILD_TYPE STREQUAL Debug)
    set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../build/release)
endif()

message(STATUS "generate lib in " ${LIBRARY_OUTPUT_PATH})

install(TARGETS secondlib
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
