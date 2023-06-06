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

def main():
    FileName = 'Split.csv'
    Category = 'Ordered by'
    SplitCSV(FileName, Category)
    pass

def SplitCSV(FileName, Category):
    with open(FileName) as fin:    
        csvin = csv.DictReader(fin)
        # Category -> open file lookup
        outputs = {}
        for row in csvin:
            cat = row[Category]
            # Open a new file and write the header
            if cat not in outputs:
                # fout = open('{}.csv'.format(cat), 'w')
                fout = open('New - {}.csv'.format(cat), 'w', newline='')
                dw = csv.DictWriter(fout, fieldnames=csvin.fieldnames)
                dw.writeheader()
                outputs[cat] = fout, dw
            # Always write the row
            outputs[cat][1].writerow(row)
        # Close all the files
        for fout, _ in outputs.values():
            fout.close()

if __name__ == '__main__':
    main()
