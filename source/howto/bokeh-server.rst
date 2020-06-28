.. index:: Holoviz
.. index:: Bokeh
.. _bokeh-plot-server:

============================
Bokeh, Panel, Holoviz, ...
============================

.. note::

    This is user-contributed content. Credits go to Dr. A. Khalatyan (researcher at IT-eScience, AIP, Potsdam)!


For deploying an interactive plots based on `Bokeh`_, `Panel`_, `Holoviz`_ or similar libraries we can use the :ref:`server feature of CoCalc <webserver>`, like in the examples for the Tensorboard:

.. highlight:: python

1. create a python file ``holo.py``::

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

2. If you are using a self hosted instance, replace ``cocalc.com`` with your domain.
3. Start it in the terminal::

        python holo.py

3. now your interactive `Holoview`_ application is available in the following URL::


        https://cocalc.com/[PROJECT_ID]/server/8006/

   or run in a terminal::

       echo "https://cocalc.com/$COCALC_PROJECT_ID/server/8006/"


.. _bokeh: https://docs.bokeh.org/
.. _panel: https://panel.holoviz.org/reference/panes/Matplotlib.html
.. _holoviz: https://holoviz.org/
.. _holoview: http://holoviews.org/user_guide/Deploying_Bokeh_Apps.html