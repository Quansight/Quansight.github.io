---
layout: post
title: Episode 6 - Intake - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/bwYldBhYNlw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [Intake](https://intake.readthedocs.io/en/latest/index.html)

* **Host:** David Charboneau
* **Co-Host:** Tony Fast
* **Guest:** Martin Durant, an Open Source developer at Anaconda working on work on Dask, Intake and data format/storage backends and currently based in Toronto, Canada.

### Project Overview

Intake has been around as an idea at Anaconda since around the beginning of 2018. The idea to make it had already existed before that, and there was even some structure in place, but a small team has now been assembled to bring it to fruition.  It was only released in August, and that is when the conversation about it came about.  With this in mind, there is still a great deal more user experience that will need to be had so that the project can be further directed according to the needs of users.  Intake download totals on Anaconda.org are currently at 4,100 so this project is still in its early days!

This project is intended to fill a hole in the data flow for people programming in Python. For many people, they will not even be aware that they had this need to fill, but the hope is that as it becomes better known then people will realize the utility.  Intake helps people with getting to their data, knowing which data is which, and how to access that data.  The hope is to save people time and allow them to more easily disseminate their data.  Projects like Blaze sort of addressed this, however at this point it is many years old.  Odo kind of addresses this as well, but each of these projects just represented parts of the puzzle, and thus Intake is an attempt to pull them all together under one framework.

While many libraries out there have various ways of loading data, (Pandas is a popular example for data scientists) there are so many different types of data out there that it is difficult to know what to load with which package and what set of arguments to use.  Further, there is no great streamlined way to critically catalog those data sets in the Python ecosystem at the moment.

Intake is about integrating with all the many packages out there that are capable of loading data.  It is then capable of accessing them all from one unified API, and that is the most crucial element.  There are many projects out there that do some piece of this puzzle, and in particular, there are even some that attempt to do some sort of catalog one example might be a traditional database system with a set of tables.  There are additionally a number of online solutions as well where you can host your data with some provider and then they can return a list of data sets that you have.  Intake tries to just be a little more generic and take a thin layer over all of these different things to bring them together and give them a consistent feel.  It is a way for the person creating these assets to get them to the user without the user having to learn everything about the different ways they might access their data.  It is about all of these different actors coming together in the data system together and agreeing on a contract of how to describe data.  With this system, the user no longer has to research, but it is also easier on the people who are putting data in place.  The larger the organization, the more that these things will be pain points.

To a great extent, Intake is not built on other technologies, it interacts with some of the file systems specific to Dask.  Dask has a particular way of talking with cloud file systems, so Intake piggybacks off of some stuff like that to be able to access data in different places.  Intake is standalone so if you do not know about Dask then you do not need to use it.  Much of this functionality is dataset specific depending on what you want to load, so each dataset has its own dependency and for example, if you have a dataset in the .zar format then there is a good chance you have no idea what that is but Intake will natively call and load that data.

Since January Martin has been the only main developer on this project, but many people have helped out along the way.  By spreading the word, the hope is that people can use Intake and give their feedback since it is so new.  It covers a huge range of things with minimal code and so the real question is where do we go from here?  Rather than continue guessing, the best case scenario is now for users to contribute to the direction of this project.  One key way in which people can really help out and get involved is by helping to gather all those little bits of code for all the data types and the unique data resources out there.

### Demo

[Intake Binder Demo](https://mybinder.org/v2/gh/martindurant/intake-release-blog/master?filepath=data_scientist.ipynb)

Get started with Intake [here](https://www.anaconda.com/blog/developer-blog/intake-taking-the-pain-out-of-data-access/).


### Roadmap

You can view the current roadmap [here](https://intake.readthedocs.io/en/latest/roadmap.html)

1. **Road ahead:**  Intake aims to be a community of data-oriented pythoneers! These are items that might be in the future for Intake, however, with that in mind, the community is encouraged to make their opinions known too!

2. **Broaden the coverage of formats:**  Data-type drivers are easy to write, but still require some effort, and therefore reasonable impetus to get the work done. Conversations over the coming months can help determine the drivers that should be created by the Intake team, and those that might be contributed by the community.  Similarly, there are many third-party data services, some of which are paid and proprietary. Currently, SQLCatalog is the only example, and therefore reference of this, but Intake will become more universally useful when it can act as a bridge to several other systems.

3. **Integration with Apache Spark:**  The spark ecosystems and Intake will co-operate nicely! Firstly, Spark sources (i.e., named tables) will become standard data sources, so that the data can be streamed from Spark to a python process, and the data-sets referenced in a catalog as usual. These data-sets will necessarily be data-frame type, although an RDD-to-sequential method may also be possible.  Later, automatic streaming of data into Spark should be possible with a to_spark() method appearing on data-frame (and maybe sequence, later) type sources.

4. **Derived Data-sets:**  Often, we can conceive of a data-type as being a modified version of another data-type. For example, the “csv” plugin produced data-frames from a set of files in the CSV format, while another plugin takes data-frames with a particular set of fields as inputs, and produces new data-frames based on some model predictions.  Rather than allow a general pipeline with arbitrary code specified in catalogs, we aim to allow the creation of arbitrary plugins where the inputs are the outputs of other data sources. This way, the logic stays in the code of the plugin, which can be distributed as Python/Conda packages as usual, but a path is in place to generate “second-order” data products. Naturally, such derived plugins ought to be thorough about describing the process in the metadata of the resultant data-source.

### Viewer Questions

**Q.** Would a scenario of this in an enterprise be: A company has lots of databases in teradata/hadoop/ - for intake to be useful one would want to have some curated datasets that would be exported to a set of files that are(refreshed at some interval) and stored somewhere, then build catalogs off those?

**A.**  Yes, this is a reasonable thing that you might want to do, but you could just build a driver that will directly talk to these data services themselves and reflect data sources that they already expose.  Both of these are independently useful.  At the moment Intake has a concept of caching, which is to download files locally (whether that be your machine or a server) and then Intake will use the cached version until it expires and refreshes.  The further development we would like to do on this would be that it would not just cache the file, but would also cache the quiry.

---

**Q.** How hard is it to add a new "kind" of container to the intake universe (i.e. xarray, dataframe, numpy, dask, pyspark, or future container concepts)?

**A.**   I would invite people to look at the code, and I claim that it’s not complicated.  Obviously, I would know the code base better than most people, but looking at the number of lines of code there is really not much.  The internal containers are based on a plugin system just like the drivers.  The intent is that this is all approachable.

---

**Q.** How are you managing the growth or addition of new plugins?  If somone wanted to come along and create a new plugin, where would that live and what are some of the development guidelines that someone would need to follow?

**A.**  The easiest thing to do would be to go to one of the repositories in the plugins directory (found in the footnotes).  All you need to do is select one of the plugins and copy it, at that point, you will have the framework in place for doing all of the things that you need.  These packages don’t need to live within the Intake repository, they can be their own independent thing, which means that developers can choose their own cadence and upload it to Anaconda.org if they wish.  So long as it depends on Intake, it should work.

---

**Q.** Do you have any examples of companies or communities using intake to create catalogs for their use?

**A.**  The best example at the moment would probably be [Pangeo](https://pangeo.io/).  They have a [website which is rendered from their catalog](http://pangeo.io/catalog.html).  The neat thing about this is the flexibility that they show, they took a simple spec and were able to gennerate a really neat view.  I should mention that there are some subtleties here which should probably be specified in the metadata of the catalog.

### Footnotes & Links

* A plugin directory is found [here](https://intake.readthedocs.io/en/latest/roadmap.html)
* [Intake Website](https://intake.readthedocs.io/en/latest/index.html)
* [GitHub page](https://github.com/ContinuumIO/intake)
* Install line: `conda install -c intake intake`
