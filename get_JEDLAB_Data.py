"""
    A short python script to harness Facebook Graph API to collect various data points for analysis
    
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

import fbconsole
import sys
import json
import time

fbconsole.logout()

fbconsole.authenticate()

allContent = []

i = 0
for post in fbconsole.iter_pages(fbconsole.get('/119600664905706/feed', {'limit':5})):
    if 'message' in post:
        thisLine = "\n"
    

        
        dateTime = post['created_time'].encode('utf8').split('T')
		
        thisLine = thisLine + dateTime[0]
		
        thisLine = thisLine +'\t' + dateTime[1].replace('+0000', '')

        thisLine = thisLine +'\t' + post['message'].encode('utf8').replace('\n', ' ')    
    
    
    	thisLine = thisLine +'\t' + post['from']['id'].encode('utf8')+'\t'+post['from']['name'].encode('utf8').replace('\n', ' ')
    
        if 'likes' in post:
            likes = 0
            newURL = "/"+post['id']+"/likes"
            for likeCount in fbconsole.iter_pages(fbconsole.get(newURL, {'limit':100})):
                likes = likes + 1           
            thisLine = thisLine +'\t' + str(likes)
        else:
            thisLine = thisLine +'\t' + '0'
    
    
    
        urlStub = (str(post['id']).replace('_','/posts/'))
      
   
        thisLine = thisLine +'\t' + 'https://www.facebook.com/'+urlStub

    
        thisLine = thisLine +'\t' + 'Post'   
         
         
         
        
        fd = open('fbposts.txt','a')
        fd.write(thisLine)
        fd.close()

        
        i=i+1
       # print "post "+str(i)



    if 'comments' in post:
        comment = 0
        
        newURL = "/"+post['id']+"/comments"
        for comments in fbconsole.iter_pages(fbconsole.get(newURL, {'limit':100})):
                
            thisLine = "\n"


            dateTime = comments['created_time'].encode('utf8').split('T')
                
            thisLine = thisLine + dateTime[0]
                
            thisLine = thisLine +'\t' + dateTime[1].replace('+0000', '')


            thisLine = thisLine +'\t' + comments['message'].encode('utf8').replace('\n', ' ')

            thisLine = thisLine +'\t' + comments['from']['id'].encode('utf8')+'\t'+comments['from']['name'].encode('utf8').replace('\n', ' ')


            thisLine = thisLine +'\t' + str(comments['like_count'])

                
                
            commentID = str(comments['id'])
                
            thisLine = thisLine +'\t' + 'https://www.facebook.com/'+urlStub+'?comment_id='+commentID          
                                                
            thisLine = thisLine +'\t' + 'Comment'
            
            
            

            fd = open('fbposts.txt','a')
            fd.write(thisLine)
            fd.close()

            
            
            comment = comment+1
            
        #    print str(i) + " comment "+ str(comment)




    