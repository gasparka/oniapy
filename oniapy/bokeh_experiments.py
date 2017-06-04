from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
import numpy as np


# octave = [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7]
octave = [0,1,2,3,4,5,6]

def get_octave(i):
    return [x + i*7 for x in octave]

x = get_octave(0) + get_octave(1) + get_octave(2) + get_octave(3) + get_octave(4) + get_octave(5) + get_octave(6)
print(x)
y = [1] * len(x)

# source = ColumnDataSource(data=dict(x=[1], y=[0]))
# p.circle(x='x', y='y', size=12, fill_color='white', source=source)
#
plot = figure(x_range=(0-1, len(x)-1+1), plot_width=1024, plot_height=512)
plot.rect(x=x, y=y, width=17, height=50, alpha=0.5, color="red",
    width_units="screen", height_units="screen")
#
show(plot)