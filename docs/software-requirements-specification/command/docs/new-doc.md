## New Doc

### Command

* `proj docs new -p path_to_docs -c category/subcategory -n file_name`
* Also use aliases --path, --category, --name
* Path `path_to_docs` - is path to docs or any folder with md files
* Path `category/subcategory` is path of categories folders for md files, it can be nested to any level
* Name `file_name` is a kebab-case, lower letters md file name

### Behaviour

* User copies markdown to clipboard
* Command establishes new file path by combining parts
* New file path: `path_to_docs/category/subcategory/file_name.md`
* Takes clipboard content and stores it in path
* Log operation

### Commits 

* feat: new doc