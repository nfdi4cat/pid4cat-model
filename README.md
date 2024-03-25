[![CI - main](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/main.yml)
[![CI - docs](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/deploy-docs.yml/badge.svg?branch=main)](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/deploy-docs.yml)

# PID4cat model

> Status: alpha - This is in early development and may change.
> We are interested in feedback of potential users.
> Don't hesitate to create an [issue](https://github.com/nfdi4cat/pid4cat-model/issues)!

A LinkML model for handle-based PIDs for resources in catalysis.

## Documentation

- [PID4Cat model](https://nfdi4cat.github.io/pid4cat-model) documentation
- [NFDI4Cat PID concept](nfdi4cat_details.md) - more information about the  role and use of this model.

## Repository Structure

- [examples/](examples/) - example data
- [project/](project/) - project files (do not edit these)
- [src/](src/) - source files (edit these)
  - [pid4cat_model](src/pid4cat_model)
    - [schema](src/pid4cat_model/schema) - LinkML schema
      (edit this)
    - [datamodel](src/pid4cat_model/datamodel) - generated
      Python datamodel
- [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site
</details>

## Contributors

A big thanks to all [contributors](https://github.com/nfdi4cat/pid4cat-model/graphs/contributors).

Main author:

- David Linke (ORCID: 0000-0002-5898-1820) - Idea and initial setup of repository. Current maintainer.

## License

The code in this repository is distributed under MIT license.

## Acknowledgement

[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter) provided the base setup for this repository.

This project started as an in-kind contribution of [Leibniz-Institut für Katalyse e.V.](https://www.catalysis.de) (Rostock, Germany) to the NFDI4Cat project.

After 2024-03-27 this work has been funded by the German Research Foundation (DFG) through the project "[NFDI4Cat](https://www.nfdi4cat.org) - NFDI for Catalysis-Related Sciences" (DFG project no. [441926934](https://gepris.dfg.de/gepris/projekt/441926934)), within the National Research Data Infrastructure ([NFDI](https://www.nfdi.de)) programme of the Joint Science Conference (GWK).
