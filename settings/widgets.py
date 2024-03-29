from libqtile import widget
from .theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=10, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=10,
        padding=-12
    )

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='roboto',
            fontsize=10,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=10, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),
    separator(),
    powerline('color1', 'dark'),
    widget.Clock(**base(bg='color1'), format='%H:%M - %d/%m/%Y'),
    powerline('color2', 'color1'),
    icon(bg="color2", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(
        background=colors['color2'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),
    powerline('color3', 'color2'),
    widget.Battery(
        **base(bg='color3'), 
        charge_char=' ', 
        discharge_char='  ',
        empty_char='  ',
        format='{char} {percent:2.0%} {hour:d}:{min:02d}',
        full_char='  ',
        low_background='#ff0000',
    ),
    powerline('color4', 'color3'),
    widget.CurrentLayoutIcon(**base(bg='color4'), scale=0.65),
    widget.CurrentLayout(**base(bg='color4'), padding=5),
    powerline('dark', 'color4'),
    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline('color1', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    widget.CurrentLayout(**base(bg='color1'), padding=5),
    powerline('color2', 'color1'),
    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font',
    'fontsize': 10,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()