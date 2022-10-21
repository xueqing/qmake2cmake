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
    PUBLIC -Wno-deprecated-copy
)

if(CMAKE_BUILD_TYPE STREQUAL Debug)
    set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../build/debug)
endif()

if(NOT CMAKE_BUILD_TYPE STREQUAL Debug)
    set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../build/release)
endif()

message(STATUS "generate lib in " ${LIBRARY_OUTPUT_PATH})

install(TARGETS firstlib
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
