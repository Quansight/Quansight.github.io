---
layout: post
title: Episode 0 - Bokeh - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/tUo-OQgIv_I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [Bokeh](https://bokeh.pydata.org).


* **Host:** Anthony Scopatz
* **Co-Host:** Tony Fast, Community organizer and open source consultant
* **Guest:** Bryan Van de Ven, employed by Anaconda and was a developer of conda,
  but has since begun working on Bokeh.

### Project Overview

Bokeh is a popular project with upwards of 190,000 downloads per month,
300 contributors, and around 7900 stars on GiHub.

Bokeh was started in 2012 with Peter Wang. The idea was that people wanted a
rich visualization library that could work well with the web.  The intention
was that it could be something like an updated version of Chaco but more user
friendly.

The needs that Bokeh fills have morphed over the years from data visualization,
to a web application backed by Python code.

Some alternatives for this project are matplotlib, altair, or bqplot. However,
none of these quite have the same feature set. Holoviews and Altair are probably
the closest alternatives. In general, visulatization is somewhat of a crowded space.

Initially, Bokeh was built on pure Javascript and it was eventually ported to
typescript. It was then ported to coffeescript and the translation ended up being
a major benefit. With our current setup we are able to have combinations such
as R-Bokeh, and we are willing to help anyone make an integration for other languages.
The main bulk of the code is intended to automatically validate and serialize.
Bokeh is built on a html5 canvas, but mostly just operated with numpy arrays.

The main contributors to the project are Bryan Van de Ven  and Mateo Poprosky at this point.
However there have been many contributors like Sarah Bird, Claire Tang, Havoc Pennington
from GTK and Gnome made the current version of the server, but as was mentioned there
are 300 plus contributors on Github. Lately, Bokeh has seen a good number of people who
had repeat PRs.  Most of the maintenance is in the hands of Mataish and Bryan but the project
would like to see it more and more in the hands of the community.

To better work with the community, Bokeh is making progress but we have not yet established
normal meetings, and Bryan would like to clear that hurtle this year or next year. Bokeh has
had internal meetings and meetings with people at Anaconda, but not really anything
in terms of contributors.

The absolute main focus right now is getting the 1.0 version released.
Bokeh is shooting for late August, early September for the 1.0 release and
is very committed to getting that out.  It is important right now to figure
out what APIs we are going to keep. We are doing final layout changes and
having to scale back a little.  Bryan is also working on some testing
infrastructure to help fix some data table regressions.  Mostly it is
a top to bottom survey of the APIs to ensure everything is there.
The heavy lifting is pretty much over and there should not be any more big PRs.

Bokeh has a bunch of Javascript tests that we run in a node framework with Moca,
but not in a browser because they are mostly unit tests.  It is difficult to
test Bokeh, because it is such a big testing surface. Another factor that makes
it difficult is that it renders to an html5 canvas, but some of these are
screenshot tests.  Bokeh does not do a hard fail on these tests yet, it is
just a report for us to inspect after each build.  The project may now be
at the point where they can hard fail it though. In particular, the project wants
to put emphasis on testing the datatable because it is an intersection between
corner cases and use cases.

### Demo

* [The Bokeh binder demo](https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb)
* [Bokeh Website](https://bokeh.pydata.org)
* [GitHub page](https://github.com/bokeh/bokeh)

Bryan is not sure that he has a favorite demo, but one big thing last year
that was overhauled was the categorical data to support nested categorical structures.
One example is that it is now much simpler to create a bar charts,
scatter plots, and other categorical charts.  Custom JS callbacks are all there
as well to look at with the tutorials.  Bokeh is looking for recommendations for
some other tutorials to include, or even just give recommendations for better documentation.
Getting feedback from the community is vital to making this better because it is
easy to overlook simple things.  One example is that recently Bokeh added some
new features to the hover tools, like displaying the name of the glyph in the tool.

At this point the project is not as concerned about going after further ipywidget
integrations like Dash and Plotly for 1.0.  Right now it works pretty well in a notebook,
but Bokeh has its our own property system that we do not want to rip out, so we do not
know how the serialization would work together with ipywidgets.  The ipywidgets wire
protocol is not quite as rich because we have so many data types to serialize.
This is a very post 1.0 question though.

### Roadmap Items

1. **Integration with vega-lite and altair:** This would be for using the Altair API to
   generate a Bokeh document and then dressing it up in a web application and add
   applications to it. Essentially the idea here is then to use the Altair API to
   generate a Bokeh output, but this would likely be post 1.0.

2. **Visual design improvements:** Since Bokeh contributors are mostly engineers, they would like help
   from someone with GUI experience and graphic design so that they can be a contributor.
   They just have not had a lot of input on the front end pieces to do the design work.
   How can Bokeh to integrate seamlessly into the kind of webapps people want to make?

   The project needs to know what a real front end dev would want.  If there are any
   front end dev designers out there, Bokeh would love them to contribute some time
   to help out with this. This could be a thing that Bokeh would be looking for funding for as well.

3. **Develop Bokeh JS as a first class Javascript library:** The idea is that
   developers could use Bokeh JS run directly with JavaScript so that those
   users without having Python.  The JavaScript tool set seems to keep changing
   and so we would want someone who is experienced with popular long lasting tools
   in the JavaScript world to help find ways to integrate Bokeh.  There is also other
   support work needed to help Bokeh JS become better documented, because it used to
   be just an implementation detail.  Much work also needs to yet be done for
   Bokeh JS to be useable by javascript developers.

4. **Webgl front end, throughput, and what it means for Bokeh:** Anyone with OpenGL
   experience would be greatly beneficial to this roadmap item. There is a library
   that Bryan is familiar with called regal that works as a higher level WebGL
   library which needs some investigation.  Because of Bryan's lack of WebGL experience,
   the project may use regal as a higher level library that we could use to build out
   Bokeh support.  Whatever is done, having an OpenGL dev would greatly accelerate
   this process.  There is however currently some WebGL support for a limited set
   of glyphs. The nice thing about this is that it pushes the capabilities of Bokeh
   up just a little bit higher. The goal is to be effective with a mid level data
   set around hundreds of thousands to a few million data points, and OpenGL can
   get us into that range.

### Viewer Questions

**Q.** Is something like the Dasks interface on the roadmap?

**A.** Not explicitly, but the project did recently add a new test. We would love
to integrate more upstream test suites and we would love to add any test suites
from Bokeh users for our downstream tests to ensure no one is having conflicts.
Essentially we would love to help integrate Bokeh into whatever project people
have, even if they are not on the roadmap.

---

Q. Is Bokeh a Numfocus sponsored project?

A. Yes, it has been on their mind for a long time, but for awhile all the development
happened by developers who were in Continuum or Anaconda. Eventually Numfocus was
able to get enough different people together to form the Bokeh committee and they
had wanted to do that for a long time.

---

Q. Does Bokeh still need a seperate server for streaming data, or is it now integrated into the notebook?

A. First, you can now run Bokeh server applications directly in the notebook. So you do not need
to run the Bokeh server yourself, it will just attach itself to the Jupyter IO loop and run
itself automatically.  Making a Bokeh server application in the notebook and running it will
allow you to bypass the seperate server.  You can also use stream with push notebook because
the function no longer has a separate protocol.

### Footnotes & Links

* You can find [the current Bokeh roadmap here.](www.quansight.com/projects)
* [The Bokeh binder demo](https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb)
* [Bokeh Website](https://bokeh.pydata.org)
* [GitHub page](https://github.com/bokeh/bokeh)
