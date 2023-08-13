set(COMMON_DIR "common")
set(COMMON_HEADERS)
set(COMMON_SOURCES)

list(APPEND COMMON_HEADERS ${COMMON_DIR}/load_buffer.h)
list(APPEND COMMON_SOURCES ${COMMON_DIR}/load_buffer.cpp)

source_group("${COMMON_DIR}" FILES ${COMMON_HEADERS} ${COMMON_SOURCES})

list(APPEND LIBRARY_HEADERS ${COMMON_HEADERS})
list(APPEND LIBRARY_SOURCES ${COMMON_SOURCES})

add_library(Library STATIC ${LIBRARY_HEADERS} ${LIBRARY_SOURCES})
add_library(Vodka::Library ALIAS Library)

if(NOT BUILD_SHARED_LIBS)
  target_compile_options(Library PUBLIC ${NO_SHARED_LIBS_FLAG})
  target_compile_options(Library PUBLIC ${STATIC_LINK_FLAG})
endif()

if(NO_EXCEPTION)
  target_compile_options(Library PUBLIC ${NO_EXCEPTION_FLAG})
  target_compile_definitions(Library PUBLIC VODKA_NO_EXCEPTION)
endif()

if(WARNING_AS_ERROR)
  target_compile_options(Library PUBLIC ${WARNING_AS_ERROR_FLAG})
endif()
