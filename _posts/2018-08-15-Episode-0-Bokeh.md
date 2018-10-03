---
layout: post
title: Open Source Directions Episode 0: Bokeh
---```

### Introductions

This is the webinar that informs the community about what is going on with Open Source Python projects.  Our host is Anthony Scopatz and today the project being highlighted is Bokeh.

Tony Fast joins us as a community organizer and open source consultant.

Bryan Van de Ven is our second guest, and he works for Anaconda and was a developer of conda, but has since begun working on Bokeh.

### Project Overview

At the moment Bokeh is a popular module, it stands at upwards of 190,000 downloads per month, with 300 contributors, and around 7900 stars.  

_Anthony and Tony asked Bryan some questions and gained some background;_

1. Bokeh was started in 2012 with Peter Chang and the idea was that people wanted a rich visualization library that could work well with the web.  The intention was that it could be something like an updated version of chalco but more user friendly.  

2. The needs Bokeh fills have morphed over the years from data visualization, to a web application backed with real Python code.  

3. Some alternatives for this project would be like matplotlib, or altair, bqplot, but they don’t quite do the same thing.  Mostly similar packages are just for graphing specific things.  Holoviews and Altair would probably the best alternatives.  In general it is somewhat of a crowded space.

4. Bokeh was built upon the Javascript side and it was eventually ported to typescript. It was ported from coffeescript and the translation ended up being a major benefit.  With our current setup we are able to have combinations such as R-Bokeh, and we are willing to help anyone make an integration for other packages.  The main bulk of the code is intended to automatically validate and serialize. Bokeh is built on a html5 canvas, but mostly just operated on numpy.

5. For contributors, mainly it is just me and Mateo Poprosky at this point, however there have been many contributors like Sarah Bird, Claire Tang, Havoc Pennington from GTK and Gnome made the current version of the server, but as we mentioned there are 300 plus contributors on Github. Lately we have seen a good number of people who had repeat PRs.  Most of the maintenance is in the hands of Mataish and I but we like to see it more and more in the hands of the community.  

6. To better work with the community, we are making progress but we have not yet established normal meetings, and I would like to clear that hurtle this year or next year. We have had internal meetings and meetings with people at Anaconda, but not really anything in terms of contributors.

7. The absolute main focus right now is getting the 1.0 version released. We are shooting for late august, early september for the 1.0 release and are very committed to getting that out.  It is important right now to figure out what APIs we are going to keep. We are doing final layout changes and having to scale back a little.  I am also working on some testing infrastructure to help fix some data table regressions.  Mostly it is a top to bottom survey of the APIs to ensure everything is there. The heavy lifting is pretty much over and there should not be any more big PRs.

8. You mentioned the selenium test, we have a bunch of Javascript tests that we run in a node framework with Moca, but not in a browser because they are mostly unit tests.  It is difficult to test bokeh, because it is such a big testing surface. Another factor that makes it difficult is that it renders to an html5 canvas, but some of these are screenshot tests.  We don't do a hard fail on these tests yet, it is just a report for us to inspect after each build.  We may now be at the point where we can hard fail it though.  Definitely we are getting to the point where we can have the selenium tests for this again.  In particular we want to put emphasis on testing the datatable because it is an intersection between corner cases and use cases.
  
  ### Demo

_Tony showed off the bokeh binder found here:_ https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb
Website: Bokeh.pydata.org 
Github page: github.com/bokeh/bokeh

You can click the tutorial link to access the binder from the homepage.

I am not sure that I have a favorite demo, but one big thing last year was that they overhauled the categorical data to support nested categorical things.  One example is that it is now much simpler to create a bar charts, scatter plots, and other categorical charts.  Custom JS callbacks are all there as well to look at with the tutorials.  We are looking for recommendations for some other tutorials to include, or even just give recommendations for better documentation.  Getting feedback from the community is vital to making this better because it is easy to overlook simple things.  One example is that recently they added some new features to the hover tools, like displaying the name of the glyph in the tool.  

At this point we are not as concerned about going after further ipywidget integrations like Dash and Plotly for 1.0.  Right now it works pretty well in a notebook, but we have our own property system that we do not want to rip out, so we do not know how the serialization would work together with ipy widgets.  The ipywidgets wire protocol is not quite as rich because we have so many data types to serialize. This is a very post 1.0 question though.

### Roadmap Items

This is the meat of the webinar; the roadmaps section.  Let's go through each item and just explain a little more about what each one entails. 

1. Item 1 on the roadmap is integration with vega light and altair

  This would be for using the Altair API to generate a bokeh document and then dressing it up in a web application and add applications to it. Essentially the idea here is then to use the Altair API to generate a Bokeh output, but this would likely be post 1.0.

2. Next roadmap item is visual design improvements

  Since we are mostly engineers, we would like help from someone with GUI experience and graphic design so that they can be a contributor.  I think we just have not had a lot of input on the front end pieces to do the design work. How can we get Bokeh to integrate seamlessly into the kind of webapps people want to make.

  We need to know what a real front end dev would want.  If there are any front end dev designers out there, we would love them to contribute some time to help out with this.  This could be a thing that Bokeh would be looking for funding for as well.

3. Develope bokeh JS as a first class Javascript library

  The idea is that they could use Bokeh JS run directly with javascript so that those users without having Python.  The javascript tool set seems to keep changing and so we would want someone who is experienced with popular long lasting tools in the javascript world to help find ways to integrate Bokeh.  There is also other support work needed to help Bokeh JS become better documented, because it used to be just an implementation detail.  Much work also needs to yet be done for Bokeh JS to be useable by javascript developers.

4. Webgl front end, throughput, and what it means for Bokeh

  Anyone with openGL experience would be greatly beneficial to this roadmap item. There is a library that I am familiar with called regal that works as a higher level webgl library which needs some investigation.  Because of my lack of webgl experience, we may use regal as a higher level library that we could use to build out Bokeh support.  Whatever is done, having an opengl dev would greatly accelerate this process.  There is however currently some webgl support for a limited set of glyphs. The nice thing about this is that it pushes the capabilities of Bokeh up just a little bit higher. The goal is to be effective with a mid level data set around 100’s of thousands to a few million data points, and opengl can get us into that range.

Alright, thank you for helping us move through some of these.  Are there any other points to highlight that you are looking for help with, or working towards?

  There are some things that are already pretty much done: better theming in some of the layouts have been done, and the network has been done and is ongoing.  As far as things we probably need help with, I would say GIS work and contour maps (mostly about how to represent the data), improve the documentation accessibility in the sense that it needs to be arranged better, and we could use built in LaTeX / MathText support (would be nice if you could just use $ quotes).

### Viewer Questions

Now we are moving on to the user questions for Bryan.

Q. Is something like the Dasks interface on the roadmap?
  
  A. Not explicitly, but we did recently add a new test, we run the Dask test suite so now Dask has a Bokeh subset of tests. We would love to integrate more upstream test suites and we would love to add any test suites from Bokeh users for our downstream tests to ensure no one is having conflicts. Essentially we would love to help integrate Bokeh into whatever project people have, even if they are not on the roadmap.

Q. Bokeh is a Numfocus sponsored project?
  
  A. Yes, it has been on their mind for a long time, but for a while all the development happened by developers who were in Continuum or Anaconda. Eventually Numb Focus was able to get enough different people together to form the Bokeh committee and they had wanted to do that for a long time.

Q. Does Bokeh still need a seperate server for streaming data, or is it now integrated into the notebook?
  
  A. First, you can now run Bokeh server applications directly in the notebook. So you do not need to run the Bokeh server yourself, it will just attach itself to the Jupyter IO loop and run itself automatically.  Making a Bokeh server application in the notebook and running it will allow you to bypass the seperate server.  You can also use stream with push notebook because the function no longer has a separate protocol.

Thanks for watching, and you can find the current Bokeh roadmap here: www.quansight.com/projects 
