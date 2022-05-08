# python-NBU-project
###

### Install packages 
```shell
pip install -r requirements.txt
```
### Packages
- https://pygame-menu.readthedocs.io/en/4.2.7/

### Examples to use
- venv/Lib/site-packages/pygame_menu/examples/game_selector.py

## Dependencies
- pygame
- pygame-menu
- pyinstaller

## Make an executable file
Run:
```shell
pyinstaller main.py --name NAME --noconsole -i File.ico
```

## Folder Structure
```
├──data                         # Game Files
│   ├──Explosion                # Explosion animation
│   ├──GAME_OVER_SCREEN         # Game Over screen animation
│   ├──Gif_Animation            # To be deleted?
│   ├──Healthbar                # Healthbar images
│   ├──Laser Sprites            # Laser sprite images
│   ├──sprites                  # Sprites
│   │    ├──items               # Items sprites
│   │    ├──Ship                # Ship sprites
├──src                          # Code files
├──venv                         # Python venv folder
```
[comment]: <> (## TODO)

[comment]: <> (- [ ] Menu flow)

[comment]: <> (- [ ] Start the game)

[comment]: <> (- [ ] Create Player)

[comment]: <> (- [ ] Move Player)

[comment]: <> (- [ ] Create Enemy)

[comment]: <> (- [ ] Create Alien or Boss)

[comment]: <> (- [ ] Shoot bullet from Player)