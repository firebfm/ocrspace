# list of actual subtitles
subList = []
with open("subtitle.txt", "r", encoding="utf8", errors='ignore') as subFile:
    for subLine in subFile:
        subList.append(subLine.rstrip())

# sub.srt is empty sub with timings only
# replace every line that says sub duration: with actual subtitles

i = 0
with open("sub.srt", "r", encoding="utf8", errors='ignore') as file:
    for line in file:
        if line.startswith('s'):
            line = line.replace(line, subList[i]+'\n')
            i = i + 1
        with open("newFile.srt","a", encoding="utf8", errors='ignore') as newFile:
            newFile.write(line)
