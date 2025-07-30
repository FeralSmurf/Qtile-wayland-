from libqtile import bar, widget
from libqtile.config import Screen

from colors import background, foreground, red, green

widget_defaults = dict(
    font="DejaVuSansM Nerd Font, Font Awesome 7, SemiBold",
    fontsize=16,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # Left widgets
                widget.GroupBox(
                    font="DejaVuSansM Nerd Font, Font Awesome 7, SemiBold",
                    active=foreground,
                    this_current_screen_border=foreground,
                    padding=4,
                    margin_x=4,
                ),
                widget.Prompt(),
                widget.Spacer(length=bar.STRETCH),
                # Center widgets
                widget.WindowName(foreground=foreground, width=600, max_chars=100),
                widget.Systray(),
                widget.Spacer(length=bar.STRETCH),
                # Right widgets
                widget.Chord(
                    chords_colors={
                        "launch": (red, foreground),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(fmt=" "),
                widget.CheckUpdates(
                    distro="Arch",
                    custom_command="checkupdates",
                    display_format="󰮯 {updates}",
                    # no_update_string="󰮯 0",
                    colour_have_updates=foreground,
                    colour_no_updates=foreground,
                    update_interval=1800,
                ),
                widget.TextBox(fmt=" "),
                widget.Wlan(fmt="  {}", format="{essid}", foreground=foreground),
                widget.TextBox(fmt=" "),
                widget.DF(
                    partition="/home",
                    format="{uf}{m}",
                    fmt=" {}",
                    visible_on_warn=False,
                    foreground=foreground,
                ),
                widget.TextBox(fmt=" "),
                widget.Battery(
                    format="{char} {percent:2.0%}",
                    fmt="{}",
                    foreground=foreground,
                    discharge_char="",
                    charge_char="",
                    low_percentage=0.20,
                    low_foreground=red,
                    charging_foreground=green,
                    not_charging_char=" =",
                ),
                widget.TextBox(fmt=" "),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    fmt=" {}",
                    change_command="brightnessctl set {}",
                    step=5,
                    brightness_command="brightnessctl get",
                    foreground=foreground,
                ),
                widget.TextBox(fmt=" "),
                widget.Volume(
                    fmt=" {}",
                    foreground=foreground,
                ),
                widget.TextBox(fmt=" "),
                widget.Clock(
                    format="%Y-%m-%d %a %H:%M",
                    fmt=" {}",
                    foreground=foreground,
                ),
            ],
            30,
            background=background,
            foreground=foreground,
            margin=[0, 0, 0, 0],  # [top, right, bottom, left] margin
        ),
        # Set static wallpaper
        wallpaper="~/Downloads/Wallpapers/darkwinter.jpg",
        wallpaper_mode="fill",
    ),
]
