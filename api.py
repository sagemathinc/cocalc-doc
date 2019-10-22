#!/usr/bin/env python3
# run this via $ make api in the root dir
# depends on api.json, which is exported via scripts/export-api-doc.ts in cocalc

import json
from os.path import join
from os import makedirs

outdir = join('source', 'api')
from shutil import rmtree
rmtree(outdir, ignore_errors=True)
makedirs(outdir)

api = json.load(open('api.json'))

# footer

FOOTER = '''

This information is based on [{shortrev}](https://github.com/sagemathinc/cocalc/commit/{gitrev}) exported at ``{timestamp}``.

'''

with open(join(outdir, '_footer.md'), 'w') as out:
    rev = api['gitrev'][:10]
    out.write(FOOTER.format(shortrev=rev, **api))

# intro
with open(join(outdir, 'index.md'), 'w') as out:
    out.write(api['intro'])

# index
index_tmpl = '''
.. index:: API

====================
API
====================

.. mdinclude:: index.md

.. toctree::
   :caption: API Endpoints
   :maxdepth: 1

{endpoints}

--------------

Examples
=================

.. toctree::
   :maxdepth: 1

   api_examples

'''

with open(join(outdir, 'index.rst'), 'w') as out:
    entries = (f'   {k}' for k in sorted(api['events']))
    api['endpoints'] = '\n'.join(entries)
    out.write(index_tmpl.format(**api))

with open(join(outdir, 'api_examples.rst'), 'w') as out:
    out.write('.. include:: ../api-examples.inc')

# events

event_tmpl = '''
# {name}

{fields_md}

{description}

---

.. mdinclude:: _footer.md
'''

for name, event in sorted(api['events'].items()):
    #pprint(event)
    with open(join(outdir, f'{name}.md'), 'w') as out:
        fd = (f'* ``{k}``: {v}' for k, v in event['fields'].items())
        event['fields_md'] = '\n'.join(fd)
        out.write(event_tmpl.format(name=name, **event, **api))
