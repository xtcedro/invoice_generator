#include <gtk/gtk.h>
#include "gui/main_window.h"

int main(int argc, char *argv[]) {
    // Create a GtkApplication with a unique application ID
    GtkApplication *app = gtk_application_new("com.pedrodominguez.invoicegenerator", G_APPLICATION_FLAGS_NONE);

    // Connect the "activate" signal to the create_main_window function
    g_signal_connect(app, "activate", G_CALLBACK(create_main_window), NULL);

    // Run the application
    int status = g_application_run(G_APPLICATION(app), argc, argv);

    // Free the GtkApplication object
    g_object_unref(app);

    return status;
}
