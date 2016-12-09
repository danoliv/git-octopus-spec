# git-octopus-spec
<a href="https://copr.fedorainfracloud.org/coprs/baitaand/git-octopus/package/git-octopus/"><img src="https://copr.fedorainfracloud.org/coprs/baitaand/git-octopus/package/git-octopus/status_image/last_build.png" /></a>

Spec file for git-octopus rpm packaging.

https://github.com/lesfurets/git-octopus

## References
#### Original project:

https://github.com/lesfurets/git-octopus

#### Spec file project:

https://github.com/danoliv/git-octopus-spec

## Prerequisites

Install mock and add current user to mock group:

    sudo yum install mock
    sudo usermod -a -G mock $(id -u -n)
    
Clone the spec file project (the project contains the spec file needed to build the rpm)

    git clone https://github.com/danoliv/git-octopus-spec.git

## Update the spec file

**You should modify the spec file following the official guidelines: [https://fedoraproject.org/wiki/Packaging:Guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines)**

Check the last available version of git-octopus from the official repo: [https://github.com/lesfurets/git-octopus/releases/latest](https://github.com/lesfurets/git-octopus/releases/latest)

Update the Version tag of the spec file to match the latest version, set the Release number to 1:

    Name:   	git-octopus
    Version:	1.4
    Release:	1%{?dist}
    Summary:	Git commands for continuous delivery
    
Update the changelog in the spec files:

    %changelog
    * Tue Dec 06 2016 Andrea Baita <andrea@baita.pro> - 1.4-2
    - added documentation build, updated build requires
     
    * Wed Nov 30 2016 Andrea Baita <andrea@baita.pro> - 1.4-1
    - Packaging of version 1.4.
     
    * Thu Nov 17 2016 Xavier Bachelot <xavier@bachelot.org> - 1.3-1
    - Initial package.
    
## Build the RPM

retrieve the tarball, the file will be put into `~/rpmbuild/SOURCES` (will create a directory if not exists)

    spectool -g -R git-octopus.spec
    
build the source rpm, the file will be put into `~/rpmbuild/SRPMS/` (will create a directory if not exists):

    rpmbuild -bs git-octopus.spec
    
finally build the rpm, by passing the src.rpm file created in the previous step:

    mock -r epel-6-x86_64 ~/rpmbuild/SRPMS/git-octopus-1.4-2.el6.src.rpm

the results will be usually available in the directory: `/var/lib/mock/epel-6-x86_64/result` (check the output of mock command)

**If the rpm build fails the spec there could have been some incompatible modification on the code, the spec file should be updated accordingly.**

## Test the new package

check the rpm by compiling and installing in the local machine

    mvn clean install
    sudo yum install <specify local rpm>
    
check the git octopus version

    git octopus -v

## Make a pull request

follow the following guide: https://guides.github.com/activities/forking/
