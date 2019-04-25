---
layout: post
title: Episode 16 - Chainer - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/IMiQin-S6ME" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [Chainer](https://chainer.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest 1:** Crissman: is an engineer working in the CuPy and Chainer teams at Preferred Networks, which is an AI startup in Japan.

### Project Overview

Chainer is a flexible and intuitive framework for Neural Networks and leverages CuPy for calculations on GPUs.  As of March 14th, there were 4,600 stars on Github About 30k downloads/month on PyPI.  

Chainer was written back in June of 2015.  At the time the only existing deep-learning framework was Theano.  So Chainer became one of the first ones to come into the Python language.  In general, it makes it easier to program when working with neural networks. It also created the Define-by-Run system, which was later adopted by PyTorch and recently by Tensorflow, for their 2.0, as "Eager Mode." It just kind of makes it easier to do deep learning calculations. TThis allows your neural network to be interpreted as it is run, giving more ability for researchers to focus less on the back end and more on the models. 

The market here is fairly busy and it includes Google’s TensorFlow and Facebook’s PyTorch.  Each project borrows from one another, for instance, Chainer was the first one to implement define by run.  Also, Chainer was intended specifically to make neural networks easier in Python. 

Chainer is pure Python although they are looking at moving into some C++.   Python works great on the front end, but in general, it is better in the long term for the sake of speed to have the backend running in a C++ kind of environment. 

Originally Chainer was started by one of Crissman’s Japanese colleagues named Seiya Tokui.  He was writing it as his third attempt at making a deep framework.  In Japan, there is about a week worth of holidays in May, and it was over that week that he was able to create Chainer.  Today a team of about six people, lead by Tokui-san at Preferred Networks maintain the project.  The goal is to keep Chainer the best tool to use for deep learning.  

The most visible user group for Crissman is within the company he works for.  Preferred Networks has a strong user base within the company because they like to use and support their own software and with most of the company’s work revolving around neural networks; they are largely coders. Their work and applications of Chainer include the development of autonomous driving technologies, robotics, and other industrial applications for Deep Learning. Aside from Preferred Networks staff, the user base is mostly from programmers within Japan and various spaces in academia. In December, Chainer joined NumFOCUS, and along with NumFOCUS, they’re participating in the Google Summer of Code program, which has helped bring in more contributors from outside of Japan.

A large part of Chainer contributors come from Japan, and there’s an extremely high level of homogeneity among the Japanese. It’s estimated that 98.5% of Japan’s population is Japanese. With the NumFOCUS partnership, there has been some diversity here, but it continues to be a gradual process of including different groups of people into this project.  As a result, most diversity comes from foreigner contributors, like Crissman. They’re always interested in more contributions for Chainer, and welcome help from whoever is interested.  This year they are participating in the Google summer of code, and the hope is that as they participate in events like this there will be an increased international interest in the project.


### Demo

[Demo at timestamp 12:59](https://youtu.be/IMiQin-S6ME?t=779)
[Chainer on Colab](https://colab.research.google.com/drive/1qK4I__mXH3RkRt_DFJOIARxnmjwtchl8)
[Talk on YouTube](https://www.youtube.com/watch?v=5xDhNpPyBv4)

### Roadmap Discussion

Currently Chainer is in beta release for the next generation, ChainerX. ChainerX was created to allow Chainer to continue delivering the maximum performance for the hardware it is running on by addressing bottlenecks in deep learning. At this point, the bottleneck on performance continues to be the Graphics Cards. That said, as current trends continue for both CPU and GPU speeds, eventually, the overhead of running Python will be material to the overall computing speed.

Work started on ChainerX, in stealth mode, to extend the functionality of Chainer and ensure that Chainer continues to make full use of the available hardware.  In addition, moving to a C++ backend allows greater flexibility for Chainer. The C++ API also makes ChainerX exportable, meaning that it can be compiled and used in devices without Python.  The current structure utilizes Scithon bindings so that the transition is smooth for users.  

ChainerX has also been built for expansion. While the current version of Chainer is focussed on Intel CPUs and NVIDIA GPUs, custom backends can be designed to work with ChainerX, allowing computation on new hardware, such as AMD or FPGA.  The X in ChainerX actually stands for X-tensible, X-celerated, and X-ecutable.  

One of the projects they are working on for the company is to come up with personalized robots.  So far they have done some focus groups and other things, and they found that what they thought would be achievable in a few years and desired most was a house tidying robot.  They were able to hold a demonstration at C-Tech in Japan using an HSR robot from Toyota.  They had programmed it to identify over 300 objects that it could pick up.  The team set up a fake living room environment for it to work in and it successfully ran for 5 days straight.  

Looking forward, they want to continue to develop the Chainer specialized modules, such as ChainerCV for Computer Vision and ChainerRL for reinforcement learning.  Once ChainerX is ready, even people who do not use Python will suddenly have access because of the versatile C++ backend.  This will become increasingly important as the world shifts to working on smaller devices which may not have large computing ability.  

### Footnotes & Links

* Chainer Forum [here](https://groups.google.com/forum/#!forum/chainer)
* [Chainer Website](https://chainer.org/)
* [GitHub page](https://github.com/chainer/chainer)
* [Slack Channel](https://bit.ly/join-chainer-slack)

