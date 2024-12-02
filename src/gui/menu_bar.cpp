#include <gtk/gtk.h>
#include "gui/menu_bar.h"
#include "gui/dialogs.h"

// Callback for the "New Invoice" menu item
static void on_new_invoice_activated(GtkMenuItem *menu_item, gpointer user_data) {
    g_print("New Invoice action triggered.\n");
    // Logic for creating a new invoice goes here
}

// Callback for the "Open Invoice" menu item
static void on_open_invoice_activated(GtkMenuItem *menu_item, gpointer user_data) {
    g_print("Open Invoice action triggered.\n");
    // Logic for opening an existing invoice goes here
}

// Callback for the "Quit" menu item
static void on_quit_activated(GtkMenuItem *menu_item, gpointer app) {
    g_application_quit(G_APPLICATION(app));
}

// Callback for the "About" menu item
static void on_about_activated(GtkMenuItem *menu_item, gpointer parent_window) {
    show_about_dialog(GTK_WINDOW(parent_window));
}

// Callback for the "Preferences" menu item
static void on_preferences_activated(GtkMenuItem *menu_item, gpointer parent_window) {
    show_preferences_dialog(GTK_WINDOW(parent_window));
}

// Function to create the menu bar
GtkWidget* create_menu_bar(GtkApplication *app, GtkWindow *parent_window) {
    // Create a menu bar
    GtkWidget *menu_bar = gtk_menu_bar_new();

    // Create the "File" menu
    GtkWidget *file_menu = gtk_menu_new();
    GtkWidget *file_item = gtk_menu_item_new_with_label("File");
    gtk_menu_item_set_submenu(GTK_MENU_ITEM(file_item), file_menu);

    GtkWidget *new_invoice_item = gtk_menu_item_new_with_label("New Invoice");
    g_signal_connect(new_invoice_item, "activate", G_CALLBACK(on_new_invoice_activated), NULL);
    gtk_menu_shell_append(GTK_MENU_SHELL(file_menu), new_invoice_item);

    GtkWidget *open_invoice_item = gtk_menu_item_new_with_label("Open Invoice");
    g_signal_connect(open_invoice_item, "activate", G_CALLBACK(on_open_invoice_activated), NULL);
    gtk_menu_shell_append(GTK_MENU_SHELL(file_menu), open_invoice_item);

    GtkWidget *quit_item = gtk_menu_item_new_with_label("Quit");
    g_signal_connect(quit_item, "activate", G_CALLBACK(on_quit_activated), app);
    gtk_menu_shell_append(GTK_MENU_SHELL(file_menu), quit_item);

    gtk_menu_bar_append(GTK_MENU_BAR(menu_bar), file_item);

    // Create the "Edit" menu
    GtkWidget *edit_menu = gtk_menu_new();
    GtkWidget *edit_item = gtk_menu_item_new_with_label("Edit");
    gtk_menu_item_set_submenu(GTK_MENU_ITEM(edit_item), edit_menu);

    GtkWidget *preferences_item = gtk_menu_item_new_with_label("Preferences");
    g_signal_connect(preferences_item, "activate", G_CALLBACK(on_preferences_activated), parent_window);
    gtk_menu_shell_append(GTK_MENU_SHELL(edit_menu), preferences_item);

    gtk_menu_bar_append(GTK_MENU_BAR(menu_bar), edit_item);

    // Create the "Help" menu
    GtkWidget *help_menu = gtk_menu_new();
    GtkWidget *help_item = gtk_menu_item_new_with_label("Help");
    gtk_menu_item_set_submenu(GTK_MENU_ITEM(help_item), help_menu);

    GtkWidget *about_item = gtk_menu_item_new_with_label("About");
    g_signal_connect(about_item, "activate", G_CALLBACK(on_about_activated), parent_window);
    gtk_menu_shell_append(GTK_MENU_SHELL(help_menu), about_item);

    gtk_menu_bar_append(GTK_MENU_BAR(menu_bar), help_item);

    return menu_bar;
}
