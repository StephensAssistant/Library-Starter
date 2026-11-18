# Library Starter

Create your own repository from the starter, or copy the tracked files into a new repository with a fresh history. Clone your copy, install Python 3.12 and run `python -m pip install -r .github/requirements-ci.txt`.

Create a `staging` branch from `main`. Read [AGENTS.md](AGENTS.md) before adding records. Configure your repository’s access, branch protection and chosen AI connection separately. Start with repository-scoped read access.

Run `python -B starter_record_smoke.py .` against a committed checkout to exercise the record paths in a disposable clone. See the [graph guide](.github/LIBRARY-GRAPH.md) to generate a visual from your own records.
