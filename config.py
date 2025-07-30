from libqtile.utils import guess_terminal
from libqtile.backend.wayland import InputConfig
from libqtile import layout

# import other stuff
from keys import keys
from groups import groups
from layouts import layouts, floating_layout
from mouse import mouse
from widgets import widget_defaults, extension_defaults, screens

terminal = guess_terminal()

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {
    "type:keyboard": InputConfig(
        kb_layout="us,us,ro", kb_variant=",intl,std", kb_options="grp:alt_shift_toggle"
    ),
}
# Add more rules for other devices or configurations as needed

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24
