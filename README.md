<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/renpy-template/master/game/gui/window_icon.png" alt="Ren'Py Template">
</p>

# renpy-template

📖 Write visual novels with Ren'Py Template.

Play the game on:

- [remarkablegames](https://remarkablegames.org/renpy-template)

## Prerequisites

- [Ren'Py SDK](https://www.renpy.org/latest.html)

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/renpy-template.git
cd renpy-template
```

Rename the project:

```sh
git grep -l 'Renpy Template' | xargs sed -i '' -e 's/Renpy Template/My Novel/g'
```

```sh
git grep -l 'Renpy Template' | xargs sed -i '' -e 's/renpy-template/my-novel/g'
```

## Run

Change directory to Ren'Py SDK:

```sh
cd path/to/renpy-sdk
```

### CLI

Launch the project:

```sh
./renpy.sh path/to/renpy-template
```

### GUI

Open `Ren'Py Launcher`:

```sh
./renpy.sh launcher
```

Click `refresh` and select `renpy-template`

Click `Launch Project`

## License

[MIT](LICENSE)
