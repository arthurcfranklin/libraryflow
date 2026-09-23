# Contributing to LibraryFlow

This document defines the development and contribution guidelines used to keep LibraryFlow consistent as the project evolves.

## Development Workflow

LibraryFlow follows an incremental development workflow:

```text
Roadmap
   ↓
Milestone
   ↓
Issue
   ↓
Implementation
   ↓
Validation
   ↓
Documentation
   ↓
Commit
   ↓
Release
```

Features and structural changes should remain aligned with the project roadmap, technical documentation, and current architecture.

## Branch Strategy

Development currently takes place on the `main` branch.

As the project grows, a broader branching strategy may be adopted when the additional separation becomes useful.

Possible future branches include:

```text
main
├── develop
├── feature/*
├── fix/*
└── docs/*
```

Branches should only be introduced when they improve the development workflow rather than adding unnecessary process overhead.

## Commit Convention

LibraryFlow uses a Conventional Commits-style convention.

| Type | Purpose | Example |
| --- | --- | --- |
| `feat` | New functionality | `feat: implement users module` |
| `fix` | Bug fix | `fix: resolve sidebar rendering issue` |
| `docs` | Documentation changes | `docs: update database documentation` |
| `refactor` | Internal restructuring without changing behavior | `refactor: reorganize services layer` |
| `style` | Interface or presentation changes | `style: improve dashboard layout` |
| `chore` | Maintenance and administrative tasks | `chore: update dependencies` |

Commit messages should be concise and describe the purpose of the change.

## Development Guidelines

Before committing a change:

- Validate the affected functionality.
- Review the implementation for unintended changes.
- Remove unused code when appropriate.
- Maintain consistency with the existing architecture.
- Update related documentation when behavior or structure changes.
- Keep changes focused on a clear purpose.

## Documentation

Documentation is maintained alongside the application in [`docs/`](./).

Changes that affect system behavior, architecture, requirements, or workflows should update the relevant documentation.

Depending on the change, this may include:

- [`requirements.md`](requirements.md)
- [`business-rules.md`](business-rules.md)
- [`use-cases/use-cases.md`](use-cases/use-cases.md)
- [`database.md`](database.md)
- [`api.md`](api.md)
- [`architecture.md`](architecture.md)
- [`roadmap.md`](roadmap.md)
- [`changelog.md`](changelog.md)

Use cases affected by a feature should also be reviewed individually in [`use-cases/`](use-cases/).

## Issues

Features, bugs, and relevant technical work should be tracked through GitHub Issues when appropriate.

A useful issue should clearly identify:

- the objective or problem;
- the expected behavior;
- relevant requirements or business rules;
- technical considerations when applicable.

Example:

```text
Title:
Implement Users Management Module

Description:
Implement the users CRUD according to requirements RF006 through RF009.
```

## Pull Requests

When pull requests are used, changes should be reviewed for:

- correct functionality;
- code quality;
- architectural consistency;
- visual consistency when the interface is affected;
- appropriate documentation updates;
- unintended regressions.

Pull requests should remain focused and avoid combining unrelated changes.

## Releases

LibraryFlow follows semantic versioning conventions:

```text
vMAJOR.MINOR.PATCH
```

Pre-release identifiers may be used while the project is under development:

```text
v0.5.0-beta
```

A release should represent a meaningful project milestone and should only be created after:

- the planned functionality is complete;
- affected functionality has been validated;
- relevant documentation has been updated;
- the changelog reflects the release.

## Milestones

Milestones organize larger stages of the product roadmap.

Current planned milestones include:

| Milestone | Status |
| --- | --- |
| Users Management Module | Planned |
| Loans Management Module | Planned |
| Authentication Module | Planned |
| Stable Release `v1.0.0` | Future |

For the complete development plan, see [`roadmap.md`](roadmap.md).

## Project Standards

Contributions should preserve the principles established throughout the project:

- clear and maintainable code;
- consistent architecture;
- incremental development;
- synchronized technical documentation;
- focused commits and changes;
- simple solutions where additional complexity provides no clear benefit.

These guidelines should evolve with the project as its architecture and development workflow mature.
