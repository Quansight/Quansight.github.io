---
layout: post
title: Episode 00 - jupyterlab-omnisci - Quansight Quicks
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/M_pQXYJebUo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Quansight Quicks, the 10 min short that provides demos for open source projects.
This episode, the project being highlighted is [jupyterlab-omnisci](https://github.com/Quansight/jupyterlab-omnisci)

* **Presented by:** Ian Rose: works for Quansight as a Software Developer and a core contributor to the scientific Python and Jupyter communities. He has a Ph.D. in Geophysics from UC Berkeley. He has expertise in the thermal, chemical, and rotational evolution of planetary bodies.

### Project Runthrough

In this video, Ian demonstrates some of the integrations that the team has been building between Omnisci databases and JupyterLab.  JupyterLab is a web application which provides an interactive programming environment through [Jupyter](https://jupyter.org/) notebooks and other activities in the Jupyter-related ecosystem.  

Upon launching the notebook there are various options available to the user.  These options allow you to select the type of activity and code environment you want.  The UI is set up with the standard menu bar, file browser, running settings, a command pallet, and a list of open tabs.  By accessing the file browser, a user can open up (as an example) a markdown preview of the readme.  You can also open a new terminal that can allow the user to keep track of their systems.  In this same way, you could also do something like open a new notebook.  In general, it just provides a nice environment for interactive programming.  

JupyterLab is designed from the ground up to be extremely extensible, and to that point, third parties can write extensions that add new things to the menus, command pallet, types of activities, and data types that the application can render.  It is meant to be something that anyone can customize to their liking.  Specifically, this modular design has allowed for customizations which work with Omnisci.  

One of the first changes is the addition of an option to the settings tab which allows the user to change the default Omisci connection.  This is helpful because it allows you to auto-populate areas that you may work with inside the notebook.  When it first starts up, a blank SQL editor text field appears and from here you can start building your SQL query.  As an example, you can compose a query using the pc contributions example dataset.  By having the computer wired up you can get smart completions, and easily make your high-performance data grids to display the executed commands.  Even with large datasets, it should be able to stand up no problem and you can scroll through it without lag.  

While that SQL editor is useful, it is also necessary to interact with the Omnisci database in Python.  This will allow for more general programming tasks.  Once a new notebook is open, the user can see the interface that Ian and the team have been working on which allows you to access the Omnisci backend.  The Ibis project has been key here because it provides a library that allows users to input more Pythonic code to execute queries in SQL.  By activating a convenience function in the command cloud, you can easily find the code for injecting Ibis into the Omnisci backend.  When this code is executed you should get a list of tables from either the example or whatever dataset you are using.  

To start off, you would just select one of the tables from the database.  Next, you would select some columns from that table by composing an expression.  If you take that expression and output it in a cell, it is not immediately evaluated but it gives you a visual representation of the query that is built. You can also output the SQL query that will be executed by the back end using ‘expression.compile’.  In order for the user to finally execute this, you can put ‘expression.execute’ and you should get your data back as a Pandas data frame.  

This is all well and good, but sometimes it is nice to have an escape hatch so that you can explore a little bit in raw SQL.  To that end, it is also possible to embed the SQL editor in a notebook environment.  To use this, start by importing a Python library, then use the SQL renderer editor made up of the connection and expression.  What this does is embeds the same SQL editor that was always used, but does so inside the notebook with that expression which was entered into the previous text field.  Because this is a live SQL editor, you can also add new columns table.  When you re-execute the query you should then have the new column that you added.  

This should provide a more Pythonic and interactive way for people to integrate with the Omnisci databases from their notebooks and Python code.  The last thing to mention is using a Vega spec from Omnisci.  Users can open the spec from a text editor, and it should be a Json-Vega specification.  There is also a custom renderer for this Json spec which connects to the Omnisci backend and actually executes that Vega.  By doing this you can execute the Vega and have a window that displays the data in a graphical form.  

Hopefully, these tools and integrations will make it easier for users to interact with the Omnisci ecosystem and allow Python users to have lightning fast analytics.

### Footnotes & Links

* [Demo on YouTube](https://www.youtube.com/watch?v=M_pQXYJebUo)
* [Omnisci webpage](https://www.omnisci.com/)
* [Ian’s Website](https://gitter.im/numba/numba)
* [JupyterLab website](https://jupyterlab.readthedocs.io/en/stable/#)
