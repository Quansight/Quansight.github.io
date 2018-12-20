---
layout: post
title: Episode 9 - Datashader - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=AE79jGEINqo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [Datashader](http://datashader.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Jim Bednar, leads the PyViz development team at Anaconda, Inc., and is based in Austin, Texas.

### Project Overview

Datashader is a graphics pipeline system for creating meaningful representations of large datasets quickly and flexibly.  Current;y it has 1464 stars on Github and about 2,300 downloads/month across PyPI and conda.

In a way this project began with conventional plotting techniques developed over the past few centuries of scientific research work as we can see with early scientific journals displaying reutamentary charts.  These old methods worked very well for small datasets, but as more data was added they became less and less practical to use.  With traditional plotting you will eventually reach a point at which you add so many points that you begin to overwrite the points which you previously plotted.  We now find ourselves in a world which is awash with data, and those techniques don’t perform well with large datasets.  Often times these excessively large datasets result in a complete misrepresentation of the actual properties of the data.  It would make far more sense that your analysis and conclusions should become more accurate as you are able to obtain more data, but so far that has just not been accomplished with traditional plotting systems.  Datashader was born from this concept, and built on the theoretical premise of having infinite data.

Under the assumption that you have a large dataset, regardless of how large as long as Dask can handle it, Datashader can take the datasets and turn them into an image (basically a 2D histogram). This image can then be embedded in a plot that accurately represents the data’s distribution, without requiring trial-and-error tweaking.  The end result is something that looks like a plot, but which far exceeds the limits of a plot.  Datashader has this capability without the risk of crashing or errors that you would normally run into with other plotters when trying to load large datasets.  Another convenience is that Datashader does not require the user to input parameters.  By default it will simply take the data and try to render it as faithfully as possible on the screen without knowing what it is.

At the same time that Datashader was being developed, the vaex project was being developed independently.  When given point data, this alternative project does essentially the same thing as Datashader.  The point of divergence is that vaex offers 3D aggregations where as datashader works with many different types of data like points, grids, lines, meshes, and rasters.  There are also a few proprietary softwares in this space as well, one is OmniSci, formerly MapD, which is a GPU-based system and Nanocubes which takes a slice and dice approach.
 
Datashader can use Pandas, dataframes, or a Dask dataframe and is a pure Python program.  Furthermore it has been just in time compiled with the Numba system and loops into very fast vectorized code. Optionally, you can use Dask for distributed and out of core computation as well.  This configuration allows it to handle essentially unlimited dataset sizes which have been tested up to billions of points on a laptop, and trillions on a cluster or HPC system.  Just as a note, while Datashader does not assume Dask, it is able to use Dask. 

Perhaps about five years ago, there was a research project from XDATA/DARPA which was designed to push the envelope on what could be done with understanding data.  At this time there were several different collaborators which all started to have meetings about this. Anaconda, or Continuum Analytics, was a partner for this project and the idea for Datashader came out of that.  The question was asked, “What if we had infinite data, how would we make it displayable?”  Based upon these questions, some prototypes were created in Java, and some other contexts.  At this stage the main contribution was run by Peter Wang and Joseph Cottam from Indiana University.  Once Jim came on board, they authorized him to spend some time working on and developing this project.  Most of the original code was written by Jim Christ, and the rest came from Jim Bednar.  Now the project is composed of contributions from about 20 people, this is partially due to the fact that every time Datashader is used in another project a new person joins for a while, contributes a bunch of stuff, and then moves on.  This process has been both beneficial, and a little bit of a drawback.  So far, most of the big contributors have been Anaconda employees, so it is completely open source but almost all of the work is funded.  Many people will use it, but then they post some pictures and that is about it, there is a lack of user involvement in the development process.  People are far more likely to write code around it at the moment, rather than contribute to it.  It is currently perfect for the average user, but the point at which the software is pushed, usually ends up outside of the normal user experience.  This has resulted in most people not noticing the areas of improvement to be made, unless they are a large company trying to use the software.

Currently the PyViz team at Anaconda, Inc. maintains this project, with funding from a variety of client projects that use Datashader.  Many of the contributors to this project are from Anaconda, but not all.  There are currently about 7 outside contributors.  The users are a different story and in general could be described as anyone with big data.  Some of the typical users are corporations and government organizations that produce their own data.  There is another contingent of people who just take existing datasets and enjoy using datashader to see what comes out of it.  Usually examples are representations of geographic data because that’s easy for people to appreciate and understand, but it works for any data, and people have used it for things such as shipping routes, airplane flights, grocery store shopping, and even all objects in the universe.


### Demo

[Interactivity Notebook](http://datashader.org/getting_started/3_Interactivity.html)
[Demo at timestamp 14:19](https://www.youtube.com/watch?v=AE79jGEINqo)
[Github Repository](https://github.com/pyviz/datashader/tree/master/examples)
[Github examples](https://github.com/pyviz/datashader/tree/master/examples)

### Roadmap

You can view the current roadmap [here](https://www.quansight.com/projects)

1. **Adding more data types that can be datashaded:**  Many of the current examples are of aggregated point data, and because of the availability of GPS data people can easily use it in Datashader.  Other data forms such as linear data can also be displayed by Datashader in such a way that could only be represented with numerical statistics in the past.  This now allows you to understand data which has hundreds of thousands of curves in a way that was never previously possible.  Datashader can also use very large meshes and rasters, but beyond these capabilities are some limitations.  The biggest area of improvement here would be in adding support for large polygons.  Arbitrary polygons are often used in geospatial mapping for things like government borders, and currently this is not implemented.  In theory anything that can be visualized can be rendered using Datashader, but now it is just about adding to the list.

2. **Better integration with plotting libraries:**  We were at a point where Bokeh was controlling the interactive user experience and Datashader was doing the rendering.  At this point there were quite a lot of holes in the interface which caused issues with things like importing.  One example of this was that in some cases you could easily get a color bar and see what was going on, but not if you chose histogram equalization.  The problem was that Datashader was just rendering in a completely different way then a plot rendered in other software.  Since that time there has been a lot of work trying to rebuild this from the ground up, however there is still a lot of work to be done.  With the Plotly interface being brand new, there is a lot of opportunity for community contributions.


3. **Improve speed and memory performance:**  With the way Datashader development has gone, there has never been a monitoring system set up to keep track of the memory usage when new features are added.  Every once in a while a bottleneck is discovered, but there is no built in system to help detect those.  While the code base itself remains mostly unchanged, each of these additions creates the potential for a reduction in optimization.  This would more or less just be a regression oriented test suite.  


4. **HollowViews allow users to set criteria based on size:**  Right now if you are a holoviews user and you have some flaw and want to load 50X more data into the plot, then it should work fine when you type datashade.  The problem arises when you have to go back and forth a lot with bigger and smaller datasets, because it is either always datashaded, or you you keep the smaller dataset functionality.  If you try to go back and forth it will crash your browser.  The hope here is to add the capability for Bokeh to be aware of the dataset size.  This update would provide some parameters so that it would not try to process datasets above a certain size in the browser, but rather send those larger sets to Datashader and visa versa.



5. **Isolated point case:**  Datashader works perfectly when you have huge sets of data or an infinite amount of data, but when you look closely at the rendering there may be parts which are sparse.  Right now each line or point occupies only one pixel at most, so it becomes difficult to see these sparse areas in a high fidelity way.  There are currently solutions implemented to address this, but they could be a lot better.  There is no funding going toward this at the moment, so this would be a perfect place to help contribute time or funding so that Datashader can be just that much closer to its potential.


### Viewer Questions

**Q.** How datashader technology compares to technology used in Google Maps visualization?

**A.** So Google Maps, specifically tile based map servers, is interesting because you can use Datashader to grade such things.  Most people may not know, but when you go to Google Map and try to zoom from all of America down to a single city block, it creates little map tiles in 16X16 blocks of images.  Each of these tiles is pre-rendered and all you are doing is pulling them down from the web server.  In essence it creates the illusion of zooming, but there is no live data involved.  Everything is pre-rendered at different resolutions, and at the lowest level there is just a ridiculous number of tiles.  For Datashader, everything is live and processed on the local hardware.  The only thing which exists on the map is what has been rendered just for me in that instance.  So what you could do it use Datashader to render the tiles which can then be sent to people if you have a large enough server to store all the renderings.  The tradeoff between these two methods comes down to whether you have more hard drive space or more computing power.

---

**Q.** Have you tried AirSpeed Velocity for performance? It can run all commits on your hardware (may take time, but it does it), and you can have multiple benchmarks?

**A.**  The answer is yes, I love ASV it is a great tool.  We actually can’t run it over all of our commits, because we don’t have enough power.  Just running a test suit once is very expensive because we are working with big data performance, not just performance in general.  The nuance here is that we have to run a big test and then go back to find the problems across many commits. 

---

**Q.** Jared Thompson: Can a legend be added to show the color with the trip density?

**A.** Yes, under certain circumstances.  If you are in Bokeh, and you choose linear or logarithmic wrapping from your value to a color then you can easily have a legend.  If you are using histogram equalization, which is a parameter free no barometric way to map color, then no but we are working on that.

---

**Q.** Have you thought of using KD Trees?

**A.** The answer of course is yes KD Trees and Quad Trees for geographically or data space subdividing the dataset and that is our planned approach.  We have some funding for trying it, but I don’t know if it will be enough, but that will probably depend on how well it works.  The funding is just there to start but maybe not finish.

### Footnotes & Links

* User Introduction [here](http://datashader.org/getting_started/index.html)
* [Datashader Website](http://datashader.org/#)
* [GitHub page](https://github.com/pyviz/datashader)
* [Gitter page](https://gitter.im/ioam/holoviews)
