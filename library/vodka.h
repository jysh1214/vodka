/**
 * @file vodka.h
 * @author Alex Chiang
 * @brief vodka header file.
 */
#ifndef VODKA_H
#define VODKA_H

#include <iostream>

/* Display function setting */
#if defined(__cpp_lib_syncbuf)
#include <syncstream>
std::osyncstream VODKA_DISPLAY(std::cout);
#else
#define VODKA_DISPLAY (std::cout)
#endif

/* Debug log setting */
#if defined(DEBUG)
#include <source_location>
#define VODKA_DEBUGLOG(message)                                                \
  do {                                                                         \
    VODKA_DISPLAY << "file: " << location.file_name() << "("                   \
                  << location.line() << ":" << location.column() << ")"        \
                  << location.function_name() << ": " << message << "\n";      \
  } while (0)
#else
#define VODKA_DEBUGLOG(message) // disable it
#endif

/* Exception setting */
#if defined(VODKA_NO_EXCEPTION)
#define VODKA_THROW(error)
#else
#define VODKA_THROW(error) throw error
#endif

#if defined(DEBUG)
#endif

#endif // VODKA_H
