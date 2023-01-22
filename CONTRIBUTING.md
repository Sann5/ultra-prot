# CONTRIBUTING

Thanks for taking the time to contribute! Please check out our [code of conduct](CODE_OF_CONDUCT.md) which specifies guideleines for members and contributers which aim at building and mantaining a friendly and safe environment.

## Reporting a bug or suggesting an enhancement?

- As a first step, please search in the [existing issues](https://github.com/Sann5/USCPa/issues).
- If your point hasn't already been addressed, [create an issue](https://github.com/Sann5/USCPa/issues/new/choose) providing the details as instructed in the template.

## How do I submit a change?

We welcome contributions via pull requests:

- Fork the repo and create a branch from the default branch
- If you have added code that should be tested, add tests
- If any documentation updates are needed, make them
- Ensure the test suite passes and the code lints
- Submit the pull request

Once you have submitted your PR:

- You PR will be rewied by our team.
- Upon approval, PR is to be merged using the "squash and merge" option, so that the commit history remains linear and readable.

## Code style and format

This repo uses pre-commit hooks to style and format the code automatically ([black](https://github.com/psf/black) and [pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks)). Please consider using [flake8](https://github.com/pycqa/flake8) and [mypy](https://github.com/python/mypy) for additional formating and static type checking. All of these tools are considered dependencies and are therefore included in the `environment.yml`.
  