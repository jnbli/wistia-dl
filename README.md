# Wistia-DL

## Purpose
Inspired by [YouTube-DL](https://ytdl-org.github.io/youtube-dl/), this script downloads videos from Wistia

## Usage
``` wisita-dl sxpw0wdxff```
Here, sxpw0wdxff is the video id. The full video url is: https://fast.wistia.net/embed/iframe/sxpw0wdxff

## Lesson I Learned
Only after creating this script did I realize that YouTube-DL already has this functionally. In fact, it can download videos from YouTube and [a handful of other sites](https://ytdl-org.github.io/youtube-dl/supportedsites.html). To download the previous Zendesk video using YouTube-DL, simply use the following in terminal:
```youtube-dl --default-search wistia sxpw0wdxff```
