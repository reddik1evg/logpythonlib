import rich
from rich import print as pr
def ere(inf):
    pr('[red]ERROR[/red]:', inf)
def infolog(inf):
    pr('[blue]INFO[/blue]:', inf)
def warning(inf):
    pr('[yellow]WARNING[/yellow]:', inf)
