## Project Commands

### Commit and Push to last commit

```sh
repo="/home/atari-monk/atari-monk/project/project-tools"
git -C "$repo" add . &&
git -C "$repo" commit --amend -m "docs: reorganized docs" &&
git -C "$repo" push --force origin main
```
