# Repository Guidelines

## Project Structure & Module Organization
- `source/` holds the reStructuredText content; group new topics beside related chapters (for example, project-focused pages live under `source/project-*`).
- Static assets belong in `source/_static/` for shared CSS/JS and `source/img/` for screenshots; reference them with relative paths so Sphinx copies them into `_static`.
- The Sphinx config (`source/conf.py`) controls extensions and theme overrides; update it when adding extensions or shared substitutions.
- Built artifacts land in `build/`; this directory is disposable and should not be checked in.

## Build, Test, and Development Commands
- `make html` builds the full manual into `build/html/` with warnings treated as errors, ensuring clean docs.
- `make clean` removes the build cache; run it before final builds to avoid stale assets.
- `make linkcheck` (Sphinx passthrough) validates outbound links; use it for PRs that touch external URLs.
- `make watch` rebuilds on file changes when `inotifywait` is installed, useful for iterative editing.

## Coding Style & Naming Conventions
- Write docs in reStructuredText with 3-space indentation for nested lists and directives.
- Use sentence-case section headings (`Heading Like This`) to match existing files and keep underline lengths equal to heading text when using underlined styles.
- Prefer descriptive cross-reference labels (`.. _project-home:`) and reuse existing labels instead of duplicating anchors.
- Store screenshots as compressed PNG/WebP and name them after the feature (`project-home-banner.png`); document updates should include refreshed images when UI changes.

## Testing Guidelines
- Treat a warning-free `make html` run as the primary test; the `-W` flag fails the build on broken references or bad syntax.
- For substantial link updates, run `make linkcheck` and fix reported redirects or failures before merging.
- When adding snippets that rely on code blocks, preview the rendered HTML locally (`build/html/index.html`) to verify syntax highlighting and admonitions.

## Commit & Pull Request Guidelines
- Follow the repository’s imperative, present-tense commit style (e.g., `Update launch CoCalc link`); keep summaries under ~72 characters.
- Group related doc edits into focused commits so reviewers can track topic-specific changes.
