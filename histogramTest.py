#!/usr/bin/env python
"""
    A short python script to create shiny graphs based on Facebook Graph API collected
    
    Copyright (C) 2014  Russel M. Neiss

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
    
"""


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv


with open('fbposts.txt', 'rU') as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)

for rows in d:
    if not len(rows): continue
    if rows[7] == "Post":
        x.append(int(rows[5]))


unique_values = set(x)
bins = len(unique_values) 

print np.mean(x)
print np.median(x)
print np.std(x)
print min(unique_values)
print max(unique_values)
    
#plt.hist(x, bins, normed=1, range=[min(unique_values),max(unique_values)])

plt.hist(x)


plt.title('Distribution of Posts Per User')
plt.xlabel('Number Posts')
plt.ylabel('Frequency')
plt.subplots_adjust(left=0.15)

plt.show()
