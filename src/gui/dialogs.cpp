#include <gtk/gtk.h>
#include "dialogs.h"

// Function to show the About dialog
void show_about_dialog(GtkWindow *parent_window) {
    GtkWidget *about_dialog = gtk_message_dialog_new(
        parent_window,
        GTK_DIALOG_MODAL,
        GTK_MESSAGE_INFO,
        GTK_BUTTONS_OK,
        "Invoice Generator\nVersion 1.0\n\n"
        "Developed by Pedro Dominguez\n"
        "This application helps manage invoices, services, and customers."
    );
    gtk_window_set_title(GTK_WINDOW(about_dialog), "About Invoice Generator");
    gtk_dialog_run(GTK_DIALOG(about_dialog));
    gtk_widget_destroy(about_dialog);
}

// Function to show a Preferences dialog
void show_preferences_dialog(GtkWindow *parent_window) {
    GtkWidget *preferences_dialog = gtk_dialog_new_with_buttons(
        "Preferences",
        parent_window,
        GTK_DIALOG_MODAL,
        "_OK",
        GTK_RESPONSE_OK,
        "_Cancel",
        GTK_RESPONSE_CANCEL,
        NULL
    );

    // Content area to add widgets
    GtkWidget *content_area = gtk_dialog_get_content_area(GTK_DIALOG(preferences_dialog));
    GtkWidget *label = gtk_label_new("Preferences settings will go here.");
    gtk_box_append(GTK_BOX(content_area), label);

    gtk_widget_show(label);
    gtk_widget_show(preferences_dialog);

    // Run the dialog and handle responses
    gint response = gtk_dialog_run(GTK_DIALOG(preferences_dialog));
    if (response == GTK_RESPONSE_OK) {
        g_print("Preferences saved.\n");
    } else {
        g_print("Preferences dialog canceled.\n");
    }

    gtk_widget_destroy(preferences_dialog);
}
