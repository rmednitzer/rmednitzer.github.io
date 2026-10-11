# Forgejo mirror workflows

This repository's authoritative CI runs on GitHub Actions. The Forgejo repository is a passive mirror and intentionally has no Forgejo Actions workflow or generic runner.

Forgejo searches `.forgejo/workflows` first and falls back to `.github/workflows` only if the Forgejo directory does not exist. Keep this README here to prevent GitHub-only workflows from being queued on the mirror. Do not put YAML workflow files in this directory without explicitly provisioning a repository-scoped Forgejo runner and reviewing its trust boundary.
