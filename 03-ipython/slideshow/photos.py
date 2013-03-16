#!/usr/bin/env python
import jinja2 as jin
import os, glob

# Generate a template
template_page = jin.Template('''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
  <head>
	<title>{{page}}</title>
	<link rel="stylesheet" type="text/css" href="style.css" media="screen" />
  </head>
  <body>
	<ul>	
		<li><a href="base_{{first}}.html">first</a></li>
		<li><a href="base_{{previous}}.html">previous</a></li>
		<li> {{current}} </li>
		<li><a href="base_{{next}}.html">next</a></li>
		<li><a href="base_{{last}}.html">last</a></li>
	</ul>
	<div id="photo"><img src="{{current}}"/></div>
  </body>
</html>
''')

photos = glob.glob('photos/*.jpg')

data = { 'first': 0, 'last': len(photos)-1}
for index, val in enumerate(photos):
    data['current'] = val
    data['previous'] = (index -1)%(len(photos))
    data['next'] = (index+1)%(len(photos))
    tmp = template_page.render(data)
    with open('base_'+str(index)+'.html','w') as f:
        f.write(tmp)

    
    