# Slideshare-Downloader
A Python program to download files from Slideshare as images and reassemble them into PDFs. 

WIP.

Given a series of URLs in a .csv file, this program will extract the first jpg image, iterate across the page numbers until a 404 is returned, combine the files into a PDF and then delete the JPG files for each URL.

This program does not require that Slideshare downloads are enabled, and does not require a user to have a Slideshare account.

To Do:

Incorporate OCR to deliver searchable PDFs.
