# py-mapplot
Draw simple colored maps from shapefiles using `matplotlib` and `basemap`.

## Simple example
```python
from mapplot.mapplot import MapPlot
import mapplot.projections as prj
import mapplot.func as func
import operator as op
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

mp = MapPlot(ax=ax,resolution='l',**prj.LAEA_EUROPE)

# Prepare map with regions and group by 'ID' property in shapefile
mp.load_regions('<path-to-shapefile>',key_fcn=op.itemgetter('ID'),filter_fcn=func.eq('LEVEL',0))
# Draw regions on map
mp.draw_regions()

# Color based on values in the dictionary
mp.color_from_values({'reg1': 1,'reg2':0},cmap=<colormap>)
mp.add_colorbar(label='Some quantity')
```
