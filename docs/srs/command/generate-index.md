## Generate documentation index

### Index file

* Generate file `docs/index.md`.
* `index.md` must be regenerated completely on every command invocation.
* Use `docs/order.txt` to determine the order of files.
* Group files into sections based on their immediate parent folder.
* Files directly under `docs/` belong to the `## Documentation Index` section.
* Section names come from folder names.
* Convert kebab-case folder names to title case:

  * `getting-started` → `Getting Started`
  * `api-reference` → `Api Reference`
* Convert file names from kebab-case to title case and remove the `.md` extension:

  * `file-name.md` → `File Name`
  * `api-reference.md` → `Api Reference`
* Preserve acronyms/casing that cannot be inferred from kebab-case, e.g. `README.md` → `README`.

Use this format:

```md
## Documentation Index

### Section

* [File Name](section/file-name.md)
```

For files directly under `docs/`:

```md
## Documentation Index

* [README](README.md)
```

### Example

Given:

```text
docs/
├── README.md
├── getting-started/
│   ├── installation.md
│   └── configuration.md
└── reference/
    └── api.md
```

`docs/order.txt` should contain:

```text
README.md
getting-started/installation.md
getting-started/configuration.md
reference/api.md
```

User decides order:

```text
README.md
reference/api.md
getting-started/configuration.md
getting-started/installation.md
```

`docs/index.md` should contain:

```md
## Documentation Index

* [README](README.md)

### Reference

* [Api](reference/api.md)

### Getting Started

* [Configuration](getting-started/configuration.md)
* [Installation](getting-started/installation.md)
```

### Commit

* feat: generate docs index
