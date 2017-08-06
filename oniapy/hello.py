# stream.py
from math import cos, sin

from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, Range1d, Button, BoxSelectTool
from bokeh.plotting import figure
from copy import deepcopy

p = figure(x_range=[0, 10], y_range=[0, 100])

source = ColumnDataSource(
    data=dict(left=[1], right=[2], top=[0], bottom=[10]))
last = p.quad(left="left", right="right", top="top", bottom="bottom", fill_color="#b3de69", source=source)


# source = ColumnDataSource(data=dict(x=[1], y=[0]))
# r = p.rect(x='x', y='y', width=17, height=50, alpha=0.5, color="red", source=source, width_units="screen", height_units="screen")
# r = p.rect(x=0, y=0, width=17, height=50, alpha=0.5, color="red", width_units="screen", height_units="screen")



class Update:
    def __init__(self):
        self.c = 0

    def __call__(self, *args, **kwargs):
        p.y_range.start = 0 + self.c
        p.y_range.end = 100 + self.c
        self.c -= .1
        pass


last_source = None


def push():
    global last_source
    h = 500
    print(p.y_range.start)

    last_source = ColumnDataSource(
        data=dict(left=[1], right=[2], top=[p.y_range.start], bottom=[p.y_range.start - h]))
    p.quad(left="left", right="right", top="top", bottom="bottom", fill_color="#b3de69", source=last_source)


def release():
    new = last_source.data
    new['bottom'] = [p.y_range.start]
    last_source.data = new


# add a button widget and configure with the call back
button = Button(label="ON")
button.on_click(push)

off = Button(label="OFF")
off.on_click(release)

curdoc().add_periodic_callback(Update(), 10)
lay_out = layout([[p], [button], [off]])
curdoc().add_root(lay_out)

if __name__ == '__main__':
    d = Update()()

    # def update():
    #     x, y = source.data['x'][-1], source.data['y'][-1]
    #
    #     # construct the new values for all columns, and pass to stream
    #     new_data = dict(x=[x*cos(0.1) - y*sin(0.1)], y=[x*sin(0.1) + y*cos(0.1)])
    #     source.stream(new_data, rollover=64)
