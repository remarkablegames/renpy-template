<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/renpy-template/master/game/gui/window_icon.png" alt="Ren'Py Template">
</p>

# Ren'Py Template

![release](https://img.shields.io/github/v/release/remarkablegames/renpy-template)
[![build](https://github.com/remarkablegames/renpy-template/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/renpy-template/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/renpy-template/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/renpy-template/actions/workflows/lint.yml)

📖 Write visual novels with Ren'Py Template.

Play the game:

- [remarkablegames](https://remarkablegames.org/renpy-template)

Or download:

- [Windows](https://github.com/remarkablegames/renpy-template/releases/latest/download/win.zip)
- [Mac](https://github.com/remarkablegames/renpy-template/releases/latest/download/mac.zip)
- [Linux](https://github.com/remarkablegames/renpy-template/releases/latest/download/pc.zip)

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)

### Audio

- [Kenney](https://kenney.nl/assets/interface-sounds)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/renpy-template.git
cd renpy-template
```

Rename the project:

```sh
git grep -l "Ren'Py Template" | xargs sed -i '' -e "s/Ren'Py Template/My Novel/g"
```

```sh
git grep -l 'renpy-template' | xargs sed -i '' -e 's/renpy-template/my-novel/g'
```

Replace the assets:

- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`
- [ ] [`icon.icns`](https://anyconv.com/png-to-icns-converter/)
- [ ] [`icon.ico`](https://anyconv.com/png-to-ico-converter/)
- [ ] `web-icon.png`
- [ ] `web-presplash.webp`

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
