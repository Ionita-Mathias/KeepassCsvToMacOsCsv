import csv
import importlib.util
import locale
import os
import tkinter as tk
from tkinter import filedialog


MESSAGES = {
    "input_title": {
        "fr_FR": "Choisir le fichier CSV d'entrée",
        "en_US": "Choose the input CSV file"
    },
    "success": {
        "fr_FR": "Fichier CSV réorganisé créé avec succès.",
        "en_US": "CSV file successfully reorganized."
    },
    "no_input_selected": {
        "fr_FR": "Aucun fichier d'entrée sélectionné. Sortie du script.",
        "en_US": "No input file selected. Exiting the script."
    },
    "no_output_specified": {
        "fr_FR": "Aucun fichier de sortie spécifié. Sortie du script.",
        "en_US": "No output file specified. Exiting the script."
    },
    "installing_dependencies": {
        "fr_FR": "Installation des dépendances...",
        "en_US": "Installing dependencies..."
    },
    "dependencies_installed": {
        "fr_FR": "Dépendances installées avec succès.",
        "en_US": "Dependencies installed successfully."
    },
    "all_dependencies_installed": {
        "fr_FR": "Toutes les dépendances sont déjà installées.",
        "en_US": "All dependencies are already installed."
    }
}


def get_message(code):
    language = locale.getdefaultlocale()[0]
    return MESSAGES[code][language]


def install_dependencies():
    missing_packages = [package for package in [
        "csv", "tkinter"] if importlib.util.find_spec(package) is None]

    if missing_packages:
        print(get_message("installing_dependencies"))
        os.system(f"pip install {' '.join(missing_packages)}")
        print(get_message("dependencies_installed"))
    else:
        print(get_message("all_dependencies_installed"))


def choose_input_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title=get_message("input_title"))
    return file_path


def create_output_file(input_file):
    input_directory, input_filename = os.path.split(input_file)
    output_filename = os.path.splitext(input_filename)[0] + "-ForMacOs.csv"
    output_file = os.path.join(input_directory, output_filename)
    return output_file


def reorganize_csv(input_file, output_file):
    column_mapping = {
        "Title": "Account",
        "URL": "Web Site",
        "Username": "Login Name",
        "Password": "Password",
        "Notes": "Comments",
        "OTPAuth": ""
    }

    fieldnames_output = ["Title", "URL",
                         "Username", "Password", "Notes", "OTPAuth"]

    data = []
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fieldnames_input = next(csvreader)

        for row in csvreader:
            new_row = []
            for column_output in fieldnames_output:
                column_input = column_mapping.get(column_output)
                if column_input and column_input in fieldnames_input:
                    index = fieldnames_input.index(column_input)
                    value = row[index] if index < len(row) else ""
                else:
                    value = ""
                new_row.append(value)
            data.append(new_row)

    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fieldnames_output)
        csvwriter.writerows(data)

    print(get_message("success"))


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    install_dependencies()

    input_file_path = choose_input_file()
    if not input_file_path:
        print(get_message("no_input_selected"))
        exit()

    output_file_path = create_output_file(input_file_path)

    reorganize_csv(input_file_path, output_file_path)
