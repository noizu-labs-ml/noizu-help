CONTRIBUTING
=====


## Local Development Setup

### 1. Clone Repo 
```bash
git clone git@github.com:noizu-labs-ml/smah.git
```

### 2. Setup asdf, direnv, and poetry

#### 2.1 ASDF (not currently used)
https://asdf-vm.com/guide/getting-started.html

```
cd ~/
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.1
```

Add asdf and auto completion hooks to your ~/.bashrc
```
. "$HOME/.asdf/asdf.sh"
. "$HOME/.asdf/completions/asdf.bash"
```


#### 2.2 Direnv
```
apt install direnv
```

Add to shell (in ~/.bashrc) and restart terminal session.
```
eval "$(direnv hook bash)"
```

#### 2.3 Conda 
Run the below and then refresh or restart terminal session.

##### 2.3.1 Install Miniconda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

chmod +x Miniconda3-latest-Linux-x86_64.sh

./Miniconda3-latest-Linux-x86_64.sh
```


#### 2.4 Poetry

```bash
conda create -n poetry python=3.10
```

##### Setup Pipx
https://pipx.pypa.io/stable/installation/

##### Setup Poetry
```bash
conda activate poetry
pipx install poetry   
```

### 3. Setup Environment

#### 3.1 Install Deps with Poetry
```bash
cd smah # go to repo folder
conda create -n smah-dev python=3.10
conda activate smah-dev   
poetry install
```

#### 3.2 Setup Environments

##### 3.2.1 Environment Variables
set OPENAI_API_KEY env variable or set key in your smah config file `~/.smah/config.yaml`

##### 3.2.1 Set Environment Variables with direnv
touch and add the following to smah/.envrc.dev

```bash 
export SMAH_OPENAI_API_KEY=${YOUR_OPENAI_API_KEY}"
```

and run `direnv allow` 

#### 3.2.2 Setup Environment Variables with .bashrc

Add the same line to the end of your `~/.bashrc` file 
```bash
export SMAH_OPENAI_API_KEY=${YOUR_OPENAI_API_KEY}"
```
Start a new terminal session or run `source ~/.bashrc`

Switch back to smah-dev conda environment
```bash 
conda activate smah-dev
```
#### 3.3 Build And Test

Test 

```bash
poetry run pytest --verbose
```

If tests look good: (of are known issues with your local change)

```bash 
pip build 
pip install
smah -q "Hello World"

```

The env active version of smah will now be pointed at your local repo.

On first run if not already configured you will be walked through the setup process.




## Publishing
### 1. add PYPI_TOKEN to .envrc.secret
```
export PYPI_TOKEN="your api token" 
```
### 2. config poetry
poetry config pypi-token.pypi $PYPI_TOKEN

### 3. build and publish
poetry publish --build