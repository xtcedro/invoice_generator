#include <gtk/gtk.h>
#include "gui/main_window.h"
#include "gui/menu_bar.h"

// Function to create the main window
void create_main_window(GtkApplication *app) {
    // Create the main application window
    GtkWidget *window = gtk_application_window_new(app);
    gtk_window_set_title(GTK_WINDOW(window), "Invoice Generator");
    gtk_window_set_default_size(GTK_WINDOW(window), 800, 600);

    // Create a vertical box layout to hold the menu bar and main content
    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 0);
    gtk_window_set_child(GTK_WINDOW(window), vbox);

    // Add the menu bar
    GtkWidget *menu_bar = create_menu_bar(app, GTK_WINDOW(window));
    gtk_box_append(GTK_BOX(vbox), menu_bar);

    // Create a placeholder widget for the main content area
    GtkWidget *main_content = gtk_label_new("Welcome to the Invoice Generator!");
    gtk_box_append(GTK_BOX(vbox), main_content);

    // Show the window and all child widgets
    gtk_widget_show(window);
}
