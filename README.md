<img src="https://boltpython.com/assets/img/bolthead.svg" width="30" height="30">

# bolt-starter-bare

This is the bare starter kit for [Bolt](https://boltpython.com/),
which includes [`bolt`](https://boltpython.com/docs/bolt) itself and [`bolt-dev`](https://boltpython.com/docs/bolt-dev) for easier development.

## Usage

Make a copy of this template repository by clicking the "Use this template" button or by running:

```bash
gh repo create new-project --template=dropseed/bolt-starter-bare --private --clone
```

Then, install the dependencies (note that you'll need [Poetry](https://python-poetry.org/) installed on your system):

```bash
./scripts/install
```

Now you can fire up the development server and open http://localhost:8000 in your browser:

```bash
bolt dev
```
