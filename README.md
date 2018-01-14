# Resume Miner

A script to rate a Resume for a given company.



## cortical.io

Welcome to Resume Miner source code page.

Release Version: 0.2

This page contains
<UL>
<LI><B>Introduction</B></LI>
<LI><B>Dependencies</B></LI>
<LI><B>How to run</B></LI>



### Introduction
A script to rate the competency of a resume in PDF format by comparing it to a company's requirements mentioned on its website.:

### Dependencies
* Setuptools: `sudo apt-get install python-setuptools`
* Sklearn : `pip install sklearn`
* Slate : `sudo easy_install slate`
* BeautifulSoup : `pip install beautifulsoup4`
* Requests : `pip install requests`
* Grammar Check engine : `pip install --user --upgrade grammar-check`


### How to use/build
* You will need Python (version 2.7 has been tested).
* Install dependencies
* Clone all the sources from our Github repository.
* Go <a href="http://www.cortical.io/resources_apikey.html">here</a>, register for free API key.
* Copy the key received in the mail and paste it in config.py


### How to run
* Rename your resume to 'resume.pdf' and copy-replace the 'resume.pdf' file it in the cloned repo directory. 
* In terminal, navigate to source
* `python Ex1.py`
