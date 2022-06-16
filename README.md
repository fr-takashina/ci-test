# What this template provides

## Document templates

### Project charter

The project charter is usually a short document that explains a project clearly and concisely, and refers to more
detailed documents for additional information [^1]. A project charter should:

- Identify the scope of the project.
- Provide a shared understanding of the project objectives.
- Act as a contract between the project sponsor, key stakeholders and the project team, detailing responsibilities.

This project charter template is modified to match our style. It contains:

- Reasons for undertaking the project
- Objectives and constraints of the project, including
    - in-scope and out-of-scope items
    - schedules and milestones
- Team members and their responsibilities (perhaps in RACI chart)
- [Optional] Risks and issues

TODO: put a template.

<!--
Here is [a template](https://docs.google.com/document/d/1cShvfehW1RwJvx_Ww441wxH7B3WtM3byx23B59yn0u0/edit?usp=sharing).
-->

### Requirement definition

In a requirement definition document, you describe **what to implement** in detail. Each requirement should be linked to
a milestone defined in the project charter. Note that, since a requirement definition document is used to communicate
with non-tech members, that is, who will use the outcome (products, insights, etc.) of the project, it must be described
without technical details as much as possible.

TODO: put a template.

<!--
Here is [a template](https://docs.google.com/document/d/1x-8OGW7ZZbvUq6o751Jl6hT9R3uJHcwtCqe8I2zfs5M/edit?usp=sharing).
-->

### Basic design

In a basic design document, you describe **how to implement** the project objectives. You can add some figures like ER
diagram, flowchart, class diagram, etc. While it's important to avoid a predictable rework, be careful that premature
abstraction & over-specification can be more dangerous. They can lead to a lot of redesigns when the requirements
change, which often happens. Do not design *too much*.

More detailed designs (e.g., specification of class or function) would be written in source code comments. Thanks to
Sphinx, you can automatically generate documents from the comments.

You can find a sample in `docs` directory. We describe how to use this in the latter part of this document.

## Repository configurations

### Package manager

A package manager or package-management system is a collection of software tools that automates the process of
installing, upgrading, configuring, and removing computer programs for a computer in a consistent manner [^3]
. [Poetry](https://python-poetry.org/) is a modern package manager that has an exhaustive dependency resolver, safe
environment isolation, and intuitive CLI.

We describe how to use this in the latter part of this document.

### .gitignore

When you use Git, you should configure `.gitignore` to avoid sharing unnecessary files with other members, since it
prevents other members from easily understand your code. The commonly used sample for `.gitignore` is
published [here](https://github.com/github/gitignore). The proper setting changes depending on project specification.
For example, if you are using Python on macOS, you would
combine [the .gitignore for Python](https://github.com/github/gitignore/blob/main/Python.gitignore)
and [that for macOS](https://github.com/github/gitignore/blob/main/Global/macOS.gitignore).

This repository contains the `.gitignore` for Python & macOS. You can add more configuration, manually editing the file.

### Linters/formatters

In Python, there are too many linters/formatters to maintain. [pysen](https://github.com/pfnet/pysen) is a package that
orchestrates such linters/formatters with a single configuration file. Using pysen, you can run the following
linter/formatter without complicated configuration.

- black
- flake8
- isort
- mypy

We describe how to use this in the latter part of this document.

### Test automation

Test automation is the practice of automatically reviewing and validating a software product, such as a web application,
to make sure it meets predefined quality standards for code style, functionality (business logic), and user
experience [^2]. [pytest](https://docs.pytest.org/) is a common Python package that enables developers to write such an
automated test code easily.

We describe how to use this in the latter part of this document.

### TODO: CI/CD

This MUST be added in the future. Unfortunately, however, there is no available CI/CD service in our team for now.

# How to use this template

## How to start

After [installing poetry](https://python-poetry.org/docs/), you can install all dependencies by running the following
command at the root of the repository:

```bash
poetry install
```

Then you must:

- Replace repo name by your project's name.
    - VSCode Search & replace feature would help replace infile string 
    - You also have to change the directory name for source code root
- `poetry add` project-specific dependencies.
- Write your own code, tests, docs, and so on.

Optionally, you can:

- Update .gitignore (in particular, the setting for PyCharm is over-simplified for the boilerplate's own purpose).

## How to use package manager

See the [reference](https://python-poetry.org/).

Note that if something is going wrong, you might resolve the issue by clean-installing the packages. You can find the
path to the package by running the following command at the root of the repository:

```
poetry env info -p
```

Delete the displayed directory. Then, install the packages again:

```
poetry install
```

## How to build the docs

### Directory structure

We are using [Sphinx](https://www.sphinx-doc.org/) for documentation.

The contents of `docs/source` directory are used to build documents. Note that the directories that start with an
underscore is pre-defined, while the others are user-defined. `_static` is used for storing resources like images,
where `_template` should provide literally some templates for generating docs. You can find more detailed explanation in
the official document.

```
└─source
    ├─design
    ├─optimization
    ├─reference
    ├─_static
    └─_templates
```

### Build documents from source

You can build documents from `source` directory as following:

```
poetry run sphinx-build -b html ./docs/source ./docs/build/html
```

### Generate reference from source code comments

Using `sphinx-autogen`, we can generate reference from docstring (source code comments with
a [specific format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)).

```
poetry run sphinx-autogen -o ./docs/source/reference ./docs/source/reference/index.rst
```

**Use Google Style**. Technically, both NumPy Style and Google Style are available, which are very similar. The
importance is consistency within the team. We are using Google Style, so follow the standard.

## How to run linting/formatting

### Linting

```shell
poetry run pysen run lint
```

### Formatting

```shell
poetry run pysen run format
```

### Additional configuration

There are some configuration in `pyproject.toml`. You can turn on/off which linter/formatter will be used.

You have to register your own modules to `isort_known_first_party`. If you forgot this, the imports would be wrongly
sorted.

```toml
isort_known_first_party = ["pysen", "opt_app_boilerplate"]
```

You can configure which directory will be checked by changing the following line.

```toml
[tool.pysen.lint.source]
includes = ["opt_app_boilerplate"]  # lint only the production code
```

## How to run test

You can run test as following:

```shell
poetry run pytest ${test file or directory you want to run}
```

We put some test examples in this repository. Check `tests` and `data_test` directory to learn how they work.

---

[^1]: https://en.wikipedia.org/w/index.php?title=Project_charter&oldid=1078108175

[^2]: https://www.atlassian.com/devops/devops-tools/test-automation

[^3]: https://en.wikipedia.org/w/index.php?title=Package_manager&oldid=1070199878
