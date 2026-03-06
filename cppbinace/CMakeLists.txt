cmake_minimum_required(VERSION 3.20)
set(VCPKG_APPLOCAL_DEPS OFF)
project(cooking)

set(CMAKE_CXX_STANDARD 17)

# curl folder
set(CURL_DIR "curl dire")

# nlohmann_json (header-only, just point to the include folder)

set(JSON_DIR "C:/libs/nlohmann")

include_directories("${CURL_DIR}/include")
include_directories("${JSON_DIR}")

add_executable(CryptoTracker main.cpp)

target_link_libraries(CryptoTracker
        "${CURL_DIR}/lib/libcurl.dll.a"
)

add_custom_command(TARGET CryptoTracker POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CURL_DIR}/bin/libcurl-x64.dll"
        $<TARGET_FILE_DIR:CryptoTracker>
)
