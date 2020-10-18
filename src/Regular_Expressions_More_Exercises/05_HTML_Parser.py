import re

title_pattern = r'<title>([a-zA-Z\s]+)</title>'
body_pattern = r'<body>(.+)</body>'
tags_pattern = r"<(\"[^\"]*?\"|'[^']*?'|[^'\">])*>"

text = input()

title_match = re.finditer(title_pattern, text)
for match in title_match:
    print(f"Title: {match[1]}")

body_match = re.search(body_pattern, text)
content = re.sub(tags_pattern, '', body_match[1])
content = re.sub(r'\\n', '', content)
#content = re.sub(r'\s{2,}', ' ', content)
print(f"Content: {content}")
