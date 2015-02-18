# py-mapplot
Draw simple colored maps from shapefiles using `matplotlib` and `basemap`.

## Simple example
```python
from mapplot import MapPlot
import projections as prj
import funcs
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

mp = MapPlot(ax=ax,resolution='l',**prj.LAEA_EUROPE)

# Prepare map with regions and group by 'ID' property in shapefile
mp.load_regions('<path-to-shapefile>',key_fcn=funcs.prop('ID'))

# Color based on values in the dictionary
mp.color_from_values({'reg1': 1,'reg2':0})
mp.add_colorbar(label='Some quantity')
```
