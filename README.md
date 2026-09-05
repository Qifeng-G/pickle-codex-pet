# Pickle Codex Pet

Pickle is a photorealistic animated desktop pet for the Codex desktop app, based on a real golden-russet dog.

## Install with Codex

Copy the prompt below, paste it into Codex, choose `pickle` or `xiaozuo` when asked, and approve the installation:

```text
Install a Codex desktop pet from https://github.com/Qifeng-G/pickle-codex-pet. Ask me whether I want `pickle` or `xiaozuo` (小佐), then clone the repository, run `scripts/install.sh <chosen-pet>`, verify the installed files, and tell me when to restart Codex.
```

Codex will install the chosen pet, verify the copied files, and tell you when to restart the app.

## Reusable Codex skill

This repo also includes a reusable Codex skill for creating photorealistic Codex pets from your own real pet photos and videos.

Copy this prompt into Codex to install the skill:

```text
Install the Real Pet Codex Pet skill from https://github.com/Qifeng-G/pickle-codex-pet/tree/main/skills/real-pet-codex-pet.
```

## Repository structure

```text
pickle-codex-pet/
├── pet/                 # Files copied into the Codex pets directory
├── previews/            # MP4 previews for the nine animation states
├── docs/                # Visual documentation
├── qa/                  # Atlas validation evidence
├── skills/              # Reusable Codex skill for making real-pet desktop pets
├── scripts/install.sh   # Repeatable local installer used by Codex
├── LICENSE
└── README.md
```

## Contributing

Bug reports and improvements are welcome through GitHub issues and pull requests. When changing the atlas, preserve the packaged spritesheet dimensions and validate transparency, row semantics, animation continuity, and pet identity before submitting.

## License

This project is available under the [MIT License](LICENSE). The license covers the included pet artwork, configuration, previews, and documentation.
