---
layout: post
title: Episode 4 - PyViz - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/hOIHmi7qxfM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [PyViz](http://pyviz.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Jim Bednar, leader of the open source team at Anaconda and currently based in Austin, Texas

### Project Overview

PyViz was started because Python has many, many tools for data visualization, yet users still find it very hard to get their work done, and most are just bewildered by all the different options available. The result of this is that people choose whatever their buddy is using, tying their code into knots trying to make that library solve their specific problems. Or they give up and use a non-Python tool.  PyViz tries to make sense of all this, guiding users to the right tools for their problems.  The focus is on big and small data, in web browsers, in and out of notebooks, visualized faithfully and accurately.

PyViz provides an environment where many viz tools can easily be installed.
It gives an overview and tutorial that cuts across multiple projects so that you can see how to use them individually and put them together for real tasks helping to make each project work well with the others where appropriate.  We also add higher-level tools that make others easier to use or more powerful and show users how to handle even very large datasets in a web browser tab.

As far as alternatives go, each Python viz tool is maintained by its own separate developer.  There are some that build on other tools (e.g. Seaborn on top of Matplotlib), but there are no other initiatives that try to make sense of a big set of different projects.

PyViz is primarily built upon existing Bokeh, Matplotlib, Plotly, and Cartopy libraries, and works with dozens more viz and data-handling libraries.  PyViz itself doesn’t have any code; it’s a set of people, a project, an environment, a website, tutorials, examples, a GitHub organization, a chat room.

Jim started the project with his group at Anaconda, based on their work with many different consulting clients. These clients wanted a more coherent, comprehensive way to solve their data exploration and visualization problems, particularly for large datasets, and wanted something that cut across all client projects and OSS projects as the go-to way to tell people how to get things done. Everything else was specific to clients or to a specific OSS library.

PyViz is maintained by a somewhat rotating cast of 5-7 full-time Anaconda employees. In turn, most of the funding for these employees come from industry and government consulting clients for specific projects.  Most of the work of the PyViz team is spent on the individual projects involved; only a small fraction is spent on pyviz.org itself.

Users come from a huge range of industry, academic, and government positions, across many research areas and job descriptions.  So far, the main library authors involved have been the maintainers of Bokeh, HoloViews, GeoViews, and Datashader.  We’re always happy to have more perspectives and help improving integration between projects.  The underlying projects have many external contributors, but just a handful so far for PyViz itself.

### Demo

Follow instructions at pyviz.org to install, then:
[Interact:](https://anaconda.org/jbednar/datashadercliffordinteract): Turn a Jupyter notebook into a deployable app with one line of code
[Attractors:](https://anaconda.org/jbednar/datashaderattractors) Build a complex dashboard directly in a notebook and go back and forth
[Gapminders:](https://anaconda.org/jbednar/panel_gapminders) Use Matplotlib, Plotly, bokeh, Altair, R ggplot2 -- whatever you like!
[hvPlot:](https://hvplot.pyviz.org/) Interactive Pandas plots for free!
[See PyViz.org](PyViz.org) for much, much more.


### Roadmap Items

You can find the [roadmap here](www.quansight.com/projects)

1. **Better integration with other tools:**  PyViz doesn’t yet cover everything in Python viz; e.g. there is relatively little integration of 3D viz libraries, and few tools that support desktop GUIs.  We’d love to work with people interested in expanding that sort of functionality, to make PyViz truly inclusive.

2. **Better dashboard look-and-feel support:**  Panel makes it simple to build even complex dashboards using almost any plotting library, but it can be difficult to control the look and feel or to match the style of the non-Python dashboarding tools it can replace.  We don’t have funding to work on that, but it would be fabulous to be able to try to make it easier to make dashboards that are visually competitive with some of these less-flexible or harder to use alternatives, so that people can stay in Python and keep being productive while generating output that looks like what the rest of the organization expects.

3. **Extensive documentation about deployment:**  The PyViz tools can export to HTML documents or PNGs for sharing, but in other cases, you need a live Python server running, e.g. for data too big to stuff into one web page.  Anaconda offers a paid product for deploying to such a server inside a firewalled agency or enterprise, but there are also many options for making public deployments, such as Heroku, Google Cloud, AWS, and MyBinder.  Our users have reported that the tools work with all these variants, but documenting and testing these possibilities takes time and effort, and we’d greatly appreciate help in documenting how to work with these diverse systems and how to decide between them.

4. **GUI-based plot creation:**  Many of the PyViz tools are fully declarative, which makes it very straightforward to build GUI-based ways of composing and configuring them.  Current tools all require Python knowledge, but it should be feasible to build fully graphical approaches to building visualizations and dashboards that can help broaden the audience for these tools.  Unlike existing commercial GUI dashboarding tools, a PyViz tool wouldn’t be a dead end -- whenever users reach the limits of what is available in the GUI, they can work with colleagues or consultants to bring in additional functionality from the PyViz ecosystem immediately.  We’d love to work with people to build such a user-friendly tool on top of the solid foundation provided by PyViz.

### Viewer Questions

**Q.** Note - I have not used PyViz heavily as I mostly use Altair, how stable is the syntax one sees on the pyviz.org site. For example, I see lost of cell magics with opts and others use it as a variable etc.. (again I have not used this library heavily - just wondering how much churn is going on)

**A.** So for the magics question we found them to be helpful for our own purposes because they tap complete in our Jupyter Notebook.  On balance we decided they were more confusion than they were worth so we were gradually trying to remove them.  We simply have a lot of material and it takes a long time to remove things so at this point there is no reason to use cell magics because there is a pure Python equivalent for everything.  We will eventually steer most users to just do it that way because the feedback indicated that magics was too confusing at first.  To answer the other question, the PyViz ecosystem is a broad community of recent immigrants and some people who have been with it a long time.  The matplotlib portion of it is not moving very quickly because it is already solid and stable, the Bokeh portion is less stable but quite comparably stable, HoloViews is quite stable, Pannel has not quite been released yet but it is based on projects that have been around for a very long time and we realized that we could do this in a very general way.  Datashadar’s API changes very slowly and just kind of sits there and works so it varies per project.

---

**Q.** If I'm the author of a visualization tool, how would I make sure my tool can be integrated into the PyViz stack. What are the hooks for outside contributors to participate?

**A.** The first thing is that Panel will probably already support it, so if you just put up a Panel and you use Panel.row then you will see what happens.  The worst case will be that a screen representation of the object is displayed, but if your object can display HTML, PNG, Latec or any such thing then it should just work.  If it does not work then you can add those methods to your object.  This process does not require any changes to PyViz or Panel.  For deeper things like HoloViews, it supports matplotlib, Bokeh, and the 3D aspects of Plotly.

---

**Q.** Does param generates Jupyter widgets?

**A.** It can through a package called paramMB, which is a param in the notebook.  When you use it with pannel it generates our Bokeh widgets.  With this approach, you can easily move between notebooks and not notebooks and just not worry about it.

---

**Q.** Is PyViz integrated with IPython widgets? How does an IPython widget user get started with PyViz.

**A.** If you specifically think about Panel, is it competitive with Dash because it is a way to lay out plots and have widgets on them, but since Dash does not work with a notebook then you would need to look at IPython widgets.  It allows you to lay things out and put widgets on them only in the notebook.  There are some initiatives to try to make them work outside the notebooks but PyViz is the only way to do both things at once today.

---

**Q.** How easy is it to connect PyViz servables with JupyterLab plugins? Also, how do you make your webpages (pyviz.org and panel.pyviz.org)

**A.** There are actually three contexts, Jupyter Lab, classic Jypiter, and the point servers and it works the same on all three of those.  There is a Jupyter Lab extension that provides two-dimensional communication.  So we have bi-directional communication, either the standalone server or classic Jupyter Notebook.  The key here is whether you can get things back and forth between Python and JavaScript.  We have created all the components at all the levels so everything works.

---

**Q.** What is the best way for those who are new to PyViz to get started?

**A.** Go to pyviz.org and follow the instructions.

### Footnotes & Links

* You can find [the current PyViz roadmap here.](https://www.quansight.com/projects)
* [PyViz Website](http://pyviz.org/)
* [GitHub page](https://github.com/pyviz/pyviz)

