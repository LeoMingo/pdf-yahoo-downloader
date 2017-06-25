import pdf_web_downloader as pwd

def main():
    pagehtml = ""
    for i in xrange(3):
        pagehtml += pwd.get_pagehtml_str(pwd.parse_key_to_search_string("machine learning pdf download", i))
        print "page {0} html download complete".format(str(i))


    llm = pwd.LinkListManip(pagehtml)
    llm.download()

if __name__ == "__main__":
    main()




