import os

# the world's worst static site generator
# not like i need anything fancy though

rss_head = '''
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
    <channel>
        <title>immutably aliased</title>
        <link>https://allie-m.github.io/blog.html</link>
        <description>Graphics programming and also other things</description>
        <language>en</language>
        %s
    </channel>
</rss>
'''
rss_item_template = '''
<item>
    <title>%s</title>
    <link>https://allie-m.github.io/blogposts/%s</link>
    <description>%s</description>
    <guid>%s</guid>
    <pubDate>%s</pubDate>
</item>
'''

# TODO FINISH THIS
def generate_rss():
    dir_path = "blogposts"
    with open("feed.xml", "w") as out:
        contents = ""
        for fname in os.listdir(dir_path):
            fpath = dir_path + fname
            with open(fpath, "r") as f:
                body = f.read() # TODO fill in
                contents += rss_item_template % "title" % "description" % "guid"
        out.write(rss_head % contents)

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <!-- <link rel="icon" href="icon.ico"> -->
    <title>allie-m // %s</title>
    <link href="%sstyle.css" rel="stylesheet" type="text/css"/>
    <meta name="viewport" content="width=450, initial-scale=1.0">
</head>
<body>
    <div id="header">
        <h2 id="header-title">%s</h2>
        <div id="menu">
            <ul>
                <li>
                    <a href="%sindex.html">home</a>
                </li>
                <li>
                    <a href="%sblog.html">blog</a>
                </li>
                <li>
                    <a href="%sprojects.html">projects</a>
                </li>
                <li>
                    <a href="%sother.html">other</a>
                </li>
            </ul>
        </div>
    </div>
    <div id="content">
        %s
    </div>
</body>
'''

# https://allefeld.github.io/nerd-notes/Markdown/A%20writer's%20guide%20to%20Pandoc's%20Markdown.html
# ^ use this as a guide for the markdown

def process_titles():
    d = {}
    with open("titles.txt", "r") as f:
        for line in f.read().strip().splitlines():
            if line != "":
                pair = line.split("=")
                key = pair[0].strip()
                val = pair[1].strip()
                d[key] = val
    return d

def process_dir(dir_path, titles, depth=0):
    for fname in os.listdir(dir_path):
        fpath = dir_path + fname
        if os.path.isdir(fpath):
            os.system("mkdir " + fpath[6:]) # no-op if the directory already exists
            process_dir(fpath + "/", titles, depth=depth+1) # recursive process
        else:
            # print(fpath, "pandoc -f markdown " + fpath + " > " + fpath[6:-3] + ".html")
            os.system("pandoc -f markdown " + fpath + " > temp")
            with open("temp", "r") as f:
                body = f.read()
                name = fpath[6:-3]
                title = titles.get(name)
                if title is None:
                    title = name
                genpath = fpath[6:-3] + ".html"
                back = "../" * depth
                contents = template % (title, back, title, back, back, back, back, body)
                with open(fpath[6:-3] + ".html", "w") as out:
                    out.write(contents)

titles = process_titles()
process_dir("pages/", titles)
os.system("rm temp")
