from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


def main():
    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # resolution = 'i' means use intermediate resolution coastlines.
    # lon_0, lat_0 are the central longitude and latitude of the projection.
    plt.figure(figsize=(2,4))
    m = Basemap(projection='lcc',
            resolution=None,llcrnrlon=-48.88,llcrnrlat=-164.04,urcrnrlon=52.01,urcrnrlat=-58.04)
    #m = Basemap(width=12000000,height=9000000,projection='lcc',,
    #            resolution=None)
    # can get the identical map this way (by specifying width and
    # height instead of lat/lon corners)
    #m = Basemap(width=891185,height=1115557,\
    #            resolution='i',projection='cass',lon_0=-4.36,lat_0=54.7)
    m.shadedrelief()
    # draw parallels and meridians.
    plt.savefig('basemap.png',dpi=600)

if __name__ == '__main__':
    main()
