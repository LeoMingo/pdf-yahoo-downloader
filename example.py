#import socket
#socket.setdefaulttimeout(15)
import pdf_web_downloader as pwd
#from urllib import urlretrieve

def main():
    pagehtml = ""
    for i in xrange(5):
        pagehtml += pwd.get_pagehtml_str(pwd.parse_key_to_search_string("machine learning pdf download", i))
        print "page {0} html download complete".format(str(i))


    llm = pwd.LinkListManip(pagehtml)
    pl = llm.download_pdf(dest_dir='./dl-pdf/')
    """
    for i in pl:
        urlretrieve(i, i.split('/')[-1])
        print i.split('/')[-1]
    """


if __name__ == "__main__":
    main()




