# Git Enumerator

A small Bash utility to extract, view, and analyze modified resources or file routes from Git commits.

## Features

- Extract file paths modified in specific commits (`-c`).
- Process lists of commit hashes from a file (`-l`).
- Read and show resource paths from an external list (`-r`).
- Specify a custom path to a `.git` repository directory (`-p`).

## Usage

```bash
./gite.sh [options]
```

### Options

| Option | Description |
| --- | --- |
| `-h` | Show help message |
| `-c <hash>` | Specify a single commit hash |
| `-l <file>` | Provide a file containing a list of commit hashes |
| `-r <file>` | Provide a file containing a list of specific routes |
| `-p <path>` | Set the path to the `.git` directory (defaults to current directory) |

## Examples

Extract resources modified in a specific commit:

```bash
./gite.sh -c <commit_hash> -p /path/to/repo
```

Process a list of commits from a file:

```bash
./gite.sh -l commits.txt
```

