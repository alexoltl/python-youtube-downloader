from pytube import YouTube
from youtubesearchpython import VideosSearch
import time

while True:
    print("Welcome to the python youtube downloader.\n")
    print("1. Search\n2. Link\n3. About/How to use\n")
    ask = input("Enter an option from 1-3: ")
    if ask == "1":
        asksearch = input("Enter a search term here: ")
        search = VideosSearch(asksearch)
        
        sr = search.result()["result"]
        sr1 = sr[1]
        sr2 = sr1["id"]
        
        svideolink = "https://www.youtube.com/watch?v=" + sr2

        yts = YouTube(svideolink)

        print(f"\nTitle: {yts.title}")
        print(f"Thumbnail: {yts.thumbnail_url}")
        print(f"Views: {yts.views}")

        yss = yts.streams.get_highest_resolution()
        print("\nDownloading in 3 seconds... This will be downloaded in the folder you have this python program in.")
        time.sleep(3)
        yss.download()
        print("Downloaded.")

    if ask == "2":
        videolink = input("\nPaste video link here: ")
        ytl = YouTube(videolink)

        print(f"\nTitle: {ytl.title}")
        print(f"\nThumbnail: {ytl.thumbnail_url}")
        print(f"\nViews: {ytl.views}")

        ysl = ytl.streams.get_by_itag(22)
        print("\n\nDownloading in 3 seconds... This will be downloaded in the folder you have this file in")
        time.sleep(3)
        ysl.download()
        print("Downloaded.")
        
    if ask == "3":
        print("\nThis is a small personal project made by me, alexoltl.")
        print("I used pytube to code this.")
        print("\n\nHow to use")
        print("\nThis downloads youtube videos using pytube. There are two ways to get to the video to start downloading. First way is to search for the video.")
        print("To search, simply enter a search term when prompted. This will always grab the top result. Make sure that it's the right one, for that reason I've added a wait until it starts downloading.")
        print("\n\nTo find via a link, just send a valid youtube link. It will crash if you send something else. A valid youtube link has to be the full youtube link (contains https) but doesn't have to have www. For example: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("\n\nThat's about it for this program. You now know everything about this program.\n")
    else:
        print("That is an invaild input. Try again.")