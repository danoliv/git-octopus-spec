# git-octopus-spec
<a href="https://copr.fedorainfracloud.org/coprs/baitaand/git-octopus/package/git-octopus/"><img src="https://copr.fedorainfracloud.org/coprs/baitaand/git-octopus/package/git-octopus/status_image/last_build.png" /></a>

Spec file for git-octopus rpm packaging.

https://github.com/lesfurets/git-octopus

# usage
  get the tarball
  
  `spectool -g /path/to/git-octopus.spec`

  build srpm
  
  `rpmbuild -bs /path/to/git-octopus.spec`

  build rpm
  
  `mock -r epel-6-x86_64 /path/to/git-octopus-1.3-1.fc25.src.rpm`

