# Project definition
project('invoice_generator', 'cpp', version: '1.0', default_options: ['cpp_std=c++17'])

# GTK 4 dependency
gtk_dep = dependency('gtk4')

# Include directories for header files
inc = include_directories('include', 'include/gui')

# Source files
sources = [
  'main.cpp',
  'src/gui/main_window.cpp',
  'src/gui/menu_bar.cpp',
  'src/gui/dialogs.cpp',
]

# Build the executable
executable(
  'invoice_generator',         # Name of the output binary
  sources,                     # Source files
  include_directories: inc,    # Include directories
  dependencies: gtk_dep        # GTK 4 dependency
)
