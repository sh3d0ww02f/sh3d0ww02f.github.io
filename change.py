template='''
<html>
  <head>
    <title>A Test For first step</title>
  </head>
  <body>
  {}
  </body>
</html>
'''
content="test<br>"
with open("index.html",'w')as f:
    f.write(template.format(content))
