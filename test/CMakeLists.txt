cmake_minimum_required(VERSION 2.8)
project(lest_package_test)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test test.cpp)
target_link_libraries(test ${CONAN_LIBS})

target_compile_options( test PUBLIC -Dlest_FEATURE_AUTO_REGISTER=1 )

if( ${CMAKE_GENERATOR} MATCHES "Visual" )
    target_compile_options( test PUBLIC -W3 -EHsc )
else()
    target_compile_options( test PUBLIC -std=c++11 -Wall -Wno-missing-braces )
endif()
