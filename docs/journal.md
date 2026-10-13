Journal
TP01
Q1. Délai entre le premier commit et la fusion sur main
Premier commit :2026-10-13T06:46:21. Fusion : 2026-10-13T10:33:16.
(Les délais incluent l'attente de la revue de l'autre membre.)

Q2. Ce qui ne dépend pas de GitHub
Marche tel quel sur GitLab, Gitea ou Forgejo :

    Git lui-même : branches, commits, rebase, git add --resolved, --force-with-lease
    Commits conventionnels et signature SSH des commits et tags (gpg.format ssh, allowed_signers)
    pre-commit et ruff, pytest, le flux « branche courte, PR, revue, squash »


Change selon la forge :

    Les commandes gh (gh pr create, gh pr review, gh pr merge, gh api) : à remplacer par glab sur GitLab, tea sur Gitea, ou l'interface web
    L'enregistrement de la clé de signature et d'authentification (propre à chaque forge)
    Les règles de protection de branche et le vocabulaire (pull request devient merge request sur GitLab)


Q3. Pourquoi signer si la forge vérifie déjà qui pousse ?
La forge authentifie la personne qui pousse, pas l'auteur déclaré dans le commit : user.name et user.email sont de simples champs que n'importe qui peut écrire. Une signature prouve cryptographiquement qui a créé le commit, indépendamment de la forge. Elle reste vérifiable sur un clone poussé par quelqu'un d'autre, ou après la migration du dépôt vers une autre forge.

Ce qui m'a pris le plus de temps
tout
