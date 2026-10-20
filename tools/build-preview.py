"""Gera a versão de prévia (Artifact) do site: sem doctype/head/body e com a logo embutida."""
import base64, re, sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf8").read()
logo = "data:image/png;base64," + base64.b64encode(open("assets/logo-sirius-claro.png", "rb").read()).decode()
head = re.search(r"<head>(.*?)</head>", s, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", s, re.S).group(1)
head = re.sub(r'<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*|<link rel="icon"[^>]*>\s*', "", head)
title = re.search(r"<title>.*?</title>", head).group(0)
head = head.replace(title, "", 1)
page = title + '\n<meta name="claude:viewport-fit-sides" content="cover">\n' + head.strip() + "\n" + body.strip() + "\n"
open(out, "w", encoding="utf8").write(page.replace("assets/logo-sirius-claro.png", logo))
