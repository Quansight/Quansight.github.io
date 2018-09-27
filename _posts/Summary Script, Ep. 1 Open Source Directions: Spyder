---
layout: post
title: Open Source Directions Episode 1: Spyder
---```

### Introduction

This is the webinar that informs the community about what is going on with Open Source Python projects.  Today's project being highlighted is Spyder.

Welcome to everyone, thank you for joining us, and I am your host Anthony Scopatz.

David Charboneau is our co-host, and he is the leader of open team development at Quansight.

Carlos Cordoba joins us as the lead developer of Spyder. He joined Quansight just a couple months ago and is based out of Bogota, Colombia.

### Headlines 

Before we get started, here are some open source headlines in the news: The first story is about Shannon Labs and their $100,000 funding offer for breakthrough ideas in neuroscience or brain computer interfaces and other ideas.

In other news, stack overflow released a new code of conduct that replaces their policy of “be nice”.  One great thing about this is that it encourages friendly ways to comment and discourages specific unfriendly ways to comment on posts. It is certainly worth checking out if you are interested in the behavior of people online, whether civil or otherwise.

I have some news about Spyder: We are about to release two new versions. The first bug fix version of our 3-3 series: 3-3.1. This new release fixes a couple of bugs regarding connections to external kernels, which have been started in different interpreters other than the one Spyder is running on. We are also about to release our first beta for Spyder 4.

### Project Overview

Now we will move on to introducing the project. Spyder is an open source scientific computing IDE. It has approximately 3400 stars on github, it has over 100 contributors, and about 40-50 PRs per month. On its user base there are around 30000 downloads per month on PypI, and about 200 issues per month opened. 

Q. So Carlos, why was this project started, and what inspired the work?
  A. Pierre is really more qualified to answer this question since he started the project, but my understanding is that he wanted an IDE similar to Matlab for his co-workers.  At that time he worked at the commission of atomic energy in France as a physicist. It came out of a previous project that he had put together called PyD, and then with that as a basis started Spyder in 2009.  I (Carlos) came on board in 2010 and helped create some bug fixes and other features.  I had to quickly learn in 2015 how to maintain a Python project because Pierre got a promotion at his job and wanted me to take over the project continuation.

Q. What sort of need does Spyder fill in the broader Pydata, Scipy stack and ecosystem?
  A. Spyder is a desktop application, and these days that is kind of rare.  Having it desktop, rather than web based, allows us to create a richer application.  One example of this is that fact that at the moment we have about 17 diffornet plugins that we are able to work at integrating together. If you were to look at how many packages we have collected over time you would see that we are currently up to 88.  This is why we can call Spyder a true IDE, because we have really tried to make it a fully integrated experience.  The hope is that they never need to leave the IDE to complete a different part of their scientific Python project.  

Q. We have already mentioned Matlab, are you aware of any alternative project out there?
  A. Yes, there is for instance Pyzo which was developed by Omar who was working with me at Anaconda and now he is a freelancer.  This project was our main competitor at one point, but now Omar is also trying to create an IDE/framework which they are calling Flex.  Flex would be a web based IDE though, so really we are kind of the only ones in this category.  Although it is not Python based, R Studio is probably the closest equivalent out there.  

Q. What is this technology built on?
  A. It is built on PyQt, and that was the main reason that I joined the work on Spyder.  I really don’t like using JavaScript so this was a great alternative.  It started with PyQt 4, and I migrated it to PyQt 5 for the Spyder 3 release.  This was a huge migration because PyQt 4 had such a different callback system, they went more Pythonic and this required us to convert all the code.  

Q. The project started with Pierre, but were there other folks involved in the beginning, were you one of the first?
  A. So, I would say I was the first contributor, yes. I had used Mathematica for several years and I really liked the documentation center that it had.  Because of this I wanted something similar for Python.  Pierre was helping, but so far his work could only show doc streams in plain text format.  I began looking for something to convert doc streams to html automatically.  I found PyQt to be good since it had a web widget which was capable of rendering the html to show to users as a web page.  I found a very small snippet of code in the Sage project which did the same thing, so I cleaned it up and sent it to Pierre.  That was essentially my first contribution to the project.  

### Demo

Now that we have learned a little more about the background of the project, we will move into the demo.  You can find the information from the demo on the Spyder website at: www.spyder-ide.org

### Roadmap

Now we will move to our roadmap discussion, to broadly discuss where the project is going and some of the large scale features that people might be able to help with.

1. Language server protocol integration

This is a protocol developed by Microsoft and is very similar to the Jupyter protocol because these languages are agnostic. It is used by various tools such as VScode and Atom and other editors.  We do have the initial framework in place for this and we are preparing to release this feature with the beta V. 2.

2. New debugging kernel and UI

This has been a request from many users, but would require a dedicated kernel to support the capability that people are asking for.  If completed, this would give users total control of execution, the ability to interact with variables, run arbitrary code and visualize the data at every step.  Doing this would also enable a new debugger panel to monitor the program flow and set breakpoints.

3. Major enhancements to projects

Spyder has a projects feature, and it is limited to a current session for the most part and a current directory management.  The goal would be to integrate that with some additional best practice workflow tools and center that on reproducible environments.  You could then specify things like your Conda environment or Pip environment.  Specifically this could link things like Venf and Conda and other tools to make the projects notion a little more reproducible. 

4. Third Party Plugins

There are currently many plugins, but there is still a desire to have more.  This would also imply the improvement of existing plugins.  You need this maintenance feature to ensure backwards compatibility etc.

5. Full support for the custom objects in the variable explorer

This concept embodies the killer feature of Spyder, and overall would just really be nice to have.  It has support for things like Numpy and arrays and data frames, but being able to customize it by plugging in your own types to that feature would be really great.  Jupyter is kind of similar with its display API that you can plug into, however that is not for arbitrary or generic objects.

6. Keyboard shortcut and management presets

This would allow you to implement your own key sets, or allow you to transition from one IDE to another and things like that.

### Viewer Questions

Now we will move into the question and answer session.

Q. The first question is; how is the connection with Github, is there any, or is it planned? 
  A. We do not currently have a way to handle git projects, or to push to github directly.  It is on our to-do list though, and hope to be able to do that next year.  Currently the licensing issues are in the way.  

Q. Why did you discontinue the terminal window?
  A. You actually can still execute in an external terminal, we do not have support for Mac, but it does work on Linux and Windows.  

Q. How can you import/export custom preferences for Spyder?
  A. That option is not yet available for Spyder, but we may include that in version 4 or 4.1.

Q. What is the current contributor base?
  A. There are currently about 5 contributors, and they have been active in the last year.

Q. Is there a way to suppress the output for telling me what step I am on?
  A. That is more of a Python thing, but we are trying to develop a new debugging kernel that should improve the debugging experience.  

Q. How do you find time to do open source projects between the full time job and personal life?
  A. So I am actually working part time with Quansight, and without their support the project might not be able to survive.  As for personal life, I don’t have a personal life so in other words github is my social life.

Q. Has testing been performed with Tensorflow or Keras with deep neural nets (maybe a depth of 200)? 
  A. No, we have not performed testing with those, but if your code works in Jupyter Notebook then it should work in Spyder because we use the same kernels and protocols. 

### Concluding Information

For us to have a sustainable model to promote this and other projects, it is a great help to have time or finances contributed to supporting projects like Spyder.

Spyder’s new website: www.spyder-ide.org 

Thanks for watching, and you can find the Spyder roadmap here: www.quansight.com/projects 
