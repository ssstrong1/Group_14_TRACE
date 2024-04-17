<br />
<div align="center">
    <h1>TRACE</h1>
    <h3>CSC-289-0001 - Group 14 README</h3>
</div>


<!-- TABLE OF CONTENTS -->

# Table of Contents
<li>
  <a href="#introduction">Introduction</a>
  <ul>
    <li><a href="#about">About</a></li>
    <li><a href="#purpose">Purpose</a></li>
    <li><a href="#contributors">Contributors</a></li>
  </ul>
</li>
<li>
  <a href="#setup">Setup</a>
  <ul>
    <li><a href="#installation-guide">Installation Guide</a></li>
  </ul>
</li>
<li>
  <a href="#tutorial">Tutorial</a>
  <ul>
    <li><a href="#user-guide">User Guide</a></li>
  </ul>
</li>
<li>
  <a href="#resources-required">Resources Required</a>
  <ul>
    <li><a href="#system-requirements">System Requirements</a></li>
    <li><a href="#internet-connection">Internet Connection</a></li>
  </ul>
</li>


<!-- ABOUT THE PROJECT -->
# Introduction
### About
> Goal: To provide an accurate estimate of the amount of tax owed by an individual or business entity to the government, based on their income and other relevant factors.
> 
> Objectives (Main): TRACE is a simple form-based tax calculation software, allowing a user to see what they owe and what their potential return could be. The program can calculate the estimated tax liability or refund for a given year based on the user’s income, deductions, etc.
> 
> Objectives (Details):
> - Provide a simple interface for calculating a user’s tax returns.
> - Reduce the number of errors in tax estimates
> - Complete all planned deliverables within our deadline.
> - Maintain clear communication throughout the project.
> - Adhere to Agile principles.
> - Develop a user interface where tax documents can be uploaded in less than 5 minutes
> - Process estimated tax due/owed in less than 30 seconds

>   
> Scope: The application takes forms 1040, 1099, and W2 as input for its calculations. The application does not consider any dynamic values as all calculations are done offline. The application accepts input and displays output through a simple form interface. Users from other states are not taken into consideration by the application; it is only used to calculate income taxes in North Carolina. The application uses SQLite database files as a portable means of saving the user’s input and its own output for later use. Multiple files can be opened in multiple instances of the application.
> 
> Overview: A user can enter values from their 1099 and W2 forms, and based on that, the application will calculate what they owe and their potential tax return. The user can export all their entered and returned values in a file which can be saved to disk and opened in the application later on.
The application is composed of multiple Python scripts, and its interface uses the tkInter library.
The application uses an SQLite library to create and read its saved files.


### Purpose
> This document provides detailed information regarding the Tax Return Accumulator, Calculator and Estimator
> or TRACE for short.

### Contributors
- Stephen Strong - Project Manager
- Alexi McNabb
- Dylan Arone


# Setup
### Installation Guide
> install required dependencies.


# Tutorial
### User Guide

# Resources Required
### System Requirements
- The minimum requirements for a user's computer is an operating system and machine that can run Python 3.10. Additionally, some disk space is needed to store the application and its files.
> 
- Windows OS
> 
- Machine capable of running 1920x1080p or 2160x1440p resolution
### Internet Connection
- The only requirements for an Internet connection is for downloading the application. Otherwise, the application does not communicate over the Internet whatsoever.

