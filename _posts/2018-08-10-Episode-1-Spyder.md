---
layout: post
title: Episode 1 - Spyder - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/vtLdH4VbACA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introduction

This is the webinar that informs the community about what is going on with Open Source Python projects.  Today's project being highlighted is Spyder.


* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau, he is the leader of open team development at Quansight.
* **Guest:** Carlos Cordoba, lead developer of Spyder. He joined Quansight just a couple months ago and is based out of Bogota, Colombia.

### Project Overview

Spyder is an open source scientific computing IDE. It has approximately 3400 stars on github, it has over 100 contributors, and about 40-50 PRs per month. On its user base there are around 30000 downloads per month on PyPI, and about 200 issues per month opened.

A fellow named Pierre started this project, because he wanted an IDE similar to Matlab for his co-workers.  At that time he worked at the Commission of Atomic Energy in France as a physicist. Spyder came out of a previous project that he had put together called PyD, and then with that as a basis he started Spyder in 2009.  Carlos came on board in 2010 and helped create some bug fixes and other features.  He had to quickly learn in 2015 how to maintain a Python project because Pierre got a promotion at the laboratory and wanted Carlos to take over the project continuation.

Spyder is a desktop application, and these days that is kind of rare.  Having it desktop, rather than web based, allows for the creation a richer application.  One example of this is the fact that at the moment Spyder has about 17 difforent plugins that are able to work while being integrated together. If you were to look at how many packages the Spyder team has collected over time, you would see that there are currently up to 88 plugins.  This is Spyder can be called a true IDE, because it has truly tried to be made into a fully integrated experience.  The hope is that users will never need to leave the IDE to complete a different part of their scientific Python project.

There are a few alternative projects out there for instance Pyzo; which was developed by Omar who worked with Carlos at Anaconda and now he is a freelancer.  This project was the main competitor at one point, but now Omar is also trying to create an IDE/framework which they are calling Flex.  Flex would be a web based IDE though, so really Spyder is kind of the only ones in this category.  Although it is not Python based, R Studio is probably the closest equivalent out there.

Spyder is built on PyQt, and that was the main reason that Carlos joined the work.  He really didn't like using JavaScript so this was a great alternative.  It started with PyQt 4, and Carlos migrated it to PyQt 5 for the Spyder 3 release.  This was a huge migration because PyQt 4 had such a different callback system, they went more Pythonic and this required the to convert all the code.

The project started with Pierre, but Carlos was the first contributor. He had used Mathematica for several years and really liked the documentation center that it had.  Because of this he wanted something similar for Python.  Pierre was helping, but so far his work could only show doc streams in plain text format.  Carlos began looking for something to convert doc streams to html automatically.  He found PyQt to be good since it had a web widget which was capable of rendering the html to show to users as a web page.  He found a very small snippet of code in the Sage project which did the same thing, so he cleaned it up and sent it to Pierre.  That was essentially the first contribution to the project.

### Demo

You can find the information from the demo on the [Spyder website here](https://www.spyder-ide.org/).

### Roadmap

1. **Language server protocol integration** This is a protocol developed by Microsoft and is very similar to the Jupyter protocol because these languages are agnostic. It is used by various tools such as VScode and Atom and other editors.  We do have the initial framework in place for this and we are preparing to release this feature with the beta V2.

2. **New debugging kernel and UI** This has been a request from many users, but would require a dedicated kernel to support the capability that people are asking for.  If completed, this would give users total control of execution, the ability to interact with variables, run arbitrary code and visualize the data at every step.  Doing this would also enable a new debugger panel to monitor the program flow and set breakpoints.

3. **Major enhancements to projects** Spyder has a projects feature, and it is limited to a current session for the most part and a current directory management.  The goal would be to integrate that with some additional best practice workflow tools and center that on reproducible environments.  You could then specify things like your Conda environment or Pip environment.  Specifically this could link things like Venf and Conda and other tools to make the projects notion a little more reproducible.

4. **Third Party Plugins** There are currently many plugins, but there is still a desire to have more.  This would also imply the improvement of existing plugins.  You need this maintenance feature to ensure backwards compatibility etc.

5. **Full support for the custom objects in the variable explorer** This concept embodies the killer feature of Spyder, and overall would just really be nice to have.  It has support for things like Numpy and arrays and data frames, but being able to customize it by plugging in your own types to that feature would be really great.  Jupyter is kind of similar with its display API that you can plug into, however that is not for arbitrary or generic objects.

6. **Keyboard shortcut and management presets** This would allow you to implement your own key sets, or allow you to transition from one IDE to another and things like that.

### Viewer Questions

Now we will move into the question and answer session.

**Q.** How is the connection with Github, is there any, or is it planned?

**A.** We do not currently have a way to handle git projects, or to push to github directly.  It is on our to-do list though, and hope to be able to do that next year.  Currently the licensing issues are in the way.

---

**Q.** Why did you discontinue the terminal window?

**A.** You actually can still execute in an external terminal, we do not have support for Mac, but it does work on Linux and Windows.

---

**Q.** How can you import/export custom preferences for Spyder?

**A.** That option is not yet available for Spyder, but we may include that in version 4 or 4.1.

---

**Q.** What is the current contributor base?

**A.** There are currently about 5 contributors, and they have been active in the last year.

---

**Q.** Is there a way to suppress the output for telling me what step I am on?

**A.** That is more of a Python thing, but we are trying to develop a new debugging kernel that should improve the debugging experience.

---

**Q.** How do you find time to do open source projects between the full time job and personal life?

**A.** So I am actually working part time with Quansight, and without their support the project might not be able to survive.  As for personal life, I don’t have a personal life so in other words github is my social life.

---

**Q.** Has testing been performed with Tensorflow or Keras with deep neural nets (maybe a depth of 200)?

**A.** No, we have not performed testing with those, but if your code works in Jupyter Notebook then it should work in Spyder because we use the same kernels and protocols.

### Footnotes & Links

* For us to have a sustainable model to promote this and other projects, it is a great help to have time or finances contributed to supporting projects like Spyder.
* To see the current roadmap visit [Quanisight's website](https://quansight.com/projects)
* [Spyder’s new website](https://www.spyder-ide.org)
