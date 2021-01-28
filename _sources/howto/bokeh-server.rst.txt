.. index:: Holoviz
.. index:: Bokeh

.. highlight:: python

============================
Bokeh / Holoview Server
============================

.. note::

    This is user-contributed content. Credits go to Dr. A. Khalatyan (researcher at IT-eScience, AIP, Potsdam)!


.. _bokeh-server:

Bokeh / DASK server
===========================

The combination of the `Bokeh`_, `DASK`_ and `Holoview`_ is allowing us to interactively render large datasets.
This example is deploying an interactive visualization of a `DASK`_ dataframe via a `Holoview`_ application:

1. create a file named ``server_app.py``::

        import os
        import dask.dataframe as dd
        import holoviews as hv
        import pandas as pd
        import numpy as np
        from holoviews.operation.datashader import datashade

        hv.extension('bokeh')

        # 1. Load data
        ## load from a parquet file:
        #ddf = dd.read_parquet("data.parq")[['xgal', 'ygal']].persist()

        # or let's just generate some random data for demo
        df = pd.Dataframe({
            'xgal': np.random.randn(1000),
            'ygal': np.random.randn(1000)
        })
        ddf = dd.from_pandas(df)

        # 2. Datashade it

        points = hv.Points(ddf, kdims=['xgal', 'ygal'])
        shaded = datashade(points).opts(plot=dict(width=800, height=600))

        # 3. Instead of Jupyter's automatic rich display, render the object as a bokeh document
        doc = hv.renderer('bokeh').server_doc(shaded)
        doc.title = 'HoloViews Bokeh App'


2. in terminal start the Bokeh server::

        bokeh serve --disable-index-redirect --allow-websocket-origin='*' --port 5006 server_app.py

3. now your interactive plot is accessible on following URL::

        https://cocalc.com/[PROJECT_ID]/server/5006/server_app

   or run this line in a terminal to get the URL and click on it::

       echo "https://cocalc.com/$COCALC_PROJECT_ID/server/5006/server_app"


.. _holoview-server:

Holoview App
============================


For deploying an interactive plots based on `Bokeh`_, `Panel`_, `Holoviz`_ or similar libraries we can use the :ref:`server feature of CoCalc <webserver>`, like in the examples for the Tensorboard:

1. Create a python file ``holo.py``. (If you are using a self hosted instance, replace ``cocalc.com`` with your domain)::

        import holoviews as hv
        import panel as pn
        import numpy as np

        hv.extension('bokeh')

        def sine(frequency, phase, amplitude):
            xs = np.linspace(0, np.pi*4)
            return hv.Curve((xs, np.sin(frequency*xs+phase)*amplitude)).options(width=800)

        if __name__ == '__main__':
            ranges = dict(frequency=(1, 5), phase=(-np.pi, np.pi), amplitude=(-2, 2), y=(-2, 2))
            dmap = hv.DynamicMap(sine, kdims=['frequency', 'phase', 'amplitude']).redim.range(**ranges)
            pn.serve(dmap, port=8006, allow_websocket_origin=["cocalc.com"], show=False)

2. Start it in the terminal::

        python3 holo.py

3. now your interactive `Holoview`_ application is available in the following URL::


        https://cocalc.com/[PROJECT_ID]/server/8006/

   or run this line in a terminal to get the URL and click on it::

       echo "https://cocalc.com/$COCALC_PROJECT_ID/server/8006/"

.. _dask: https://dask.org/
.. _bokeh: https://docs.bokeh.org/
.. _panel: https://panel.holoviz.org/reference/panes/Matplotlib.html
.. _holoviz: https://holoviz.org/
.. _holoview: http://holoviews.org/user_guide/Deploying_Bokeh_Apps.html
