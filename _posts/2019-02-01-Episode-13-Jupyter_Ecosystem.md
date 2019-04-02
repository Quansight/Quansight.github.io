---
layout: post
title: Episode 13 - Jupyter Ecosystem - Open Source Directions
author: bsodenkamp
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/HzyfFSLfHiQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [The Jupyter Ecosystem](https://jupyter.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest 1:** Carol Willing, is a Jupyter Steering Council member, core developer with a focus on Jupyter's use in learning (over 5 years), and a Python core developer.
* **Guest 2:** Matthias Bussonnier,  by Day he facilitates research at the University of California, Merced, and by Night he is a Pythonista (mostly), and one of the early founders of Jupyter and a core developer of Jupyter as well as IPython.

### Project Overview

 Just like many open source projects it is difficult to track exactly how many users there are because people can pretty much do whatever they want with the code.  Preferring not to try and track users has made it even a bit more difficult to figure out who the users are, but the preference is for people to come to the dev team and let them know about their use case.  From these interactions with users they believe that the majority of users are physicists or biologists.  The rough estimate for number of users in 2018 was at about 8 million worldwide.  Just as a comparison, there are about 21 million developers worldwide, about 4.4 million in North America and about 24 million users on GitHub in 2018.  This being said, these numbers are rough statistics because of the aforementioned lack of data.

The crux of this project is filling in for Interactive Computing and having Literate Computing (as opposed to Literate Programming). It fulfills a crucial role for exploratory programming, which enables the user to interact and play with their data. Even if someone does not have a background in computer science, they can rapidly leverage their computing power with Jupyter.  It was also designed around access to a web browser for that leveraging capability over the programming language.

Early on after the switch from IPython notebooks to Jupyter, they did some early tests with the San Diego user group and realized the potential that this project had to make computer science fun.  The simplicity of the software helped contribute to an overall feeling that it was non-intimidating.  Although it was simple, it was also capable of being engaging and doing complex things.  Carol began her exploration of Jupyter with a music theory library, and immediately felt welcomed by the experience.  The hardest thing to get used to is using ‘Shift’+’Enter’.

There are two main areas where other people are working on similar things to Jupyter and the first is UI.  Some of these different UIs are actual competitors.  Some IDE-like competition might be RStudio, or Spyder.  Some of the notebook like UI competitors might be Zeplin, Nteract, and Colaboratory.  An example of a text editor could be Vim. And one operating systems is Emacs. Keeping all this in mind, it is Important that compatibility is kept with as many things as possible going forward. Jupyter is meant to be seen not only as a default implementation but also a protocol. As long as you implement the protocol, it should function correctly.  You can develop your own custom things because of the way that Jupyter is build around a standard messaging specification designed for communication with a number of front ends.  Furthermore in the scope of sharing things, JupyterHub and Binder are distributed offerings that have been key projects in bringing notebooks to distributed users. One of the nice things about Jupyter’s original architecture is the concept of allowing people to write different custom things for authentication or spinning up notebooks in a particular way.  This has lead to the explosion of things like Colab, Azure notebooks, Amazon Sagemaker as well as Gryd, Paperspace, Digital Ocean, and Pangeo which use the Jupyter Lab technology.

The full implementation that Jupyter is built upon is Python, Javascript, Typescript, Tornado, and ZMQ. It is now run with [Python 3](https://python3statement.org/) of course, and just as a reminder to watchers, readers, or listeners, Python 2 EOL is Jan. 1st, 2020.  As far as deployments go, you can deploy Jupyterhub on bear metal but one of the things that really accelerated the adoption of Jupyterhub was Kubernetes and the ability to incorporate ideas from different disciplines. This power combo has encouraged productivity and learning through exploration and interactivity.

The project was technically started back in 2001 as IPython by Fernando Pérez.  He decided that he wanted to work on a new project and thought about ways in which he could link a bunch of languages together like Pearl, C, Python, etc.  He realized that he could glue together things with Python but it does not have a nice contracted story, but being a rebel he began working on IPython 0.1.  Over time other people helped out on the project like John Hunter [matplotlib](https://numfocus.org/programs/john-hunter-technology-fellowship), Travis Oliphant [Numpy](http://www.numpy.org/), Brian Granger, Min Ragan-Kelley, Paul Ivanov, and Thomas Kluyver just to cite a few.  Eventually they were able to win a grant which allowed them to make a network enabled console.  This further gave them the ability to embed images.  Around 2014 they decided to split IPython into multiple parts and this is when the Jupyter project started to take shape as IPython remained Python only.
The fact that Jupyter allows people to be effective and communicate the results of computations allows it to tell a powerful story for data scientists.  This combined with a rich community and ecosystem has created perfect conditions for a rapidly growing user base.  It also serves people who are working with many packages because it streamlines the whole process and makes life easier.  This success has also likely come directly from the Jupyter users that were the focus of this project, or at least the users that Jupyter notebook was targeted to in the beginning. It was mostly written by scientist for scientists who wanted a simple tool that could be usable for everyone without having a background in programming. There was clearly a large rate of adoption at SciPy 2012. Improvement in Python packaging helped a lot to contribute to success as well.  For the platform itself, it’s a browser and it’s powerful but simple. Being a free software is appealing to students, it also has a package manager, and you don’t have to wait for the fitting licence to become available from someone else in your lab.

There are approximately 20 regular attendees at the core developer meetings who you could say constitute the main contributors to the project at this point.  With such a small team there is a huge emphasis on the role of community contributors which continue to be helpful in the management of maintenance.  Using READMEs, they have tried to better communicate the names of maintainers, and try to give commit rights to more active contributors so that more people can feel included.  Since many of the community members are volunteers they will even try to fly them out to conferences from time to time so that they can have a chance to meet the team.  While there are many volunteers, the [ACM awards](https://blog.jupyter.org/jupyter-receives-the-acm-software-system-award-d433b0dfe3a2) list some of the longest running members of the contributor community. 

One of the fabulous things about this project being open source is that there has been global adoption, especially in areas of the world where it would be difficult to obtain a license to proprietary software.  The individuals who have taken to this project are from many languages like Python, Julia, and R.  Subjects that seem to utilize it the most range from science to digital humanities and some even use it for operations and training.  The contributors tend to be those who were originally just delighted users that wanted to continue building on this project that they enjoyed using.  There are many people who can see the value in this project and want to give back to it.  Educators have been instrumental in its continued growth at the highest levels as well as community workshops etc.  The enterprise crowd has even been utilizing it for things like machine learning.  Far a showcase of these uses you can browse the [Jupyter Blog](https://blog.jupyter.org/).

To help encourage diversity, they will often take the time to message new community members on an individual basis and ensure that they can feel comfortable participating in the community.  In addition to this, some of the Jupyter funding is reserved for diversity and inclusion efforts and so far there are two people who are working on [this program](https://blog.jupyter.org/outreachy-jupyter-supporting-diversity-in-open-communities-dfa78db4b0bd) by reaching out to people in an effort to bring them into the community.  Inclusion is a huge topic, so to make efforts more effective Carol tries to look at things based on their “multiplier Effect”.  One of the big things that was done in the Python community was to create a welcoming and thoughtful community.  The bar was constantly raised to ensure that the expectation for kindness and graciousness was always higher.  Simple things like using emojis helped to lighten the mood and achieve these goals of being more inviting.  Documentation is another critical aspect which allows people in the Jupyter Ecosystem to “learn how to fish”.  While it is desirable to do more in this area, many organizations are limited in their resource allocation to diversity efforts.  To address this it is important to help them understand that many of these efforts are just generally designed to grow the community and as that happens diversity will come.  



### Demo

[Demo at timestamp 34:13](https://youtu.be/HzyfFSLfHiQ?t=2053)
Jupyter demo [UI selection](https://jupyter.org/try)
Jupyter yt dev workshop [signup](https://yt-project.org/)

### Project Directions

1. **Technical:**  The JupyterLab subteam is still pushing JupyterLab toward 1.0, which is being worked on in addition to realtime collaboration.  Right now they are also working on pushing IPython toward async/await in the REPL. 

2. **Community:**  Most of the Jupyter’s success has come through other libraries which are used in Jupyter, so it is important not to overshadow them.  Currently there is something in the works which would be an iteration of a Jupyter Conference for 2019 though this is still not solidified.  In general though, greater efforts need to be made to empower the community with discourse, github, etc.

3. **Business and Sustainability:**  There is a critical need to keep the momentum and sustain that among the business elements of this project to ensure its long term success.  There are companies and organizations which have money that they can contribute, but the difficulty is that many of the strongest proponents of this software lack training in such things as fundraising. This will be an are of focus moving forward so that the project can continue to grow.

4. **Education:**  There has been great energy behind the open source model with using Jupyter in Education, and specifically the hope was always to help the notebooks to be dominant in this area.  Really the surface has just barely been scratched on this, and there is really a game changer.  An open source book was created by a group of current education users within three and a half days, and the hope is that this will evolve over time as people use things.  Community experiences will continue to feed back into education tips and best practices, helping to solidify this area of development.


### Viewer Questions

**Q.** As far as dashboarding/webapp are concerned, where is JupyterLab heading? I am aware of projects like Voila, but it's still young. What's the panorama of solutions?

**A.**  There is no one answer.  The potential solutions all have tradeoffs to them.  A few that I know about are Dash, plotly, Bokeh App, Voilà, and the IBM dashboard.  The difficult part about this is creating something that works across languages vs being language specific.  One example is that many people use Shiny with R, but that is specifically for R.  For that I am not sure I have a good answer because there are too many things involved with it.  The best solution might just be for you to get involved and start working on a solution.

---

**Q.** Last time I checked, interactive widgets were not working quite well with JupyterLab, any news/progress on that?

**A.**  As far as we can tell, once you have the extension enabled it should work. There can be issues when you are trying to use a private or undercommited API, so maybe an old-unstable classic notebook API.  These sorts of notebooks can break at any time.  Otherwise you can try to force refresh your browser, or post the issue in the repository.  One thing that we should probably document a little further is Python packaging because it can be very complicated.  Often times when the extensions don’t work, it’s due to not being installed correctly in the correct environment.  If you run into a roadblock here, then that is something that should definitely be asked about on Gitter.  

---

**Q.** I am also interested in dashboarding with appmode, voila, thebe etc. Currently using jupyterhub with appmode, but feel it is too easy for biz users to get to the code version by accident.

**A.**  I believe that is one of the reasons behind Voila, basically it tries to address the case for business where you want to hide everything and prevent the user from changing the code.  I don’t think that there is a perfect solution to this now because Jupyter is based on openness and it won’t do everything you want, but at some point you might have to consider the possibility that Jupyter is not yet the right solution.  Then your alternative is to perhaps hire an app developer to make something for you, but there are always tradeoffs to every avenue.  

---

**Q.**  Hi. Thanks for this seminar. Talking about diversity, there is an increasing trend on computational notebooks, ours, called [Grafoscopio](https://mutabit.com/grafoscopio/index.en.html) is done for/from a Global South perspective. Which could be a way to make these different approaches talk each other

**A.** I think I saw a note in the chat about using these tools in developing countries that don’t have a stable electrical grid, internet service, or bandwidth.  For these people the ability to have a stand alone project that does not rely so heavily on packages is very important.  One of the ways that we have tried to address this is with the Docker stacks which has a lot of different types of combinations of packages with the actual notebook interface.  There are also projects like Interact which can help.  I think we will continue to see more and more solutions which address the needs of various niches which is part of the benefit to having various front end UIs.  

### Footnotes & Links

* List of community channels [here](https://jupyter.org/community)
* [Jupyter Website](https://jupyter.org/)
* [GitHub page](https://github.com/jupyter/help)
* [Gitter page](https://gitter.im/jupyter/jupyter)
