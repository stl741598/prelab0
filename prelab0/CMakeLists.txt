cmake_minimum_required(VERSION 3.10)

#set( CMAKE_CXX_COMPILER "/c/ProgramData/chocolatey/bin/g++.exe" )
#set( CMAKE_C_COMPILER "/c/ProgramData/chocolatey/bin/gcc.exe" )
#set(CMAKE_C_COMPILER "/c/ProgramData/chocolatey/lib/mingw/tools/install/mingw64/bin/gcc.exe")
#set(CMAKE_CXX_COMPILER "/c/ProgramData/chocolatey/lib/mingw/tools/install/mingw64/bin/g++.exe")



#set(DCMAKE_C_COMPILER="/c/ProgramData/chocolatey/lib/mingw/tools/install/mingw64/bin/gcc.exe")
#set(DCMAKE_CXX_COMPILER="/c/ProgramData/chocolatey/lib/mingw/tools/install/mingw64/bin/g++.exe")

project(arbitrary)

set(CMAKE_CXX_STANDARD 17)

add_executable (arbitrary arbitrary.cpp)
