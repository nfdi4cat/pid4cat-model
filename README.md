[![CI - main](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/main.yaml/badge.svg)](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/main.yaml)
[![CI - docs](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/deploy-docs.yaml/badge.svg?branch=main)](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/deploy-docs.yaml)

# Persistent Identifiers for FAIR data in Catalysis

![pid4cat logo](docs/images/logo-with-text.svg)

**pid4cat** is NFDI4Cat´s service for metadata rich, universal persistent identifiers. pid4cat builds upon the handle-system (as DOIs do). pid4cat adds a **custom API** to a handle server and provides a **LinkML model for  PID-related metadata**. The metadata are stored in the handle records. **pid4cat**  persistent identifiers are used for samples, devices, and more, to ensure consistent tracking, integration, and accessibility of resources across both central and local RDM systems.

## pid4cat metadata model

This repository contains the **pid4cat service** documentation and the **pid4cat model** expressed as a [LinkML](https://linkml.io/) model. The model is a generic PID metadata model that may be useful beyond catalysis.

> Status: beta - This is in development and may still change.
> We are interested in feedback of potential users.
> Please use [issues](https://github.com/nfdi4cat/pid4cat-model/issues) for your comments, questions or ideas!

## Documentation

- [pid4cat](https://nfdi4cat.github.io/pid4cat-model) documentation
- [pid4cat-model](https://nfdi4cat.github.io/pid4cat-model/latest/elements/) metadata schema documentation
- [NFDI4Cat PID concept](nfdi4cat_details.md) - (older) information about the role and use of this model in NFDI4Cat.

## Repository Structure

- [docs/](docs/) - mkdocs-managed documentation
  - [elements/](docs/elements/) - generated schema documentation
- [examples/](examples/) - Examples of using the schema
- [project/](project/) - project files (these files are auto-generated, do not edit)
- [src/](src/) - source files
  - [pid4cat_model](src/pid4cat_model)
    - [schema](src/pid4cat_model/schema) -- LinkML schema
    - [datamodel](src/pid4cat_model/datamodel) -- generated Python data models
- [tests/](tests/) - Python tests
  - [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Contributors

A big thanks to all contributors! Without you pid4cat would not exist.

In addition to the [GitHub contributors](https://github.com/nfdi4cat/pid4cat-model/graphs/contributors), several people contributed offline:

- Preston Rodriguez (ORCID: [0000-0002-0377-5018](https://orcid.org/0000-0002-0377-5018)), @prestonrodrigues (implementation of handle API gateway server, operation of handle server)
- Mark Dörr (ORCID: [0000-0003-3270-6895](https://orcid.org/0000-0003-3270-6895)), @markdoerr (discussions on model and API)
- Volodymyr Kushnarenko (ORCID: [0000-0001-7427-2410](https://orcid.org/0000-0001-7427-2410)), @vkush (discussions on model, operation of handle server)
- Hendrik Borgelt (ORCID: [0000-0001-5886-7860](https://orcid.org/0000-0001-5886-7860)), @HendrikBorgelt (discussions on model)

Main author:

- David Linke (ORCID: [0000-0002-5898-1820](https://orcid.org/0000-0002-5898-1820)) - Idea, initial setup of repository, main developer of pid4cat-model, project coordination.

## License

The code and data model in this repository are distributed under the MIT license. The documentation, images and logos are CC-BY 4.0 licensed.

## Acknowledgement

The repository uses [linkml-project-copier](https://github.com/linkml/linkml-project-cookiecutter) as underlying project template.

This project started as an in-kind contribution of [Leibniz-Institut für Katalyse e.V.](https://www.catalysis.de) (Rostock, Germany) to the NFDI4Cat project.

After 2024-03-27 this work has been funded by the German Research Foundation (DFG) through the project "[NFDI4Cat](https://www.nfdi4cat.org) - NFDI for Catalysis-Related Sciences" (DFG project no. [441926934](https://gepris.dfg.de/gepris/projekt/441926934)), within the National Research Data Infrastructure ([NFDI](https://www.nfdi.de)) programme of the Joint Science Conference (GWK).
