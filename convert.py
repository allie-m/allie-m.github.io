import os

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <!-- <link rel="icon" href="icon.ico"> -->
    <title>%s</title>
    <link href="%sstyle.css" rel="stylesheet" type="text/css"/>
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
                    <a href="%smaps.html">maps</a>
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
