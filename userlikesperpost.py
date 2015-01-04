#!/usr/bin/env python
"""
    A short python script to analyze the most liked posts/comments by users
    
    Copyright (C) 2014  Russel M. Neiss
	Modifications copyright 2015 Marc Stober
	

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
#import matplotlib.mlab as mlab
#import matplotlib.pyplot as plt
import csv
import sys

user=[]

with open('fbposts.txt', 'rU') as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)

for i, rows in enumerate(d):
	if not len(rows): continue
	try:
		if rows[7] == "Post":
			user.append((rows[4]))
	except:
		print "Error in row %s:" % i
		print rows
		raise

unique_users = set(user)

fd = open('JEDLABUsers.txt','w')
thisLine= ('\neachuser\tpostCount\tlikeCount\tmean(likes)\tmedian(likes)')
fd.write(thisLine)
fd.close()

for eachuser in unique_users:

    likes=[]
    likeCount = 0
    postCount = 0
    for rows in d:

        if not len(rows): continue
        print rows[4], eachuser
        if rows[4] == eachuser:
            if rows[7] == "Comment":

                postCount = postCount + 1
                likeCount = likeCount + int(rows[5])
                likes.append(int(rows[5]))
    thisLine= ('\n' + eachuser + '\t'+ str(postCount)+ '\t'+ str(likeCount)+'\t'+str(np.mean(likes))+'\t'+str(np.median(likes)))


    fd = open('JEDLABUsers.txt','a')
    fd.write(thisLine)
    fd.close()

