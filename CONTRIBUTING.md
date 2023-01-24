# CONTRIBUTING

Thanks for taking the time to contribute! Please check out our [CODE_OF_CONDUCT.md](https://github.com/Sann5/ultra-prot/blob/main/CODE_OF_CONDUCT.md) which specifies guidelines for members and contributors which aim at building and maintaining a friendly and safe environment.

## How do I submit a change?

We welcome contributions via pull requests:

- Fork the repo and create a branch from the default branch
- If you have added code that should be tested, add tests
- If any documentation updates are needed, make them
- Ensure the test suite passes and the code lints
- Submit the pull request

Once you have submitted your PR:

- Your PR will be reviewed by our team.
- Upon approval, PR is to be merged using the "squash and merge" option, so that the commit history remains linear and readable.

## Code style and format

- This repo uses pre-commit hooks to style and format the code automatically ([black](https://github.com/psf/black) and [pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks)). Please consider using [flake8](https://github.com/pycqa/flake8) and [mypy](https://github.com/python/mypy) for additional formatting and static type checking. All of these tools are considered dependencies and are therefore included in the `environment.yml`.
- Please comment and add Google style docstrings where applicable (example of [Google style docstrings](https://github.com/sphinx-contrib/napoleon/blob/83bf1963096490dd666f93ef5a9ed1cb229fc3ec/docs/source/example_google.py#L66)).
