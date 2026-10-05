## Generate documentation index

### Index file

- feat: generate docs index
- generate file `docs/index.md`
- `index.md` must be regenerated completely on every command invocation
- use `docs/order.txt` to determine the order of files
- group files into sections based on their immediate parent folder
- files directly under `docs/` belong to the `## Documentation Index` section
- section names come from folder names
- convert kebab-case folder names to title case:
  - `getting-started` → `Getting Started`
  - `api-reference` → `Api Reference`

- convert file names from kebab-case to title case and remove the `.md` extension:
  - `file-name.md` → `File Name`
  - `api-reference.md` → `Api Reference`

- preserve acronyms/casing that cannot be inferred from kebab-case, e.g. `README.md` → `README`

### Example

#### Order file

given:

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

user decides order:

```text
README.md
reference/api.md
getting-started/configuration.md
getting-started/installation.md
```

#### Index file

`docs/index.md` should contain:

```md
## Documentation Index

- [README](README.md)

### Reference

- [Api](reference/api.md)

### Getting Started

- [Configuration](getting-started/configuration.md)
- [Installation](getting-started/installation.md)
```

### Command

- `proj docs gen_idx -p path_to_folder_with_md_files
