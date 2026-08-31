# Git Commands for This Project

## Initialize repository

```bash
git init
```

## Check status

```bash
git status
```

## Add files

```bash
git add .
```

## Commit changes

```bash
git commit -m "Initial Spotify playlist builder setup"
```

## Create a main branch

```bash
git branch -M main
```

## Connect to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

## Push code

```bash
git push -u origin main
```

## Pull latest changes

```bash
git pull origin main
```

## Useful commands

```bash
git log
git checkout -b feature/new-feature
git stash
git stash pop
```

## Important reminder

Do not commit sensitive values such as:

- Spotify client secrets
- token cache files
- local environment files

The project already includes a `.gitignore` file to avoid tracking those files.
