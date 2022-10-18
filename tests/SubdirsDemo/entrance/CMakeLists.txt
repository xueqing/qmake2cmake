qt_add_executable(entrance
    main.cpp
)
target_include_directories(entrance PRIVATE
    ../firstlib
    ../secondlib
)

target_link_libraries(entrance PRIVATE
    Qt::Core
    Qt::Gui
    firstlib
    secondlib
)

if(CMAKE_BUILD_TYPE STREQUAL Debug)
    target_link_libraries(entrance PRIVATE
        # Remove: L${CMAKE_CURRENT_SOURCE_DIR}/../build/debug
    )
endif()

if(NOT CMAKE_BUILD_TYPE STREQUAL Debug)
    target_link_libraries(entrance PRIVATE
        # Remove: L${CMAKE_CURRENT_SOURCE_DIR}/../build/release
    )
endif()

install(TARGETS entrance
    BUNDLE DESTINATION .
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# Consider using qt_generate_deploy_app_script() for app deployment if
# the project can use Qt 6.3. In that case rerun qmake2cmake with
# --min-qt-version=6.3.
