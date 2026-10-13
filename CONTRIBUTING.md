# Contribuer

## Flux de travail
1. Partir de `main` à jour : `git switch main && git pull`
2. Créer une branche courte : `feat/...`, `fix/...`, `docs/...`, `chore/...`
3. Faire de petits commits, puis `git push -u origin <branche>`
4. Ouvrir une PR avec `gh pr create --fill --base main`
   (description : quoi, pourquoi, comment tester)
5. L'autre membre relit, demande des changements si besoin, puis approuve
6. Fusion par squash, branche supprimée : `gh pr merge --squash --delete-branch`

## Convention de commits
Conventional Commits : `type(portée): description`
Types : `feat`, `fix`, `docs`, `test`, `chore`, `refactor`.
Exemple : `feat(api): ajouter POST /reset`
Les commits sont signés (clé SSH).

## Lancer les tests
    python3 -m venv .venv && source .venv/bin/activate
    pip install -e ".[dev]"
    pytest -q

## pre-commit
    pre-commit install
    pre-commit run --all-files
Ne pas contourner avec `--no-verify`.
