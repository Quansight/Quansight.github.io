---
layout: post
title: Episode 4 - PyViz - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/hOIHmi7qxfM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [PyViz](http://pyviz.org/).

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Jim Bednar, leader of the PyViz open source team at Anaconda and currently based in Austin, Texas

### Project Overview

PyViz was started because Python has many, many tools for data visualization, yet users still find it very hard to get their work done, and most are just bewildered by all the different options available. The result of this is that people choose whatever their buddy is using, tying their code into knots trying to make that library solve their specific problems. Or they give up and use a non-Python tool.  PyViz tries to make sense of all this, guiding users to the right tools for their problems.  The focus is on making it easy to use big or small data, in web browsers, in and out of notebooks, visualized faithfully and accurately.

PyViz provides an environment where many viz tools can easily be installed.
It gives an overview and tutorial that cuts across multiple projects so that you can see how to use them individually and put them together for real tasks helping to make each project work well with the others where appropriate.  We also add higher-level tools that make others easier to use or more powerful and show users how to handle even very large datasets in a web browser.

As far as alternatives go, one can always use individual Python viz tools, each maintained by its own separate developer.  Some of these build on other tools (e.g. Seaborn on top of Matplotlib), but there are no other initiatives that try to make sense of a big set of different projects.

PyViz is primarily built upon the existing Bokeh, Matplotlib, Plotly, and Cartopy libraries, and works with dozens more viz and data-handling libraries.  PyViz itself doesn’t have any code; it’s a set of people, a project, an environment, a website, tutorials, examples, a GitHub organization, and a chat room, all helping to make sense of Python viz.

Jim started the project with his group at Anaconda, based on their work with many different consulting clients. These clients wanted a coherent, comprehensive way to solve their data exploration and visualization problems, particularly for large datasets, and as a group we wanted something that cut across all client projects and OSS projects as the go-to way to tell people how to get things done. Up to that point, everything else was specific to individual clients or to a specific OSS library.

PyViz is maintained by a somewhat rotating cast of 5-7 full-time Anaconda employees. In turn, most of the funding for these employees come from industry and government consulting clients for specific projects.  Most of the work of the PyViz team is spent on the individual projects involved; only a small fraction is spent on pyviz.org itself, but we always keep how the projects fit together in mind as we work.

Users come from a huge range of industry, academic, and government positions, across many research areas and job descriptions.  So far, the main library authors involved have been the maintainers of Bokeh, HoloViews, GeoViews, and Datashader.  We’re always happy to have more perspectives and help improving integration between projects.  The underlying projects have many external contributors, but just a handful so far for PyViz itself.

### Demo

Follow instructions at pyviz.org to install, then:
[Interact:](https://anaconda.org/jbednar/datashadercliffordinteract): Turn a Jupyter notebook into a deployable app with one line of code.
[Attractors:](https://anaconda.org/jbednar/datashaderattractors) Build a complex dashboard directly in a notebook and go back and forth.
[Gapminders:](https://anaconda.org/jbednar/panel_gapminders) Use Matplotlib, Plotly, bokeh, Altair, R ggplot2 -- whatever you like!
[hvPlot:](https://hvplot.pyviz.org/) Interactive Pandas plots for free!
[See PyViz.org](http://PyViz.org) for much, much more.


### Roadmap Items

You can find the [full roadmap here](www.quansight.com/projects).  Some examples:

1. **Better integration with other tools:**  PyViz doesn’t yet cover everything in Python viz; e.g. there is relatively little integration of 3D viz libraries, and few tools that support desktop GUIs.  We’d love to work with people interested in expanding that sort of functionality, to make PyViz truly inclusive of the range of viz tools available for Python.

2. **Better dashboard look-and-feel support:**  Panel makes it simple to build even complex dashboards using almost any plotting library, but it can be difficult to control the look and feel or to match the style of the non-Python dashboarding tools it can replace.  We don’t have funding to work on that, but it would be fabulous to be able to try to make it easier to make dashboards that are visually competitive with some of these less-flexible or harder to use alternatives, so that people can stay in Python and keep being productive while generating output that looks like what the rest of the organization expects.

3. **Extensive documentation about deployment:**  The PyViz tools can export to standalone HTML documents or PNGs for sharing in many cases.  However, in other cases you need a live Python server running, e.g. for data too big to stuff into one web page.  Anaconda offers a paid product for deploying to such a server inside a firewalled agency or enterprise, but there are also many options for making public deployments, such as Heroku, Google Cloud, AWS, and MyBinder.  Our users have reported that the tools work with all these variants, but documenting and testing these possibilities takes time, effort, and expertise, and we’d greatly appreciate outside help in documenting how to work with these diverse systems and how to decide between them.

4. **GUI-based plot creation:**  Many of the PyViz tools are fully declarative, which makes it very straightforward to build GUI-based ways of composing and configuring them.  Current tools all require Python knowledge, but it should be feasible to build fully graphical approaches to building visualizations and dashboards that can help broaden the audience for these tools.  Unlike existing commercial GUI dashboarding tools, a PyViz tool wouldn’t be a dead end -- whenever users reach the limits of what is available in the GUI, they can work with colleagues or consultants to bring in additional functionality from the PyViz ecosystem immediately, with relatively little effort to add such customizations.  We’d love to work with people to build such a user-friendly tool on top of the solid foundation provided by PyViz.

### Viewer Questions

**Q.** Note - I have not used PyViz heavily as I mostly use Altair, how stable is the syntax one sees on the pyviz.org site. For example, I see lost of cell magics with opts and others use it as a variable etc.. (again I have not used this library heavily - just wondering how much churn is going on)

**A.** So for the magics question we found them to be helpful for our own purposes because they tab complete in our Jupyter Notebook.  On balance we decided they were more confusion than they were worth, so we are gradually trying to remove them from our docs, adding tab completion in other ways.  We simply have a lot of material and it takes a long time to remove things, or they would be gone already!  At this point there is no reason to use cell magics because there is a pure Python equivalent for everything, and we will eventually steer all users to just do it that way to avoid confusion, but for now you will see both ways illustrated. To answer the other question, the PyViz ecosystem includes a large set of tools, some of which are very well established, and others recently developed to address gaps.  The Matplotlib and Param support is not moving very quickly because they are already very solid and stable (more than 10 years old), while the Bokeh and HoloViews projects both include a mix of long-supported features (3-5 years or more) and more recently added functionality (0-24 months) that is still in flux. Panel is brand new and not even fully released yet as of October 2018, but it is a straightforward layer on top of projects that have been around for a very long time; we simply realized that we could now provide dashboarding support in a very general way.  Datashadar’s API changes very slowly and just kind of sits there and works, despite not being as old as Matplotlib and Param. As you can see, the rate of innovation varies a lot per project; some parts are the bedrock on which everything else builds, and others are seeing rapid changes as we work to provide higher-level solutions for common problems.

---

**Q.** If I'm the author of a visualization tool, how would I make sure my tool can be integrated into the PyViz stack. What are the hooks for outside contributors to participate?

**A.** The first thing to consider is that Panel will probably already support it, so if you just put up a Panel and you use Panel.Row with it, then you can see what happens.  The worst case will be that a text-only representation of the object will be displayed, but if your object can display HTML, PNG, SVG, LaTeX, or any other typical visual representation, then it should just work.  If it does not work already, then you can add those methods to your object, letting it display itself in both Jupyter and in Panel.  This process does not require any changes to PyViz or Panel, but it will extend their capabilities in a natural way.  For deeper integration like making a new HoloViews backend, HoloViews currently supports Matplotlib, Bokeh, and the 3D aspects of Plotly, but other backends have been prototyped. If you want to consider that type of project, please get in touch with the PyViz authors for advice and support.

---

**Q.** Does Param generate Jupyter widgets?

**A.** Yes, Param can generate Jupyter widgets, via a package called ParamNB, which provides ipywigets-based controls for Param's objects, in a Jupyter notebook.  The same objects used with Panel will generate Bokeh widgets instead, which is what we recommend over the ipywidgets support because then you can easily move between notebooks and separate servers without changing any code and with the same look and feel of the widgets.

---

**Q.** Is PyViz integrated with IPython widgets? How does an IPython widget user get started with PyViz?

**A.** PyViz tools in general can be used with or without ipywidgets, but where this issue comes up most directly is with Panel. Panel is a direct competitor to both ipywidgets and to Dash. Interestingly, those two other projects don't compete directly with each other, because Dash focuses on standalone servers and ipywidgets currently focuses primarily on Jupyter notebooks, apart from some tentative initiatives to deploy ipywidgets outside the notebook. Panel is currently the only way to support both contexts equally well, and thus allows switching back and forth between notebook and non-notebook contexts as needed, which we argue is crucial for supporting the full workflow of data scientists and developers as they move from exploration to production and back.

---

**Q.** How easy is it to connect PyViz servables with JupyterLab plugins? Also, how do you make your webpages (pyviz.org and panel.pyviz.org)?

**A.** There are actually three contexts supported (JupyterLab, classic Jupyter, and separate servers), and Panel works the same in all three. We provide a JupyterLab extension that provides bi-directional communication, and similar mechanisms for the other contexts.  The key technical problem is ensuring that you can move data and events back and forth between Python and JavaScript, and we have ensured that such mechanisms are available in each case so that everything works.

---

**Q.** What is the best way for those who are new to PyViz to get started?

**A.** Go to [pyviz.org](http://pyviz.org) and follow the instructions.

### Footnotes & Links

* You can find [the current PyViz roadmap here.](https://www.quansight.com/projects)
* [PyViz Website](http://pyviz.org/)
* [GitHub page](https://github.com/pyviz/pyviz)

