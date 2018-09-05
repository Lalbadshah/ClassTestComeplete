#!/usr/bin/python3
import urllib.request
import urllib.parse

import http.client

from pathlib import Path



if __name__ == "__main__":
    from sys import argv

    if len(argv) == 3:



        try:
            url = 'http://localhost:' + argv[1] + argv[2]

            f = urllib.request.urlopen(url)


        except http.client.BadStatusLine as e:
            e = str(e)
            i=1
            save = False
            while(not save):
                my_file = Path("web_response_"+str(i)+".txt")
                if not my_file.is_file():
                    text_file = open(my_file, "w")
                    text_file.write("%s" % e)
                    text_file.close()
                    save=True
                i+=1


    else:

        exit()




