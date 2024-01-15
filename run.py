import csv
import os
from odf import opendocument, text, teletype
from odf.element import Element
from random import sample, shuffle


def read_square_options(path_to_file: str = "./inputs/bingo_squares.csv"):
    with open(path_to_file) as csvfile:
        all_squares = [square[0] for square in csv.reader(csvfile, delimiter="'", quotechar="'")]
        shuffle(all_squares)
        return all_squares


def replace_element_text(element: Element, old_text: str, new_text: str):
    text_to_add = old_text.replace(old_text, new_text)
    new_element = text.P()
    new_element.setAttribute("stylename", element.getAttribute("stylename"))
    new_element.addText(text_to_add)
    element.parentNode.insertBefore(new_element, element)
    element.parentNode.removeChild(element)


def main(contestant_name):
    document = opendocument.load("./inputs/template.odt")
    seen_squares = set()
    elements = [element for element in document.getElementsByType(text.P)]

    for element in elements:
        extracted_text = teletype.extractText(element)

        # Only replace table cells with numeric text
        if not extracted_text.isnumeric():
            continue

        bingo_squares = read_square_options()

        selection = bingo_squares[0]
        while selection in seen_squares:
            selection = sample(bingo_squares, 1)[0]
        seen_squares.add(selection)

        replace_element_text(element, extracted_text, selection)

    print(f"{contestant_name}'s bingo sheet generated!\n")
    document.save(f"./outputs/{contestant_name}_bingo_sheet.odt")


if __name__ == "__main__":

    print("Checking if outputs directory exists...")
    if not os.path.exists("./outputs"):
        print("Directory does not exist, creating...")
        os.mkdir("outputs")
        print("Created, moving on to sheet generation...\n")
    else:
        print("Directory exists, moving on to sheet generation...\n")

    contestants = ["Anthony", "Austin", "Cam", "Josh", "Miranda", "Rabih", "Taylor"]
    for contestant in contestants:
        print(f"Generating {contestant}'s bingo sheet...")
        main(contestant)

    print(f"Created {len(contestants)} bingo sheets, have fun!")
