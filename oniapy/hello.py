# stream.py
from math import cos, sin

from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, Range1d, Button, BoxSelectTool
from bokeh.plotting import figure
from copy import deepcopy

p = figure(plot_width=1024, plot_height=512)

source = ColumnDataSource(data=dict(x=[1], y=[0]))
r = p.rect(x='x', y='y', width=17, height=50, alpha=0.5, color="red", source=source, width_units="screen", height_units="screen")
# r = p.rect(x=0, y=0, width=17, height=50, alpha=0.5, color="red", width_units="screen", height_units="screen")



class Update:
    def __init__(self):
        self.c = 0

    def __call__(self, *args, **kwargs):
        # print(r.data_source.data["y"])

        # source.data = dict(x=[1], y=[self.c+10])
        p.y_range.start = 0 + self.c
        p.y_range.end = 100 + self.c
        # p.y_range.bounds = (p.y_range.start, p.y_range.end)
        # p.rect(x='x', y='y', width=17, height=self.c, alpha=0.5, color="red", source=source, width_units="screen",
        #        height_units="screen")
        # r.data_source.data["y"] = self.c
        self.c -= .1

# create a callback that will add a number in a random location
def callback():
    p.rect(x=1, y=p.y_range.start-20, width=17, height=50, alpha=0.5, color="red", width_units="screen",
               height_units="screen")

# add a button widget and configure with the call back
button = Button(label="The KEY")
button.on_click(callback)



curdoc().add_periodic_callback(Update(), 10)
lay_out=layout([[p], [button]])
curdoc().add_root(lay_out)

if __name__ == '__main__':
    d = Update()()
# def update():
#     x, y = source.data['x'][-1], source.data['y'][-1]
#
#     # construct the new values for all columns, and pass to stream
#     new_data = dict(x=[x*cos(0.1) - y*sin(0.1)], y=[x*sin(0.1) + y*cos(0.1)])
#     source.stream(new_data, rollover=64)