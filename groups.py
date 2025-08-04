from libqtile.config import Group

groups = [
    Group("1", spawn=["alacritty"], label=" "),
    Group("2", spawn=["qutebrowser"], label=""),
    Group(
        "3",
        label="",
    ),
    Group("4", label=""),
    Group(
        "5",
        label=" ",
    ),
]

