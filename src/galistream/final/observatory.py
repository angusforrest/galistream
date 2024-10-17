from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


def main():
    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # resolution = 'i' means use intermediate resolution coastlines.
    # lon_0, lat_0 are the central longitude and latitude of the projection.
    m = Basemap(projection='merc',
            resolution=None,llcrnrlon=-168.,llcrnrlat=-45.,urcrnrlon=-61.,urcrnrlat=37.7,lat_ts=-20)
    #m = Basemap(width=12000000,height=9000000,projection='lcc',,
    #            resolution=None)
    # can get the identical map this way (by specifying width and
    # height instead of lat/lon corners)
    #m = Basemap(width=891185,height=1115557,\
    #            resolution='i',projection='cass',lon_0=-4.36,lat_0=54.7)
    m.shadedrelief()

    lon, lat =  -156.2569, 20.7074 # Location of Boulder
    # convert to map projection coords. 
    # Note that lon,lat can be scalars, lists or numpy arrays.
    xpt,ypt = m(lon,lat) 
    # convert back to lat/lon
    lonpt, latpt = m(xpt,ypt,inverse=True)
    m.plot(xpt,ypt,'bo')  # plot a blue dot there
    # put some text next to the dot, offset a little bit
    # (the offset is in map projection coordinates)
    plt.text(xpt+100000*2,ypt-100000*2,'Haleakala Observatory\n (%5.1fW,%3.1fN)' % (lonpt,latpt),va='top',ha='left')
    
    lon, lat =   -70.749417, -30.244639 # Location of Boulder
    # convert to map projection coords. 
    # Note that lon,lat can be scalars, lists or numpy arrays.
    xpt,ypt = m(lon,lat) 
    # convert back to lat/lon
    lonpt, latpt = m(xpt,ypt,inverse=True)
    m.plot(xpt,ypt,'bo')  # plot a blue dot there
    # put some text next to the dot, offset a little bit
    # (the offset is in map projection coordinates)
    plt.text(xpt-100000*2,ypt+100000*2,'Vera C. Rubin Observatory\n (%5.1fW,%3.1fN)' % (lonpt,latpt),va='bottom',ha='right')
    
    # draw parallels and meridians.
    plt.savefig('basemap.png',dpi=600)

if __name__ == '__main__':
    main()
