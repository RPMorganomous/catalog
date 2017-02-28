#Classic Rock Hall Of Fame Catalog

##Main technologies and methodologies implemented:
* Python 2.7
* Flask
* Bootstrap
* SQLAlchemy
* sqlite
* JSON
* CRUD
* HTML
* CSS
* OAuth
* Vagrant Virtual Machine
* Google API
* Facebook API

This catalog project is a Python module that uses an sqlite database to manage bands and albums from the classic rock genre.  The purpose of this project is to demonstrate aptitude with Create Read Update and Delete database functionality.

The program is tested by executing project.py.  If all goes well, when you open your browser and point to localhost:8000 you will see this:

![alt tag](https://github.com/RPMorganomous/catalog/blob/master/static/screenshot.png)

#Follow These Steps To Test The Program
(I'm assuming you already have python2.7 installed)

###Install Virtualbox###
https://www.virtualbox.org/wiki/Downloads

###Install Vagrant###
https://www.vagrantup.com/downloads

Verify that Vagrant is installed and working by typing in the terminal:

    $ vagrant -v   # will print out the Vagrant version number

###Clone the Repository###

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).  
(On Mac or Linux systems you can use the regular terminal program.)

You will need Git to install the configuration for the VM. If you'd like to learn more about Git, [take a look at our course about Git and Github](http://www.udacity.com/course/ud775).

Once you are sure that VirtualBox and Vagrant are installed correctly execute the following:

    $ git clone https://github.com/RPMorganomous/catalog.git
    $ cd vagrant
    $ cd catalog

###Verify that these files exist in the newly cloned repository:

    --catalog                    #folder containing tournament files
    ----project.py               #file that contains the python functions which 
                                    unit tests will run on
    ----band_database_setup.py   #unit tests for tournament.py
    ----bandalbumswithusers.db   #sqlite database
    --Vagrantfile                #template that launches the Vagrant environment
    --pg_config.sh               #shell script provisioner called by Vagrantfile
                                    that performs configurations

###Launch the Vagrant Box###

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

    $ vagrant up   #to launch and provision the vagrant environment
    $ vagrant ssh  #to login to your vagrant environment
    
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

From the terminal, run:

    git clone https://github.com/udacity/OAuth2.0 oauth

This will give you a directory named **oauth** complete with the source code for the flask application, a vagrantfile, and a bootstrap.sh file for installing all of the necessary tools. 

## Run the virtual machine!

Using the terminal, change directory to oauth (**cd oauth**), then type **vagrant up** to launch your virtual machine.

###Change Directory To The Catalog Directory###

    $ cd /
    $ cd vagrant
    $ cd catalog

###Initialize the database### 

(Optional unless you want to use the pre-configured database.  Otherwise, you can delete bandalbumswithusers.db and recreate it using the following commands)

    $ python band_database_setup.py     #creates the database
    $ python lotsofalbums.py            #import a dummy user and the first three bands with albums into the database 
                                        (note that if you wish to have permission to edit these three, you must run the
                                        server and log in using the next steps BEFORE importing the database)
You should see this result:

    Bands and albums successfully imported!

###Run the application###

    $ python project.py

    Open your browser and point to localhost:8000
    Use the LOGIN option at the upper right of your screen to log in using Google or Facebook.  Upon first login you will
    be added as a new user with permission to edit any bands or albums you create.

###Shutdown the application###

    ctrl+C

###Shutdown Vagrant machine###

    $ vagrant halt


###Destroy the Vagrant machine###

    $ vagrant destroy

###Coming Soon - UPGRADES###
* More detail on bands and albums
* Gear and performance tips to reproduce the music you love
* Option to order the albums from Amazon.com

