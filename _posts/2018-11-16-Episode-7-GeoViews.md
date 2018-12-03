---
layout: post
title: Episode 7 - GeoViews - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=s9REOti_vzs&t=729s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [GeoViews](http://geo.holoviews.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Philipp Rudiger, works on consulting projects for Anaconda Inc. and is a core developer and maintainer of various PyViz projects.

### Project Overview

GeoViews is an open-source geographic visualization library, that is built on Holoviews and Cartopy, two other open source projects.  Currently, this project has 185 stars on Github and has about 3k downloads/month across PyPI and conda.

This project came out of a collaboration with the MetOffice to explore Iris gridded datasets, which were capable of showing gradient datasets for things like temperature or precipitation over time. Initially, they built this system on Matplotlib/Cartopy so that they could visualize the datasets, but this process could be somewhat painful.  The original implimentation for GeoViews was with a Ph.D. project involving mapping neural nets.  The refinement of this project improved as time went on and eventually grew to add support for bokeh.  Once Bokeh was integrated, the platform became much more interactive for the user.

GeoViews attempts to make it simple for HoloViews users to situate data geographically whenever that’s appropriate.  Additionally, it makes the process more interactive for the exploration of large GIS data by leveraging Datashader/Dask.  This means that it helps to serve users of data from areas such as; climatology, meteorology, and remote sensing.  With the implementation of Datashader you can dynamically shade these datasets, and then scale the dataset using Dask.  GeoViews also allows you to quickly combine datasets from different sources, gridded: Xarray/Iris, tabular: Pandas/Dask/Arrays, geometry: Geopandas/Shapefiles/Shapely.
While the plotting space is rather crowded, the geographic plotting space is not as crowded.  There are projects such as Cartopy supports plotting using Matplotlib, which Geoviews has been built on.  Ipyleaflet also allows plotting on tile sources, as well as offers some interactivity.
Plotly would be the last project to compare to GeoViews, and it provides some integration for geo support.

GeoViews is a component of the broader initiative to make it easier to deal with very different datasets in the pydata ecosystem.  Mainly it consists of two components: subclassed HoloViews elements with Cartopy projections, and operations to project different types of data.  There is also the data backend which enables GeoViews to natively understand the data which includes libraries like Xarray, Iris, Geopandas and so on.  Matplotlib forms the basis for the plotting and rendering components.  Bokeh support has been the focus most recently, and this component allows true interactivity, e.g. cross-filtering, drawing tools etc.

Before PyViz was a thing, there was a small team at Anaconda and in collaboration with MetOffice, the GeoViews project was started.  The MetOffice is the short name for the meteorological office which is a government department in the UK and conducts weather forecasting as well as other climatology research.  From that point on, Martin has taken on the maintenence.

Clients have always been a big support for this project moving forward.  More broadly speaking, the users have been fairly scattered, using it for personal projects.  Another big user group comes from other government agencies in the U.S. like the USGS., NASA, and the U.S. Army Core of Engineers.  We have also recently begun working with the PanGeo research project, which is a collaborative effort run by various geographic and oceanographic organizations who want to utilize cloud computing. So at this point, the PyViz team (mostly Phillip) funded through consulting projects with industry and government clients.  Right now this project is trying to become more welcoming, and the effort is to get more people to join the project and increase the diversity of the team and leadership. 


### Demo

[Basics of wrapping gridded/tabular/geometry data with projection](http://geoviews.org/user_guide/Projections.html)
[hvPlot as a simpler entry point](https://hvplot.pyviz.org/user_guide/Geographic_Data.html)
[Various examples and dashboards](http://geoviews.org/gallery/index.html
[Glacier Crossfilter App](https://anaconda.org/philippjfr/oggm_glacier-raw/notebook)
[EarthSim demos, e.g. drawing tools etc.](http://earthsim.pyviz.org/topics/GrabCut.html)

### Roadmap

You can view the current roadmap [here](https://www.quansight.com/projects)

1. **Overall Vision:**  This project is aiming to be an open-source, scalable, browser-based replacement for closed-source and native-GUI tools such as ArcGIS and QGIS.
The advantage of this approach is the flexibility, existing tools are very powerful but also monolithic and hard to extend, PyViz, of which GeoViews is one part, aims to provide flexibility to build the workflow that’s needed.  This workflow provides the opportunity to expirament, share, and discuss the application so that it can be produced according to that collaboration.  The vision here has been the genneral plan for a while because the model allows experimentation and then deployment in a fast easy way.  Rather than drive this process to come about, customers have affirmed that it works well.  There are lots of areas here where contributors could help us develop this project further, and some of these roadmap areas are great examples.


2. **Scalable Rasterization of Gridded Data:**  In the remote sensor community, specifically satellite imagery, you tend to end up with very detailed grided datasets in the Gigapixel range.  Using these images and all the detail they provide can pose a challenge to researchers who want to fully utilize that information.  Currently, GeoViews supports rasterizing structured and unstructured meshes using Datashader, whether the shapes are rectalinear, curvilinear, or unstructured meshes.  The current implementation utilizes memory, which means it is not scalable to datasets larger than the user’s available memory.  The hope is to have sufficient support and funding to make a Dask backed rasterization of rectilinear, curvilinear and unstructured meshes.


3. **Improved integration with the Intake project:**  Intake ([which can be seen in a previous episode](https://www.youtube.com/watch?v=bwYldBhYNlw&t=1036s)) allows declaring data catalogs and already has some integration for PyViz plotting via hvplot.  This implementation would be another part of the solotion to the scalability issue with large remote datasets.
Another element if this is the intent to improve workflow for persisting custom plots to the intake catalog yaml.  Implementation of this feature would make it trivial to work with large remote datasets.  One thing that could be really helpful here is if people can contribute use cases to help direct efforts.


4. **Integrating 3D Earth Rendering into GeoViews:**  One of the core design ideas behind HoloViews was that you could extend it with customer renderers, currently the efforts have been focused on Bokeh and Matplotlib but you can extend it with any renderer you want. Some clients/users have expressed interest in a 3D renderer based on either CesiumJS and/or Deck.GL.  Doing this would give the user a 3D gloabe to work with, and represents an area of opportunity for someone to help with development. CesiumJS prototype [here](https://anaconda.org/philippjfr/cesiumjs_backend/notebook).



5. **Improved integration with other tools:**  Intake has already been mentioned and how it is planned to be integrated, but datashader already provides a number of common GIS operations such as computing NDVI, hillshading etc.  The hope is to extend the functional operations that can be done to include examples such as: zonal statistics, Hydrology tools (flow accumulation, flow direction etc.), and Euclidean distance based on input geometry.  



6. **Better Support for Remote Datasets and Remote Computation:**  Currently support is provided for Dask with Dask data frames and arrays.  By keeping everything in Dask it can handle all the memory and improve other remote/out-of-core computations including parallelizing and projecting data so that the user can deal with datasets which are larger than the available memory.  This would not only include rasterization but would include other operations such as projecting data.


### Viewer Questions

**Q.** Would a scenario of this in an enterprise be: A company has lots of databases in teradata/hadoop/ - for intake to be useful one would want to have some curated datasets that would be exported to a set of files that are(refreshed at some interval) and stored somewhere, then build catalogs off those?

**A.**  Yes, this is a reasonable thing that you might want to do, but you could just build a driver that will directly talk to these data services themselves and reflect data sources that they already expose.  Both of these are independently useful.  At the moment Intake has a concept of caching, which is to download files locally (whether that be your machine or a server) and then Intake will use the cached version until it expires and refreshes.  The further development we would like to do on this would be that it would not just cache the file, but would also cache the quiry.

---

**Q.** Is it possible to import other raster formats into geoviews/holoviews other than the netCDF files shown in the tutorials?

**A.**   In general, we don’t try to do the ingesting ourselves, we natively understand the in memory or out of core formats including Xarray.  Xarray has a backend which it can load from including netCDF, grib, geotiff, etc. so anything can be ingested from Xarray.  The same goes for the iris project and otherwise fall back to NumPy/Dask arrays and you will be guaranteed to display it.

---

**Q.** Is there any direct interaction with geopandas. for example is geoviews aware of projection system being used in geopandas?

**A.**  This is actually kind of new to me, I did not know that GeoPandas represented projections.  I would encourage the asker to file an issue with GeoViews.  It would be helpful to know what support would be wanted out of that, because as long as it is straightforward enough to convert these coordinate systems to Cartopy coordinate systems then it should be easy to load them in and convert them.

---

**Q.** So Google came out with Google moon and Google Mars and since you have this geographical mapping capability, has anyone suggested or attempted to use GeoViews for maps of other celestial bodies?

**A.**  There have been some people trying out things like this in the Astropy community, which is a big project used by the astronomy comunity.  This group has played around with HoloViews a little bit, but we have not yet tackled those types of coordinate systems.  It would be really nice if Cartopy could be extended to support those because then we would just get that for free.  If anyone is interested in this area of development, then that would certainly be a neat addition and a great opportunity for contribution.

### Footnotes & Links

* User Guide [here](http://geo.holoviews.org/user_guide/index.html)
* [GeoViews Website](http://geo.holoviews.org/)
* [GitHub page](https://github.com/pyviz/geoviews)
