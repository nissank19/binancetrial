cmake_minimum_required(VERSION 3.20)
set(VCPKG_APPLOCAL_DEPS OFF)
project(cooking)

set(CMAKE_CXX_STANDARD 17)

# --- DOCKER/LINUX ADAPTATION ---
# Instead of hardcoded C:/ paths, we use find_package to locate
# the libraries installed in the Docker container's Linux environment.

find_package(CURL REQUIRED)

# nlohmann_json is header-only. In our Dockerfile (nlohmann-json3-dev),
# it installs to /usr/include/nlohmann/.
# We can find it or just include the standard path.
find_package(nlohmann_json QUIET)

# --- ORIGINAL PATHS (Commented out for Windows reference) ---
# set(CURL_DIR "C:/Users/fabia/Downloads/curl-8.18.0_4-win64-mingw/curl-8.18.0_4-win64-mingw")
# set(JSON_DIR "C:/libs/nlohmann")

# include_directories("${CURL_DIR}/include")
# include_directories("${JSON_DIR}")

# --- NEW INCLUDE LOGIC ---
include_directories(${CURL_INCLUDE_DIRS})

# If find_package didn't find the json config, we point to the standard Linux include dir
if(NOT nlohmann_json_FOUND)
    include_directories("/usr/include")
endif()

add_executable(CryptoTracker main.cpp)

# CHANGED: Linking to the variables found by CMake instead of a specific .a file
target_link_libraries(CryptoTracker
        ${CURL_LIBRARIES}
)

# --- POST_BUILD COMMAND ---
# REMOVED: In Linux/Docker, we don't copy .dll files.
# The system links to .so (Shared Object) files automatically.
# add_custom_command(TARGET CryptoTracker POST_BUILD ...)