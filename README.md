#MIT Courseware Downloader

It's a small utility to download MIT courseware and unpackage it for you.

Usage


```
from MITDownloader import Downloader


mycourses = [
    "http://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010",
    "http://ocw.mit.edu/courses/mathematics/18-013a-calculus-with-applications-spring-2005",
    "http://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010",
    "http://ocw.mit.edu/courses/mathematics/18-034-honors-differential-equations-spring-2009",
    "http://ocw.mit.edu/courses/mathematics/18-098-street-fighting-mathematics-january-iap-2008/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010",
    "http://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014",
    "http://ocw.mit.edu/courses/mathematics/18-901-introduction-to-topology-fall-2004",
    "http://ocw.mit.edu/courses/mathematics/18-s996-category-theory-for-scientists-spring-2013/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-002-circuits-and-electronics-spring-2007/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-007-electromagnetic-energy-from-motors-to-lasers-spring-2011",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-012-microelectronic-devices-and-circuits-spring-2009/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-452-principles-of-wireless-communications-spring-2006/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-331-advanced-circuit-techniques-spring-2002/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-301-solid-state-circuits-fall-2010/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2009/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-011-introduction-to-communication-control-and-signal",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-933j-the-structure-of-engineering-revolutions-fall-2001",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-849-geometric-folding-algorithms-linkages-origami-polyhedra-fall-2012/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-050j-information-and-entropy-spring-2008/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-830-database-systems-fall-2010/",
    "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s096-effective-programming-in-c-and-c-january-iap-2014/",
]

d = Downloader(mycourses, curriculum_home="/your/path/here/")
d.download_curriculum()
# Now wait a while for all the downloads
```