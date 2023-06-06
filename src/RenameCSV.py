#!/usr/bin/env python3

# This file is part of PythonUtils. https://github.com/Fabrizio927/PythonUtils
#
# Copyright (C) 2023 Fabrizio Traina (Fabrizio927) fabrizio.traina93@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import csv
import os

def rename_files(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if exists

        for index, row in enumerate(csv_reader):
            if len(row) < 2:
                print(f"Invalid row at index {index}. Skipping...")
                continue

            old_filename = row[0]
            new_filename = row[1]

            # Check if file exist
            if not os.path.isfile(old_filename):
                print(f"File '{old_filename}' does not exist. Skipping...")
                continue

            try:
                os.rename(old_filename, new_filename)
                print(f"File '{old_filename}' renamed to '{new_filename}'.")
            except OSError as e:
                print(f"Failed to rename file '{old_filename}'.",
                      "Error: {str(e)}")


if __name__ == "__main__":
    # TODO: Add Command line parser to different file name
    csv_input_file = "list.csv"
    rename_files(csv_input_file)
