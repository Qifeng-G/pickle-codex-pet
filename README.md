# Pickle Codex Pet

Pickle is a photorealistic animated desktop pet for the Codex desktop app, based on a real golden-russet dog.

## Install with Codex

Copy the prompt below, paste it into Codex, and approve the installation when asked:

```text
Install the Pickle Codex desktop pet from https://github.com/Qifeng-G/pickle-codex-pet. Clone the repository, run scripts/install.sh, verify the installed files, and tell me when to restart Codex.
```

Codex will install the pet, verify the copied files, and tell you when to restart the app.

## Animation states

| State | Behavior |
| --- | --- |
| `idle` | Calm breathing and blinking |
| `running-right` | Runs toward the right |
| `running-left` | Runs toward the left |
| `waving` | Stands happily and wags the tail |
| `jumping` | Rises up and bumps a ball with the nose |
| `failed` | Disappointed reaction |
| `waiting` | Waits attentively for input |
| `running` | Focused task execution, not literal running |
| `review` | Curious close-up inspection |

## Repository structure

```text
pickle-codex-pet/
├── pet/                 # Files copied into the Codex pets directory
├── previews/            # MP4 previews for the nine animation states
├── docs/                # Visual documentation
├── qa/                  # Atlas validation evidence
├── scripts/install.sh   # Repeatable local installer used by Codex
├── LICENSE
└── README.md
```

## Contributing

Bug reports and improvements are welcome through GitHub issues and pull requests. When changing the atlas, preserve the v2 dimensions and validate transparency, row semantics, animation continuity, and pet identity before submitting.

## License

This project is available under the [MIT License](LICENSE). The license covers the included pet artwork, configuration, previews, and documentation.
