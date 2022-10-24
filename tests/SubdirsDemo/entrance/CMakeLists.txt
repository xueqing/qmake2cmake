if(CMAKE_BUILD_TYPE STREQUAL Debug)
    set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../build/debug)
endif()

if(NOT CMAKE_BUILD_TYPE STREQUAL Debug)
    set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../build/release)
endif()

message(STATUS "generate exe in " ${EXECUTABLE_OUTPUT_PATH})

qt_add_executable(entrance
    main.cpp
)

target_include_directories(entrance PRIVATE
    ../firstlib
    ../secondlib
    ../include
)

find_library(libjson11 json11 ${CMAKE_CURRENT_SOURCE_DIR}/../lib)

target_link_libraries(entrance PRIVATE
    Qt::Core
    Qt::Gui
    secondlib
    firstlib
    ${libjson11}
)

install(TARGETS entrance
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# Consider using qt_generate_deploy_app_script() for app deployment if
# the project can use Qt 6.3. In that case rerun qmake2cmake with
# --min-qt-version=6.3.
