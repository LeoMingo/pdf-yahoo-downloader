#This script will search through a Yahoo as its search engien,
#to get a list of links given a keyword,
#then determine the links of pdfs and download them

from urllib2 import urlopen
import sys
import os

def check_idx_str(str0, str1, idx):
    for i in xrange(idx, idx+len(str1)):
        if str0[i] != str1[i-idx]:
            return False
    return True

def findAll(str0, str1):
    idx_list = []
    for i in xrange(len(str0)-len(str1)+1):
        if check_idx_str(str0, str1, i):
            idx_list.append(i)
    return idx_list

def concstr(str_list):
    s = ""
    for i in str_list:
        s+=i
    return s

def del_substr(str0, substr):
    return concstr(str0.split(substr))



def parse_key_to_search_string(strkey, pageidx=0):
    strkey_conc = strkey.replace(' ', '+')
    return "https://search.yahoo.com/search;_ylt=A0SO81H3z09Za58A3gZXNyoA;_ylu=X3oDMTEza3NiY3RnBGNvbG8DZ3ExBHBvcwMxBHZ0aWQDBHNlYwNwYWdpbmF0aW9u?p={0}&pz=10&bct=0&b={1}1&pz=10&bct=0&xargs=0".format(strkey_conc, str(pageidx))


def get_pagehtml_str(url):
    phtm = urlopen(url)
    return phtm.read()

def download_file(url, filename, dest='./'):
    if dest[-1] != '/':
        dest += '/'
    if os.path.isdir(dest):
        f = open(dest+filename, 'wb')
        conts = urlopen(url)
        f.write(conts.read())
        f.close()
        return
    else:
        print "Failed to download {0}, \"{1}\"  \
                does not exist".format(filename, dest)
        return

class LinkListManip(object):
    def __init__(self, phtm):
        self.link_list = []

        link_start = "<span class=\" fz-ms fw-m fc-12th wr-bw lh-17\">"
        link_end = "</span>"

        start = 0
        end = 0
        upperbound = len(phtm)-len(link_start)-len(link_end)
        for i in xrange(upperbound):
            if check_idx_str(phtm, link_start, i):
                i+=len(link_start)
                start = i
                for j in xrange(i, upperbound):
                    if check_idx_str(phtm, link_end, j):
                        end = j
                        self.link_list.append(phtm[start:end])
                        break

        #Get rid of <b> and </b> and
        #add 'http://' before the link
        attrs_to_del = ["<b>", "</b>", "..."]
        for i in xrange(len(self.link_list)):
            if check_idx_str(self.link_list[i], "http", 0)==False:
                self.link_list[i] = "http://" + self.link_list[i]
            for a in attrs_to_del:
                dl=findAll(self.link_list[i], a)
                if dl != []:
                    for d in dl:
                        self.link_list[i] =     \
                        del_substr(self.link_list[i], a)

    def download_pdf(self, inc_name=False, dest_dir='./'):
        #If inc_name is set to be true, the files to be downloaded will be name
        #using ascending numbers
        tok = ".pdf"
        pdf_links = [pdf_link for pdf_link in self.link_list
                     if pdf_link.split('.')[-1]=='pdf']
        if inc_name==True:
            cnt=0
            for pl in pdf_links:
                download_file(pl, str[cnt]+'.pdf', dest=dest_dir)
                print "{0}.pdf download complete".format(cnt)
                cnt += 1
        else:
            for pl in pdf_links:
                download_file(pl, pl.split('/')[-1], dest=dest_dir)
                print "{0} download complete".format(pl.split('/')[-1])



def main():
    return

if __name__ == "__main__":
    main()
