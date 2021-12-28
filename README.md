# conda_packager
Exhibits how to create a package from scratch from a repository.

## Creating Conda Package from Scratch
Required files:
- build.bat: Runs Python/software commands while setting up the package (WINDOWS)  
- bld.sh: Runs initial Python/software commands while setting up the package. (LINUX)  
*(Unneeded if you have a setup.py)*
- meta.yaml: Contains all meta data for the conda package  

### meta.yaml
[meta.yaml Reference](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html)

To remove old/outdated package files: `conda build purge`

**Reference(s):**

## Installing Conda Package
After running 'conda build [package]' the package filename and location are displayed on the console.  
```
Default:
    Miniconda:  C:\Users\[user]\miniconda3\envs\conda_dev\conda-bld\win-64
    
Note: This is just an example and depends on your local setup (Operating System, and Anaconda vs Miniconda).
```
Install newly built conda package on your local program:  
`conda install --use-local [package]`

## Maintaining a Conda Channel
[Create Conda Channel](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/create-custom-channels.html)
1. Create your conda channel directory structure:  
```
channel/
    linux-64/
        package-1.0-0.tar.bz2
    linux-32/
        package-1.0-0.tar.bz2
    osx-64/
        package-1.0-0.tar.bz2
    win-64/
        package-1.0-0.tar.bz2
    win-32/
        package-1.0-0.tar.bz2
```
2. Run `conda index [channel/]` while in the channel's root directory. This generates a `repodata.json` file within
the repository directory which gives conda access to package metadata.  

**You must run this command each time you create/modify a package on this channel**

3. You can test the contents of your conda channel with the following command:  
```
conda search -c [channel URL] --override-channels

>> Loading channels: done

# Name                      Version     Build   Channel
click                       8.0.3       py38_0  Conda_Test_Channel
```

## Updating Conda Config File (condarc)
The condarc file is an optional runtime configuration file that allows advanced users to configure various aspects of
conda such as channels for searching packages, proxy settings, and environment directories. This file is automatically 
created in the home directory:  
`C:\Users\[user]`  

```
# Example condarc file:

# Added local conda channel to 'channels' in addition to conda-forge
channels:
  - C:\Users\aaram\Desktop\Conda_Test_Channel
  - conda-forge
  - defaults
  
# Set conda-build parameters to automatically place tar.gz2 files within local conda channel
conda-build:
  include_recipe: false
  output_folder: C:\Users\aaram\Desktop\Conda_Test_Channel
  root-dir: C:\Users\aaram\Desktop\Conda_Test_Channel
  skip_existing: true

# Default for ssl verification is true. Ensure this is the case when modifying these config files.
ssl_verify: true
```

[.condarc Reference](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html)

### Basic Commands
```
# Add the conda-forge channel
conda config --add channels conda-forge

# Add a custom channel
conda config --add [channel URL]

# Always choose 'yes' when asked to proceed. (Default is False)
conda config --set always_yes True

# Specify conda-build output root directory
# Set with CONDA_BLD_PATH environment variable (Default: <CONDA_PREFIX>/conda-bld/
    
# Set manually within condarc
conda-build:
    root-dir: ~/conda-builds
```

### Advanced Concepts
1. **Environment condarc**: You can place a condarc file within your environment's root directory to override conda defaults such as channels.
2. **Proxy Settings**: Configure conda for use behind a proxy server  
```
proxy_servers:
    http: [Server Address]:8080
    https: [Server Address]:8080
```
3. **Offline Mode**: filters out conda channels that do not use the `file://` protocol
4. **Only download .tar.bz2 Packages**: `use_only_tar_bz2: True`

## Troubleshooting
**Numpy Version Warning**  
No numpy version specified in conda_build_config.yaml.  Falling back to default numpy value of 1.11

This is a benign warning. When installing the conda_packager from the output .tar.gz2 file, the latest version of Numpy
was installed (when not specified within the meta.yaml)

## Topics to Explore
1. You can add Anaconda.org tokens to allow users to see private packages. Set `add_anaconda_token: True`
```
# When the channel alias is Anaconda.org or Anaconda Server GUI you can set the system configuration so users automatically
# see private packages.

# Add the token to the channel URLs
conda install anaconda-client

# Login to you Anaconda account
anaconda login
```

