import random

THEMES = {
    "ubuntu": {
        "name": "ubuntu",
        "back": "#300a24",
        "fore": "#ffffff",
        "green": "#ffffff",
        "purple": "#ffffff",
        "orange": "#ffffff",
        "cyan": "#ffffff",
        "username": "#5cbe09",
    },
    "default": {
        "name": "default",
        "back": "#272822",
        "fore": "#f8f8f2",
        "green": "#a6e22e",
        "purple": "#ae81ff",
        "orange": "#cc6633",
        "cyan": "#8be9fd",
        "username": "#f70202",
    },
    "dracula": {
        "name": "dracula",
        "back": "#282A36",
        "fore": "#F8F8F2",
        "green": "#50fa7b",
        "purple": "#bd93f9",
        "orange": "#ffb86c",
        "cyan": "#8be9fd",
        "username": "#E356A7",
    },
    "monokai": {
        "name": "monokai",
        "back": "#2e2e2e",
        "fore": "#d6d6d6",
        "green": "#b4d273",
        "purple": "#9e86c8",
        "orange": "#e87d3e",
        "cyan": "#8be9fd",
        "username": "#f92672",
    },
    "atom": {
        "name": "atom",
        "back": "#161719",
        "fore": "#c5c8c6",
        "green": "#94fa36",
        "purple": "#b9b6fc",
        "orange": "#f5ffa8",
        "cyan": "#85befd",
        "username": "#fd5ff1",
    },
    "github": {
        "name": "github",
        "back": "#f4f4f4",
        "fore": "#3e3e3e",
        "green": "#87d5a2",
        "purple": "#e94691",
        "orange": "#2e6cba",
        "cyan": "#666666",
        "username": "#de0000",
    },
    "googledark": {
        "name": "googledark",
        "back": "#202124",
        "fore": "#E8EAED",
        "green": "#34A853",
        "purple": "#A142F4",
        "orange": "#FBBC05",
        "cyan": "#EA4335",
        "username": "#4285F4",
    },
    "googlelight": {
        "name": "googlelight",
        "back": "#FFFFFF",
        "fore": "#5F6368",
        "green": "#34A853",
        "purple": "#A142F4",
        "orange": "#EA4335",
        "cyan": "#24C1E0",
        "username": "#4285F4",
    },
    "powershell": {
        "name": "powershell",
        "back": "#052454",
        "fore": "#F6F6F7",
        "green": "#1CFE3C",
        "purple": "#D33682",
        "orange": "#FEFE45",
        "cyan": "#EF2929",
        "username": "#F6F6F7",
    },
}


def get_theme(theme_name=None):

    return THEMES.get(theme_name, THEMES.get(random.choice(list(THEMES.keys()))))


available_themes = list(THEMES.keys())
