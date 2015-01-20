import StringIO
import zipfile
from requests import Session
from os import path, rename
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup


class Downloader(object):
    def __init__(self, course_list, curriculum_home=None):
        self.courses = course_list
        self.curriculum_home = curriculum_home
        self.s = Session()

    def download_courseware(self, course_url):
        download_url = "/".join([course_url.strip("/"), "download-course-materials/"])
        download_page = self.s.get(download_url).content
        soup = BeautifulSoup(download_page)
        title = soup.find("title").text.split("|")[1].strip().replace(" ", "_")
        print "Saving as {0}".format(title)
        z_url = "http://ocw.mit.edu" + soup.find('a', target="blank").get('href')
        z = self.s.get(z_url)
        # import ipdb; ipdb.set_trace()
        zf = zipfile.ZipFile(StringIO.StringIO(z.content))
        zf.extractall(path=self.curriculum_home)
        rename(zf.namelist()[1].split("/")[0], title)


    def download_curriculum(self):
        for c in self.courses:
            try:
                print "Downloading {0}".format(c.split("/")[-1])
                self.download_courseware(c)
                print "SUCCESS"
            except Exception as e:
                print "FAILED:", e
