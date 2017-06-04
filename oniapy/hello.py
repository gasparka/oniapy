# stream.py
from math import cos, sin

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Range1d
from bokeh.plotting import figure


p = figure(x_range=(0, 10), plot_width=1024, plot_height=512)

# this is the data source we will stream to
source = ColumnDataSource(data=dict(x=[1], y=[0]))
r = p.rect(x='x', y='y', width=17, height=50, alpha=0.5, color="red", source=source, width_units="screen", height_units="screen")


class Update:
    def __init__(self):
        self.c = 0

    def __call__(self, *args, **kwargs):
        print(r.data_source.data["y"])
        r.data_source.data["y"][0] += 0.1
        r.update()
        # source.data['y'][-1] = source.data['y'][-1] + 0.1
        # print(source.data['y'][-1])
        # print('wtf')
        # construct the new values for all columns, and pass to stream
        # self.c += 0.1
        # new_data = dict(x=[1], y=[self.c])
        # p.x_range = Range1d(self.c, self.c+100)
        # p.y_range.start = self.c - 10
        # p.y_range.end = self.c + 10
        # source.data.update()
        # source.stream(new_data)


curdoc().add_periodic_callback(Update(), 10)
curdoc().add_root(p)

# def update():
#     x, y = source.data['x'][-1], source.data['y'][-1]
#
#     # construct the new values for all columns, and pass to stream
#     new_data = dict(x=[x*cos(0.1) - y*sin(0.1)], y=[x*sin(0.1) + y*cos(0.1)])
#     source.stream(new_data, rollover=64)