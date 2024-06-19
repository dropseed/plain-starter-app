<img src="https://boltframework.dev/assets/bolthead.svg" width="30" height="30">

# bolt-starter-app

This is the app starter kit for [Bolt](https://boltframework.dev/),
which includes everything you need for a database-driven app with users.

## Usage

Make your own copy of this repo by cloning it and starting fresh:

```bash
git clone --depth 1 https://github.com/dropseed/bolt-starter-app new-project
cd new-project
rm -rf .git
git init
```

Then, install the dependencies (note that you'll need [Poetry](https://python-poetry.org/) installed on your system):

```bash
./scripts/install
```

Now you can fire up the development server and open http://localhost:8000 in your browser:

```bash
bolt dev
```
