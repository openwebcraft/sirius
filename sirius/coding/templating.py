import jinja2

DEFAULT_TEMPLATE = '''\
<html>
  <head><meta charset="utf-8"></head>
  <body style="background-color: #ffffff">
    {{ raw_html|safe }}
  </body>
</html>
'''

ENV = jinja2.Environment()



# TODO apply scrubber library if wanted.
# https://pypi.python.org/pypi/scrubber

def default_template(raw_html):
    t = ENV.from_string(DEFAULT_TEMPLATE)
    return t.render(raw_html=raw_html).encode('utf-8')
