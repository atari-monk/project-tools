## New Doc

### Command

- feat: new doc
- `proj docs new -p path_to_docs -c category/subcategory -n file_name`
- use aliases --path, --category, --name
- path `path_to_docs` - is path to docs or any folder with md files
- path `category/subcategory` is path of categories folders for md files, it can be nested to any level
- name `file_name` is a kebab-case, lower letters md file name

### Behaviour

- user copies markdown to clipboard
- command establishes new file path by combining parts
- new file path: `path_to_docs/category/subcategory/file_name.md`
- takes clipboard content and stores it in path
- log operation
