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
> Purpose of Installation Guide:
>   
> Simplified Installation: This manual simplifies difficult installation procedures into clear directions. Installing, uninstalling, and upgrading the software is made simple and straightforward for all users, regardless of expertise level.  

Improved Understanding: By providing information about the software's functionality, this guide helps users better comprehend the underlying technology. It encourages self-sufficiency by giving users the ability to configure the software on their own.  

Error Prevention: Instructions that are clear can help users avoid common installation difficulties and errors. Carefully following the instructions reduces the likelihood of problems for users.  

Good User Experience: Having an installation manual available helps make the user experience better overall. User satisfaction increases when consumers can install the software successfully. 

 

System Requirements 

Operating System: Windows 10 or later 

Processor: Intel Core i5 or newer 

RAM: 8 GB or more 

Disk Space: 1 GB or more free space 

Monitor/Display with 1920x1080p minimum resolution and 2160x1440p maximum resolution 

Trace Installer 

Browser app capable of viewing/opening PDFs, For Example chrome, Firefox, Edge, etc. 

Browser capable of surfing the web 

May need to turn off windows defender to allow installation of exe. 

Internet Connection: Required for installation and updates 

 

Downloading the Installer 

Download TRACE Installer 

Visit the official GitHub pages of TRACE at GitHub - ssstrong1/Group_14_TRACE: TRACE Project 

You can click Code and click download zip:You can also click on TRACE Release under Releases: Then click on source code (zip). Optionally, you can follow the instructions below for an alternative 

If you don't want to download the zip, instead navigate to the "Installer" Folder. 

From here you can click on tracesetup.exe, then click on the three dots in the right-hand corner and click download:Make sure to check your browser downloads area. If you get this message: make sure to click on the three dots next to your file and select keep. This message will pop up next: Select Show more and select Keep anyway. Your file should now be downloaded. 

 

Download Troubleshooting 

 

If you get this message: Navigate to your windows security. 

From there click Virus and Threat Protection: 

Then click Protection History: 

Next Navigate to the file that was blocked: 

 and select actions then restore. Your download is now restored and ready to be used. Navigate to your download folder and see that it is accessible now: 

 

Installing the Software 

Running the Installer File with the Zipped Folder 

Find the downloaded zip folder (either Group_14_TRACE-main.zip or Group_14_TRACE-1.0.0.0.zip if installed from releases) in your system's Downloads folder. 

Double-click on the zipped folder and extract the contents 

Navigate to your new extracted folder and inside locate tracesetup.exe in the installer folder 

Double-click on the installer file (tracesetup.exe) to run it 

Follow the Installation Wizard 

The installation wizard will help you through the installation process. 

Choose the installation directory where you want to install TRACE. 

Click "Next" to proceed with the installation. 

Complete the Installation 

Once the installation is complete, click "Finish" to exit the installation wizard. 

TRACE is now installed on your system and ready to use. 

 

Running the Installer File without the Zipped Folder 

Find the downloaded installer file (tracesetup.exe) in your system's Downloads folder. 

Double-click on the installer file to run it. 

Follow the Installation Wizard 

The installation wizard will help you through the installation process. 

Choose the installation directory where you want to install TRACE. 

Click "Next" to proceed with the installation. 

Complete the Installation 

Once the installation is complete, click "Finish" to exit the installation wizard. 

TRACE is now installed on your system and ready to use. 

 

 

Launching the Software 

There are two options to running the application. 

1st you can right click on the TRACE icon inside the location where you installed it and select run as an administrator 

2nd you can right click on the TRACE icon inside the location where you installed it and click on properties: 

From there you can customize how you run the program by selecting the compatibility tab and choosing run this program as an administrator and clicking apply: 

If you opted to create a Desktop Shortcut you can now double-click it from your Desktop and use the program if you have changed the mentioned settings for the program 

If you have not changed the settings for the program, then you will need to right-click the application and run it as an administrator every time. 

If you are logged in as an administrator, then you do not need to right-click the program and do any of the above. All you need to do is double click the application to run it. 

Alternatively, you can find trace_main.exe in the Program Files (x86)/TRACE. 

 

 

Uninstalling the Software 

Open the Control Panel. 

Go to "Programs" or "Programs and Features." 

Find TRACE version 1.0.0.0 in the list of installed programs. 

Click on TRACE version 1.0.0.0 and select "Uninstall." 

Follow the on-screen prompts to complete the uninstallation process. 

Alternatively, you can just delete the folder where it is installed 

 

Troubleshooting 

If you have installed everything correctly but cannot see what you downloaded or installed, you will have to restore it from windows defender see Downloading the Installer (Download Troubleshooting) and follow the steps provided or install it as an administrator. In many cases windows defender flags many apps as viruses when they currently are not. 

Once logged in, if you are not using the recommended resolutions settings you may want to change them for proper use of the application. 

If you get an error message such as (this program does not have the elevated level it needs or something else) it is because you are not running it as an administrator: 

Support and Contact Information 

Links: 

Unable to Install Apps or Software on Windows? Here's What to Do (makeuseof.com) 

Top 6 Ways to Fix Unable to Install Programs or Software on Windows 11 - Guiding Tech 

Windows 11 common problems — and the fixes | Windows Central 

9 Ways to Fix Unable to Install Apps or Software on Windows 11 - Gadgets To Use 

Contact Information: 

Project Manager: Stephen Strong – ssstrong@my.waketech.edu 

User Interface Specialist: Alexi Mcnab - acmcnabb@my.waketech.edu 

Back-End Specialist: Dyaln Arone - daarone@my.waketech.edu 


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

