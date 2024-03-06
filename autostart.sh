#!/bin/bash
# Configuración de la pantalla.
xrandr --output HDMI-A-0 --mode 1280x1024 --pos 1366x0 --rotate normal --output DisplayPort-0 --primary --mode 1366x768 --pos 0x0 --rotate normal &
discord &

# Configuración del wallpaper.
feh --bg-fill /home/fer/.config/qtile/imgs/wall1.jpg  &

# El que pone el fadeout y las ventanas lindas:
picom &